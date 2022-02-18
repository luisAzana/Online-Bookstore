# Django
from cProfile import label
import imp
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Utilities
import datetime


class RenewBookForm(forms.Form):
    """ Renew book Form """
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError('Invalid date - renewal in past')
        
        # Check data is in range librarian allowed to change (+4 weeks).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Invalid date - renewal more than 4 weeks ahead')
        
        # Remember to always return the cleaned data.
        return data       
    

class SignupForm(forms.Form):
    """ Signup Form """
    username = forms.CharField(label=False, min_length=4, max_length=50, widget = forms.TextInput(
                                                                                               attrs={
                                                                                                    'placeholder':'username',
                                                                                                    'class': 'form-control',
                                                                                                    'required': True}
                                                                                               ))
    password = forms.CharField(label=False, max_length=70,widget = forms.PasswordInput(
                                                                                         attrs={
                                                                                               'placeholder':'password',
                                                                                               'class': 'form-control',
                                                                                               'required': True}
                                                                                          ))
    password_confirmation = forms.CharField(label=False, max_length=70, widget = forms.PasswordInput(
                                                                                               attrs={
                                                                                                    'placeholder':'password confirmation',
                                                                                                    'class': 'form-control',
                                                                                                    'required': True}
                                                                                               ))
     
    first_name = forms.CharField(label=False, min_length=2, max_length=50, widget = forms.TextInput(
                                                                                               attrs={
                                                                                                    'placeholder':'first name',
                                                                                                    'class': 'form-control',
                                                                                                    'required': True}
                                                                                               ))
    last_name  = forms.CharField(label=False, min_length=2, max_length=50 , widget = forms.TextInput(
                                                                                               attrs={
                                                                                                    'placeholder':'last name',
                                                                                                    'class': 'form-control',
                                                                                                    'required': True}
                                                                                               ))
     
    email = forms.CharField(label=False, min_length=6, max_length=70, widget = forms.EmailInput(
                                                                                               attrs={
                                                                                                    'placeholder':'email',
                                                                                                    'class': 'form-control',
                                                                                                    'required': True}
                                                                                               ))
    def verify_username_unique(self):
        """ Username must be unique """
        username = self.cleaned_data['username']
        query = User.objects.filter(username=username).exists()
        if query:
            raise forms.ValidationError('Username is alredy in use')
        return username
    
    def verify_password(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')
        return data
    
    def save(self):
        """ Create user """
        data = self.cleaned_data
        data.pop('password_confirmation')
        User.objects.create_user(**data)
        