from __future__ import unicode_literals

from django.db import models

from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

import re # REGEX (Regular Expression) module

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def login(self, data):

        counter = 0
        errors = []

        # EMAIL
        if(len(data['email']) < 1):
            errors.append('EMAIL CANNOT BE BLANK!')

            return (False, errors)

        elif not EMAIL_REGEX.match(data['email']):
            errors.append("EMAIL NOT VALID!")

        else:

            if User.objects.filter(email = data['email']): # returns list with objects inside so is 'truthy'
                counter += 1

            else:
                errors.append("EMAIL NOT VALID!")
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
            logged_in_user_object = User.objects.get(email = data['email'])
            print logged_in_user_object # Refayat Haque refayathaque@gmail.com

            return (True, data['email'])

        else:

            return (False, errors)
####

    def registration(self, data):

        counter = 0
        errors = []

        # NAMES (FIRST and LAST)
        if data['first_name'].isalpha() and len(data['first_name']) > 2:
            counter += 1

        elif data['first_name'].isalpha() and len(data['first_name']) < 2:
            errors.append('FIRST NAME NOT VALID!')

        elif len(data['first_name']) < 1:
            errors.append('FIRST NAME CANNOT BE BLANK!')

        if data['last_name'].isalpha() and len(data['last_name']) > 2:
            counter += 1

        elif data['last_name'].isalpha() and len(data['last_name']) < 2:
            errors.append('LAST NAME NOT VALID!')

        elif len(data['last_name']) < 1:
            errors.append('LAST NAME CANNOT BE BLANK!')

        # EMAIL
        if(len(data['email']) < 1):
            errors.append("EMAIL CANNOT BE BLANK!")

        elif User.objects.filter(email = data['email']):
            errors.append("YOU CANNOT REGISTER AGAIN!")

        elif not EMAIL_REGEX.match(data['email']):
            errors.append("EMAIL NOT VALID!")

        else:
            counter += 1
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

        if counter == 5:
            User.objects.create(first_name = data['first_name'], last_name = data['last_name'], email = data['email'], password = data['password'])
            registered_user_object = User.objects.get(last_name = data['last_name'])
            print registered_user_object # Refayat Haque refayathaque@gmail.com

            return (True, data['email'])

        else:

            return (False, errors)
####

# TABLE
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email
####
