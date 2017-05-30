from __future__ import unicode_literals

from django.db import models

from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

class UserManager(models.Manager):

    def login(self, data):

        counter = 0
        errors = []

        # USERNAME
        if(len(data['username']) < 1):
            errors.append('USERNAME CANNOT BE BLANK!')

            return (False, errors)

        else:

            if User.objects.filter(username = data['username']): # returns list with objects inside so is 'truthy'
                counter += 1

            else:
                errors.append("USERNAME NOT VALID!")
####

        # PASSWORD
        if(len(data['password']) < 8 and len(data['password']) >= 1):
            errors.append("PASSWORD NOT VALID!")

        elif(len(data['password']) < 1):
            errors.append("PASSWORD CANNOT BE BLANK!")

        else:

            if User.objects.filter(password = data['password']):
                counter += 1

            else:
                errors.append("PASSWORD NOT VALID!")
####

        # FINAL CHECK
        if counter == 2:
            logged_in_user_object = User.objects.get(username = data['username'])
            print logged_in_user_object # Refayat Haque refayathaque

            return (True, data['username'])

        else:

            return (False, errors)
####

    def registration(self, data):

        counter = 0
        errors = []

        # NAME
        if data['name'].isalpha() and len(data['name']) > 2:
            counter += 1

        elif data['name'].isalpha() and len(data['name']) < 2:
            errors.append('NAME NOT VALID!')

        elif len(data['name']) < 1:
            errors.append('NAME CANNOT BE BLANK!')

        # need validation for 'space', e.g. Refayat Haque doesn't work

        # USERNAME
        if data['username'].isalpha() and len(data['username']) > 2:
            counter += 1

        elif data['username'].isalpha() and len(data['userame']) < 2:
            errors.append('USERNAME NOT VALID!')

        elif len(data['username']) < 1:
            errors.append('USERNAME CANNOT BE BLANK!')

        elif User.objects.filter(username = data['username']):
            errors.append("YOU CANNOT REGISTER AGAIN!")
####

        # PASSWORD
        if(len(data['password']) >= 8):
            counter += 1

        elif(len(data['password']) < 8 and len(data['password']) >= 1):
            errors.append("PASSWORD IS TOO SHORT!")

        elif(len(data['password']) < 1):
            errors.append("PASSWORD CANNOT BE BLANK!")

        if(data['password'] == data['password_confirmation'] and len(data['password']) > 0 and len(data['password_confirmation']) > 0 ):
            counter += 1

        elif(data['password'] != data['password_confirmation']):
            errors.append('PASSWORDS DO NOT MATCH!')
####

        # FINAL CHECK

        if counter == 4:
            User.objects.create(name = data['name'], username = data['username'], password = data['password'])
            registered_user_object = User.objects.get(username = data['username'])
            print registered_user_object # Refayat Haque refayathaque

            return (True, data['username'])

        else:

            return (False, errors)
####

# TABLE
class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.name + " " + self.username
####
