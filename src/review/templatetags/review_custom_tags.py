from django import template

register=template.Library()

@register.filter('reviewPageRating')
def reviewPageRating(reviews):
    temp=0
    totalReviews=len(reviews)

    if(totalReviews != 0):
        for review in reviews:
            temp+=review.rate_college

        rating=round(temp/totalReviews,1)
        return {'rating':rating,'totalReviews':totalReviews}


@register.filter('stars')
def five_stars(reviews,value):
    temp=0
    for review in reviews:
        if(review.rate_college==int(value)):
            temp+=1
    return temp

@register.filter('percent')
def percent(reviews,value):
    temp=0
    for review in reviews:
        if(review.rate_college==int(value)):
            temp+=1
    percent = (temp/len(reviews))*100
    return percent
