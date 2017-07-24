from __future__ import unicode_literals
from django.db import models
import bcrypt
import re # Regex

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z]+$')
password_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$')

class UserManager(models.Manager):
    def registration_validation(self, postData):
        counter = 0
        errors = {}
        # Username check
        if len(postData['username']) < 8 and not name_regex.match(postData['username']):
            errors["username"] = "username should be more than 8 letters, and cannot have numbers or symbols"
        if len(postData['username']) < 8 and len(postData['username']) >= 1:
            errors["username"] = "username should be more than 8 letters"
        if not name_regex.match(postData['username']):
            errors["username"] = "username cannot have numbers or symbols"
        if len(postData['username']) < 1:
            errors["username"] = "username cannot be blank"
        if len(postData['username']) > 8 and name_regex.match(postData['username']):
            counter += 1
        # Email check
        if len(postData['email']) < 1:
            errors["email"] = "email cannot be blank"
        if not email_regex.match(postData['email']):
            errors["email"] = "email must be valid"
        if email_regex.match(postData['email']):
            counter += 1
        # Password check
        if len(postData['password']):
            errors['password'] = "password cannot be blank"
        if len(postData['c_password']):
            errors['password'] = "must confirm password"
        if postData['password'] == postData['c_password']:
            if not password_regex.match(postData['password']):
                errors['password'] = "password doesn't meet requirements"
            else:
                counter +=1
                hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        if postData['password'] != postData['c_password']:
            errors['password'] = "passwords don't match"
        # Final check
        if counter == 3:
            User.objects.create(username = postData['username'], email = postData['email'], password = hashed_password)
        else:
            return errors;

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
