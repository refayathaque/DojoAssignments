from __future__ import unicode_literals

from django.db import models

from django.shortcuts import render, redirect

from django.contrib import messages

from datetime import datetime

from ..app1.models import User

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

full_name = re.compile(r'^([a-z A-Z])*$')

class QuoteManager(models.Manager):

    def create_quote(self, data, session):

        counter = 0
        errors = []

        if len(data['quoted_by']) < 3:
            errors.append('QUOTED BY NAME MUST BE LONGER!')
            return (False, errors)
        else:
            counter += 1

        if(len(data['quote']) < 10):
            errors.append('QUOTED MUST BE LONGER!')
            return (False, errors)
        else:
            counter += 1

        if counter == 2:
            Quote.objects.create(quote = data['quote'], posted_by = session, quoted_by = data['quoted_by'])
            return (True, data['quoted_by'])

# Table for Quotes
class Quote(models.Model):
    quote = models.CharField(max_length=1000)
    posted_by = models.CharField(max_length=100)
    quoted_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()
    # def __str__(self):
    #     return self.posted_by + " " + self.quoted_by

# Joined table for User and Quotes
class User_Quote(models.Model):
    quote_id = models.ForeignKey(Quote, related_name="quote_name")
    user_id = models.ForeignKey(User, related_name="user_name")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
####
