from django import forms
from django.contrib.auth.models import User
from account.models import ProfileModel
import re

class ProfileForm(forms.Form):
    nickname=forms.CharField(widget=forms.TextInput(attrs={"style":'width:100%;padding:2%;',"placeholder":'Nick Name'}))
    dob=forms.DateField(widget=forms.TextInput(attrs={"style":'width:100%;padding:2%;',"placeholder":'Date of birth'}))
    country=forms.CharField(widget=forms.TextInput(attrs={"style":'width:100%;padding:2%;',"placeholder":'Country Name'}))
    state=forms.CharField(widget=forms.TextInput(attrs={"style":'width:100%;padding:2%;',"placeholder":'State Name'}))
    city=forms.CharField(widget=forms.TextInput(attrs={"style":'width:100%;padding:2%;',"placeholder":'City Name'}))
    schoolname=forms.CharField(widget=forms.TextInput(attrs={"style":'width:100%;padding:2%;',"placeholder":'School Name'}))
    collegename=forms.CharField(widget=forms.TextInput(attrs={"style":'width:100%;padding:2%;',"placeholder":'College Name'}))
    occupation=forms.CharField(widget=forms.TextInput(attrs={"style":'width:100%;padding:2%;',"placeholder":'Occupation'}))
    contact=forms.CharField(widget=forms.TextInput(attrs={"style":'width:100%;padding:2%;',"placeholder":'Contact'}))
    describe=forms.CharField(widget=forms.TextInput(attrs={"style":'width:100%;padding:2%;',"placeholder":'Describe'}))
    profile_pic=forms.ImageField()

    def __init__(self,*args,**kwargs):
        self.request=kwargs.pop('request',None)
        super(ProfileForm,self).__init__(*args,**kwargs)

    def clean_nickname(self):
        nickname=self.cleaned_data['nickname']
        if(not nickname.isalpha()):
            raise forms.ValidationError('Only special character and space are not allowed')
        return nickname

    def clean_country(self):
        country=self.cleaned_data['country']
        if(not country.isalpha()):
            raise forms.ValidationError('Only special character and space are not allowed')
        return country

    def clean_state(self):
        state=self.cleaned_data['state']
        return state

    def clean_city(self):
        city=self.cleaned_data['city']
        if(not city.isalpha()):
            raise forms.ValidationError('Only special character and space are not allowed')
        return city

    def clean_schoolname(self):
        schoolname=self.cleaned_data['schoolname']
        return schoolname

    def clean_collegename(self):
        collegename=self.cleaned_data['collegename']
        return collegename

    def clean_occupation(self):
        occupation=self.cleaned_data['occupation']
        if(not occupation.isalpha()):
            raise forms.ValidationError('Only special character and space are not allowed')
        return occupation

    def clean_contact(self):
        contact=self.cleaned_data['contact']
        if(not contact.isnumeric()):
            raise forms.ValidationError('0 to 9 digits are allowed only')
        if(len(contact) != 10):
            raise forms.ValidationError('Contact number must be length of 10 digits')
        return contact

    def clean_describe(self):
        describe=self.cleaned_data['describe']
        return describe

    def clean(self):
        '''
            Create and update profile.
            Task:
            1. Get data from the user.
            2. Validate all fields.
            3. Check profile object for user exist or not.
                3.1. If exist update information in profile object.
                3.2. If not exist create new profile object.
        '''
        #1
        cleaned_data=super().clean()
        #2
        if(self.is_valid()):
            #3
            try:
                #3.1
                profile=self.request.user.PROFILE
                profile.nickname=cleaned_data['nickname']
                profile.dob=cleaned_data['dob']
                profile.country=cleaned_data['country']
                profile.state=cleaned_data['state']
                profile.city=cleaned_data['city']
                profile.schoolname=cleaned_data['schoolname']
                profile.collegename=cleaned_data['collegename']
                profile.occupation=cleaned_data['occupation']
                profile.contact=cleaned_data['contact']
                profile.describe=cleaned_data['describe']
                profile.profile_pic=cleaned_data['profile_pic']
                profile.save(update_fields={'nickname','dob','country','state','city','schoolname','collegename','occupation','contact','describe','profile_pic'})
            except:
                #3.2
                profile=ProfileModel.objects.create(
                                                nickname=cleaned_data['nickname'],dob=cleaned_data['dob'],country=cleaned_data['country'],
                                                state=cleaned_data['state'],city=cleaned_data['city'],occupation=cleaned_data['occupation'],
                                                collegename=cleaned_data['collegename'],schoolname=cleaned_data['schoolname'],
                                                contact=cleaned_data['contact'],describe=cleaned_data['describe'],profile_pic=cleaned_data['profile_pic'],
                                                user=self.request.user
                                              )
                profile.save()

        return cleaned_data
