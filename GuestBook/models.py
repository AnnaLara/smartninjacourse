from google.appengine.ext import ndb

class Message(ndb.Model):
    name = ndb.StringProperty(default = "Anonymous")
    email = ndb.StringProperty()
    text = ndb.TextProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
