from django import forms
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

class LoginForm(forms.Form):
    username=forms.CharField(label="Username",max_length=256,widget=forms.TextInput(attrs={'placeholder':"Username",'style':"padding:2%;width:100%"}))
    password=forms.CharField(label="Password",max_length=256,widget=forms.PasswordInput(attrs={'placeholder':"Password",'style':"padding:2%;width:100%"}))

    def __init__(self,*args,**kwargs):
        self.request=kwargs.pop('request',None)
        super(LoginForm,self).__init__(*args,**kwargs)

    def clean(self):
        '''
            Validate user credentials.
            Task:
            1. Get Username and password.
            2. Check provided informaion is valid.
                2.1. If information is valid, authenticate user.
                    2.1.1 If user is authenticate then login user.
                    2.1.2 If user is not authenticate then raise validation error.
            3. Return cleaned_data
        '''
        #1
        cleaned_data=super().clean()
        #2
        if(self.is_valid()):
            #2.1
            auth_user=authenticate(username=cleaned_data['username'],password=cleaned_data['password'])
            #2.1.1
            if(auth_user):
                login(self.request,auth_user)
            #2.1.2
            else:
                raise forms.ValidationError('Incorrect Username and Password')
        #3
        return cleaned_data

class SignUpForm(forms.Form):
    firstname=forms.CharField(label="First name",max_length=30,widget=forms.TextInput(attrs={'placeholder':"First name",'style':"padding:3%;width:100%"}))
    lastname=forms.CharField(label="Last name",max_length=30,widget=forms.TextInput(attrs={'placeholder':"Last name",'style':"padding:3%;width:100%"}))
    username=forms.CharField(label="User name",max_length=50,widget=forms.TextInput(attrs={'placeholder':"User name",'style':"padding:3%;width:100%"}))
    email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'placeholder':"Email",'style':"padding:3%;width:100%"}))
    password=forms.CharField(label="Password",max_length=100,widget=forms.PasswordInput(attrs={'placeholder':"Password",'style':"padding:3%;width:100%"}))
    conformpassword=forms.CharField(label="Conform Password",max_length=100,widget=forms.PasswordInput(attrs={'placeholder':"Conform Password",'style':"padding:3%;width:100%"}))

    def clean_firstname(self):
        firstname=self.cleaned_data['firstname']
        if(not bool(re.fullmatch('[A-Za-z]{2,30}([A-Za-z]{2,30})?',firstname))):
            raise forms.ValidationError('!@#$%^&*()~+= are not allowed')
        return firstname

    def clean_lastname(self):
        lastname=self.cleaned_data['lastname']
        if(not bool(re.fullmatch('[A-Za-z]{2,30}([A-Za-z]{2,30})?',lastname))):
            raise forms.ValidationError('!@#$%^&*()~+= are not allowed')
        return lastname

    def clean_username(self):
        '''
            Validate username field.
            Task:
            1. Get the value of username field.
            2. Get the all existing user.
            3. Check username is registered or not.
                3.1. If username matched , raise validation error
            4. Return username value.
        '''
        #1
        username=self.cleaned_data['username']
        #2
        all_user=User.objects.all()
        #3
        for user in all_user:
            if(user.username == username):
                #3.1
                raise forms.ValidationError('Username Must be unique')
        #4
        return username

    def clean_email(self):
        '''
            Validate Email field.
            Task:
            1. Get the Email field value.
            2. Get all Existing user.
            3. Check provided Email is register or not.
                3.1. If match found raise validation error.
            4. return value of email
        '''
        #1
        email=self.cleaned_data['email']
        #2
        all_user=User.objects.all()
        #3
        for user in all_user:
            if(user.email == email):
                #3.1
                raise forms.ValidationError('Email is already registered')
                break
        #4
        return email

    def clean_password(self):
        '''
            Validate Password field
            Task:
            1. Get the value of password field.
            2. Check length of password.
                2.1. If length is less then 10 raise validation error
            3. Check password contain whitespaces or not
                3.1. If whitespaces found raise validation error
            4. Return password value
        '''
        #1
        password=self.cleaned_data['password']
        #2
        if(len(password) < 10):
            #2.1
            raise forms.ValidationError('Length of password must be greater or equal to 10')
        #3
        if(" " in password):
            #3.1
            raise forms.ValidationError('Spaces are not allowed')
        #4
        return password

    def clean_conformpassword(self):
        '''
            Validate the conformpassword
            Task:
            1. Get the value of conformpassword field.
            2. Check if value of password exist or not in cleaned_data object.
                2.1. If exist Get the value of password field.
                    2.1.1. Compair password and conformpassword are unequal or not.
                        2.1.1.1. If unequal raise validation error
            3. return conformpassword
        '''
        #1
        conform_password=self.cleaned_data['conformpassword']
        cleaned_data=super().clean()
        #2
        if(cleaned_data.get('password',False)):
            #2.1
            password=cleaned_data['password']
            #2.1.1
            if(password != conform_password):
                 #2.1.1.1
                 raise forms.ValidationError('Password does not match')
        #3
        return conform_password

    def clean(self):
        '''
            Create a New User.
            Task:
            1. Get the information given by user.
            2. Check the information is correct or not.
                2.1. If information is correct, Create a NewUser.
                2.2. If information is not correct do nothing.
            3. return the information.
        '''
        #1
        cleaned_data=super().clean()
        #2
        if(self.is_valid()):
            password=cleaned_data['password']
            #2.1
            new_user=User.objects.create_user(
                            email=cleaned_data['email'],
                            username=cleaned_data['username'],
                            password=password,
                        )

            new_user.firstname=cleaned_data['firstname']
            new_user.lastname=cleaned_data['lastname']
            new_user.save()
        #2.2
        return cleaned_data
