from django.shortcuts import render,redirect
from django.views.generic import View
from institute.models import InstituteModel#,Address
from django.db.models import Q
from institute.forms import FilterForm
from django.core.paginator import Paginator

# Create your views here.
class Home(View):
    def filter(self,filterform,college):
        if(filterform.is_valid()):
            if filterform.cleaned_data.get('college',False):
                college=college.filter(abriviation__iexact=filterform.cleaned_data['college'])
            if filterform.cleaned_data.get('country',False):
                college=college.filter(country__iexact=filterform.cleaned_data['country'])
            if filterform.cleaned_data.get('state',False):
                college=college.filter(state__iexact=filterform.cleaned_data['state'])
            if filterform.cleaned_data.get('city',False):
                college=college.filter(city__iexact=filterform.cleaned_data['city'])
            return college


    def get(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect('landingpage')
        else:
            college = InstituteModel.objects.all()
            filterform=FilterForm(request.GET)
            college=self.filter(filterform,college)
            paginator = Paginator(college,6)
            total_pages=paginator.num_pages

            if(request.GET.get('next',False)):
                next=int(request.GET.get('next'))
                page=paginator.page(next)
                return render(request,'home.html',{'FilterForm':FilterForm(initial=request.GET),"page":page,"page_number":next,"total_pages":total_pages})
            elif(request.GET.get('pre',False)):
                pre=int(request.GET.get('pre'))
                page=paginator.page(pre)
                self.aggregate(page)
                return render(request,'home.html',{'FilterForm':FilterForm(initial=request.GET),"page":page,"page_number":pre,"total_pages":total_pages})
            else:
                page=paginator.page(1)
                return render(request,'home.html',{'FilterForm':FilterForm,"page":page,"page_number":1,"total_pages":total_pages})


class Detail(View):
    def get(self,request,id,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect('landingpage')
        institute = InstituteModel.objects.get(id=id)
        return render(request,'details.html',{'institute':institute})


class Pics(View):
    def get(self,request,id,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect('landingpage')
        institute = InstituteModel.objects.get(id=id)
        pics = institute.INSTITUTE_IMAGES.all()
        return render(request,'pics.html',{"Pics":pics})


def Description(request,id,*args,**kwargs):
    if request.user.is_anonymous:
        return redirect('landingpage')
    institute = InstituteModel.objects.get(id=id)
    description=institute.describe
    return render(request,'description.html',{'Description':description})
