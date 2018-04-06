from google.appengine.ext import ndb

class Email(ndb.Model):
    sender = ndb.StringProperty()
    recipient = ndb.StringProperty()
    subject = ndb.TextProperty()
    message = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    deleted = ndb.BooleanProperty(default=False)
