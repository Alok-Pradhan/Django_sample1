from django.db import models
from django import forms
# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()

    def _str_(self):
        return self.name

class Signup(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
   # contact =models.CharField(max_length=100)
    uname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def _str_(self):
        return self.name

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)