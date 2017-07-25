from __future__ import unicode_literals
from django.db import models
from ..log_reg_app.models import User
# ^ Gets access for views.py to models in other apps

class MessageManager(models.Manager):
    # def message_validation(self, postData):
    def send(self, message, user_from, user_to):
        return True

class Message(models.Model):
    message = models.TextField(max_length=1000)
    user_from = models.ForeignKey(User, related_name="from_user")
    user_to = models.ForeignKey(User, related_name="to_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = MessageManager()
    messageManager = MessageManager()
    def __repr__(self):
        return "*** Message - ID: {} MESSAGE: {} FROM: {} TO: {}".format(self.id, self.message, self.user_from, self.user_to)

# Related name userful for REVERSE LOOK UP
