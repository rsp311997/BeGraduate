from django.shortcuts import render,redirect
from django.views.generic import View
from account.forms import ProfileForm
from django.contrib import messages
# Create your views here.
class Profile(View):
    '''
        Profile view used to perform some task such as:
        render profile page,
        inject ProfileForm,
        Create new Profile.
    '''
    def get(self,request,*args,**kwargs):
        '''
            Render profile page.
            Task:
            1. Check user is anonymous or not.
                1.1. If User is anonymous then redirect user to landing page.
                1.2. If User is not anonymous.
                    1.2.1. Check profile record exist for current user or not.
                        1.2.1.1. If record not found, store message and render profile page with ProfileForm injected in it.
                        1.2.1.2. If record exist, redirect towards home page.
        '''
        #1
        if(request.user.is_anonymous):
            #1.1
            return redirect('landingpage')
        #1.2
        else:
            #1.2.1
            try:
                request.user.PROFILE
            except:
                #1.2.1.1
                messages.add_message(request,messages.INFO,'Complete your profile')
                return render(request,'profile.html',{'ProfileForm':ProfileForm})
            else:
                #1.2.1.2
                profile=request.user.PROFILE
                return render(request,'profile.html',{'Profile':profile})

    def post(self,request,*args,**kwargs):
        '''
            Validate and create profile.
            Task:
            1. Create the Profile object with profile fields value and request object.
            2. Validate profile fields and if values are correct then create new profile for user internally in ProfileForm.
                2.1. redirect towards profile page.
            3. If Validation fail then render profile page with Profile form and errors injected in it.
        '''
        #1
        profileform=ProfileForm(request.POST,files=request.FILES,request=request)
        #2
        if profileform.is_valid():
            #2.1
            return redirect('profile')
        else:
            #3
            return render(request,'profile.html',{'ProfileForm':ProfileForm(initial=profileform.cleaned_data),'Errors':profileform.errors})


class EditProfile(View):
    '''
        EditProfile view is used to edit profile.
    '''
    def get(self,request,*args,**kwargs):
        '''
            Task:
            1. Check user is anonymous or not, If user is anonymous redirect to landingpage.
            2. If user is not anonymous get the profile form database.
            3. render editprofile page with ProfileForm with profile object injected in page.
        '''
        #1
        if(request.user.is_anonymous):
            return redirect('landingpage')
        #2
        profile=request.user.PROFILE
        initial={
            'nickname':profile.nickname,'dob':profile.dob,'country':profile.country,'state':profile.state,
            'city':profile.city,'schoolname':profile.schoolname,'collegename':profile.collegename,
            'occupation':profile.occupation,'contact':profile.contact,'describe':profile.describe,'profile_pic':profile.profile_pic
        }
        #3
        return render(request,'editprofile.html',{'ProfileForm':ProfileForm(initial=initial)})

    def post(self,request,*args,**kwargs):
        profile=ProfileForm(request.POST,files=request.FILES,request=request)
        if(profile.is_valid()):
            return redirect('profile')
        else:
            return render(request,'editprofile.html',{'ProfileForm':ProfileForm(initial=profile.cleaned_data),'Errors':profile.errors})
