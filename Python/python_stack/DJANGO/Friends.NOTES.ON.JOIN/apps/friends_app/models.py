from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Friendships(models.Model):
    friend1 = models.ForeignKey(User, related_name = 'friend_one')
    friend2 = models.ForeignKey(User, related_name = 'friend_two')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # THIS IS THE JOIN TABLE!
