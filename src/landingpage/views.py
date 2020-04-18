from django.shortcuts import render,redirect
from django.views.generic import View
from landingpage.forms import LoginForm,SignUpForm
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
class LandingPage(View):
    '''
        LandingPage class give's the response at BaseUrl of website.
        In response these view provide the landingpage.
    '''
    def get(self,request,*args,**kwargs):
        #1
        if(not request.user.is_anonymous):
            #1.1
            return redirect('home')
        return render(request,'landingpage.html')

class AuthenticationUser(View):
    def get(self,request,*args,**kwargs):
        #1
        if(not request.user.is_anonymous):
            #1.1
            return redirect('landingpage')
        return render(request,"auth.html",{'LoginForm':LoginForm,'SignUpForm':SignUpForm})

class Login(View):
    def get(self,request,*args,**kwargs):
        '''
            Task:
            1. Check if user is anonymous or not.
                1.1. If user is not anonymous then redirect to home page.
                1.2. If user is anonymous then render login page with login form.
        '''
        #1
        if(not request.user.is_anonymous):
            #1.1
            return redirect('landingpage')
        #1.2
        return redirect('auth')


    def post(self,request,*args,**kwargs):
        '''
            Task:
            1. Create login form object with arrguments provided information by user and current user request object.
            2. Check the user provided information is correct or not.
                2.1. If Information is correct then login user internally in LoginForm.
                    2.1.1. Add a success message in messages storage to pass it to home page.
                    2.1.2. Then redirect towards home page.
                2.2. If information is InCorrect.
                    2.2.1. Add the error messages to messages storage to pass it to login page.
                    2.2.2. Then redirect towards login page.
        '''
        #1
        loginform=LoginForm(request.POST,request=request)
        #2
        if(loginform.is_valid()):
            #2.1
            try:
                request.user.PROFILE
            except:
                return redirect('profile')
            else:
                messages.add_message(request,messages.INFO,"You have successfully login")
                return redirect('landingpage')
        else:
            #2.2
            messages.add_message(request,messages.ERROR,loginform.errors['__all__'][0])
            #2.2.1
            return redirect('auth')

class SignUp(View):
    '''
        SignUp is a view class to register a new user.
    '''
    def get(self,request,*args,**kwargs):
        '''
            Get method render signup html page and inject the SignUpForm.
            Task:
            1. Check user is anonymous or not.
                1.1. If user is not anonymous redirect towards home page.
                1.2. If user is anonymous render signup page with SignUpForm injected in it.
        '''
        #1
        if(not request.user.is_anonymous):
            #1.1
            return redirect('landingpage')
        #1.2
        return redirect('auth')


    def post(self,request,*args,**kwargs):
        '''
            Post method Validate information and create NewUser.
            Task:
            1. Create SignUpForm object with arguments contain imfromation provided by user.
            2. Validate information provided by user.
                2.1. If information is valid then internally create NewUser.
                    2.1.1. Add success message to message storage to pass message to home page.
                    2.1.2. Redirect towards home page.
                2.2. If information is invalid then.
                    2.2.1. Render the signup page with SignUpForm and ERRORS Injected in it.

        '''
        #1
        signup_form=SignUpForm(request.POST)
        #2
        if(signup_form.is_valid()):
          #2.1
            #2.1.1
            messages.add_message(request,messages.SUCCESS,"Account is successfully create, Please login!")
            #2.1.2
            return redirect('auth')
        #2.2
        else:
            #2.2.1
            return render(request,"auth.html",{'SignUpForm':SignUpForm(initial=signup_form.cleaned_data),'Errors':signup_form.errors,'LoginForm':LoginForm})

class Logout(View):
    '''
        Logout View
    '''
    def get(self,request,*args,**kwargs):
        '''
            Task:
            1.  Check User is anonymous or not.
                1.1. If user is anonymous redirect towards landingpage.
                1.2. If user is not anonymous.
                    1.2.1. Logout the user.
                    1.2.2. add success message.
                    1.2.3. redirect ot landingpage.
        '''
        #1
        if(request.user.is_anonymous):
            #1.1
            return redirect('landingpage')
        #1.2
        else:
            #1.2.1
            logout(request)
            #1.2.2
            messages.add_message(request,messages.SUCCESS,"Your logged out successfully")
            #1.2.3
            return redirect('landingpage')
