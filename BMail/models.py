from google.appengine.ext import ndb

class Email(ndb.Model):
    sender = ndb.StringProperty()
    recipient = ndb.StringProperty()
    subject = ndb.TextProperty()
    message = ndb.TextProperty()
    deletedBySender = ndb.BooleanProperty(default=False)
    deletedByRecipient = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    deleted = ndb.BooleanProperty(default=False)
