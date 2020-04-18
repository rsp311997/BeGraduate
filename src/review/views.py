from django.shortcuts import render,redirect
from django.views.generic import View
from institute.models import InstituteModel
from django.core.paginator import Paginator
from review.models import Review
import time
# Create your views here.

class ReviewView(View):
    def get(self,request,id,*args,**kwargs):
        if(not request.user.is_authenticated):
            return redirect('landingpage')
        else:
            if(request.GET.get('pre',False)):
                current_page=int(request.GET.get('pre'))
            elif(request.GET.get('next',False)):
                current_page=int(request.GET.get('next'))
            else:
                current_page=1

            Instituties=InstituteModel.objects.get(id=id)
            reviews=Instituties.REVIEWS.all()
            paginator=Paginator(reviews,6)
            page=paginator.page(current_page)
            return render(request,"reviewlist.html",{'AllReviews':reviews,'Reviews':page,'current_page':current_page,'total_pages':paginator.num_pages,'institute_id':id})

    def post(self,request,*args,**kwargs):
        institute_id=int(request.POST['institute_id'])
        institute=InstituteModel.objects.get(id=institute_id)
        rate_college=request.POST['rate_college']
        rate_tpo=request.POST['rate_tpo']
        rate_principal=request.POST['rate_principal']
        rate_director=request.POST['rate_director']
        your_view=request.POST['your_view']
        pros=request.POST['pros']
        cons=request.POST['cons']
    

        new_review=Review.objects.create(
                        user_id=request.user,
                        institite_id=institute,
                        rate_principal=rate_principal,
                        rate_director=rate_director,
                        rate_tpo=rate_tpo,
                        rate_college=rate_college,
                        your_view=your_view,
                        pros=pros,
                        cons=cons
                        )

        return redirect('review',institute_id)
