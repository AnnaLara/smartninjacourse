#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Email
from datetime import datetime

from google.appengine.api import users


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

def emailFilter(atr_name, value, email_list):
    for element in email_list:
        if element.atr_name != value:
            email_list.remove(element)
    return email_list


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}

        user = users.get_current_user()
        params["user"] = user

        if user:
            logged_in = True
            logout_url = users.create_logout_url('/')
            params["logout_url"] = logout_url
        else:
            logged_in = False
            login_url = users.create_login_url('/')
            params["login_url"] = login_url

        params["logged_in"] = logged_in

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.redirect_to("Inbox")

        else:
            return self.render_template("hello.html")


class NewEmailHandler(BaseHandler):
    def get(self):
        return self.render_template("new_email.html")

    def post(self):
        sender = users.get_current_user().email()
        recipient = self.request.get("recipient")
        subject = self.request.get("subject")
        message = self.request.get("message")

        email = Email(sender = sender, recipient = recipient, subject = subject, message = message.replace("<script>", ""))
        email.put()

        return self.render_template("message_sent.html")

class InboxHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        emails = Email.query(Email.recipient == user.email()).fetch()
        params = {"emails": emails, "user": user, "view_name": "Inbox"}
        self.render_template("view_emails.html", params = params)


class SentEmailsHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        emails = Email.query(Email.sender == user.email()).fetch()
        params = {"emails": emails, "user": user, "view_name": "Sent"}
        self.render_template("view_emails.html", params = params)


class MessageDetailsHandler(BaseHandler):
    def get(self, email_id):
        user = users.get_current_user()
        title = "Email details"
        email = Email.get_by_id(int(email_id))

        params = {"email": email, "user": user, "title": "title"}
        self.render_template("email_details.html", params = params)



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/new-email', NewEmailHandler),
    webapp2.Route('/inbox', InboxHandler, name = "Inbox"),
    webapp2.Route('/sent', SentEmailsHandler),
    webapp2.Route('/emails/<email_id:\d+>', MessageDetailsHandler),
], debug=True)
