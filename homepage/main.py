#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


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
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

class BlogHandler(BaseHandler):
    def get(self):
        return self.render_template("blog.html")

class ProjectsHandler(BaseHandler):
    def get(self):
        return self.render_template("projects.html")

class SkillsHandler(BaseHandler):
    def get(self):
        return self.render_template("skills.html")

class EducationHandler(BaseHandler):
    def get(self):
        return self.render_template("education.html")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/blog.html', BlogHandler),
    webapp2.Route('/projects.html', ProjectsHandler),
    webapp2.Route('/skills.html', SkillsHandler),
    webapp2.Route('/education.html', EducationHandler),
], debug=True)
