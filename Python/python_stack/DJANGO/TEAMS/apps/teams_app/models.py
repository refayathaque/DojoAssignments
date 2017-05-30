from __future__ import unicode_literals

from django.db import models

from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

from ..login_registration_app.models import User

class UserManager(models.Manager):

    def make_team(self, data):

        counter = 0
        errors = []

        # TEAM NAME
        if(len(data['team_name']) < 1):
            errors.append('TEAM NAME CANNOT BE BLANK!')
            return (False, errors)

        elif Team.objects.filter(name = data['team_name']):
            errors.append('THIS TEAM ALREADY EXISTS!')
            return (False, errors)

        else:
            counter += 1

        if counter == 1:
            Team.objects.create(name = data['team_name'])
            return (True, data['team_name'])
####

# TABLES
class Team(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.name

# JOINED TABLE
class User_Team(models.Model):
    team_id = models.ForeignKey(Team, related_name="team_name")
    user_id = models.ForeignKey(User, related_name="user_name")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
####
