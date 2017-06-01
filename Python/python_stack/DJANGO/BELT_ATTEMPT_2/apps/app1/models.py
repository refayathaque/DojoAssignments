from __future__ import unicode_literals

from django.db import models

from django.shortcuts import render, redirect

from django.contrib import messages

from datetime import datetime

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

full_name = re.compile(r'^([a-z A-Z])*$')

class UserManager(models.Manager):

    # Registration validation
    def registration(self, data):

        counter = 0
        errors = []

        # Name validation w/ regex
        if len(data['name']) > 2 and full_name.match(data['name']):
            counter += 1

        elif data['name'].isalpha() and len(data['name']) < 2:
            errors.append('NAME NOT VALID!')

        elif len(data['name']) < 1:
            errors.append('NAME CANNOT BE BLANK!')

        # Alias validation
        if data['alias'].isalpha() and len(data['alias']) > 2:
            counter += 1

        elif data['alias'].isalpha() and len(data['alias']) < 2:
            errors.append('ALIAS NOT VALID!')

        elif len(data['alias']) < 1:
            errors.append('ALIAS CANNOT BE BLANK!')

        elif User.objects.filter(alias = data['alias']):
            errors.append("THIS ALIAS EXISTS! TRY ANOTHER!")

        elif EMAIL_REGEX.match(data['alias']):
            errors.append("ALIAS CANNOT BE AN EMAIL!")

        # EMAIL
        if(len(data['email']) < 1):
                errors.append("EMAIL CANNOT BE BLANK!")

        elif User.objects.filter(email = data['email']):
                errors.append("YOU CANNOT REGISTER AGAIN!")

        elif not EMAIL_REGEX.match(data['email']):
                errors.append("EMAIL NOT VALID!")

        else:
            counter += 1

        # Password validation
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

        # Birth date validation
        if not data['birth_date']:
            errors.append('FILL OUT BIRTH DATE!')
            return (False, errors)

        birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
        # minimum_age = datetime.strptime(data['travel_end'], '%Y-%m-%d')

        # if minimum_age < birth_date:
        #     errors.append('YOU MUST BE AT LEAST 18 TO JOIN!')
        #     return (False, errors)
        if birth_date > datetime.now():
            errors.append('YOU CANNOT BE BORN IN THE FUTURE!')
            return (False, errors)
        else:
            counter += 1

        # Final registration validation check
        if counter == 6:
            User.objects.create(name = data['name'], alias = data['alias'], email = data['email'], password = data['password'], birth_date = data['birth_date'])

            return (True, data['email'])

        else:

            return (False, errors)

    # Login validation
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

        # FINAL CHECK
        if counter == 2:

            return (True, data['email'])

        else:

            return (False, errors)

# TABLE
class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    # def __str__(self):
    #     return self.name + " " + self.alias + " " + self.email
