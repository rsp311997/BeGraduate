from django import template

register=template.Library()

@register.filter('sub')
def sub(value,arg):
    return value-arg

@register.filter('firstThreeImages')
def firstThreeImages(images):
    return images[0:3]

@register.filter('first500Characters')
def first500Characters(charaters):
    return charaters[0:500]

@register.filter('firstTwoReviews')
def firstTwoReviews(reviews):
    return reviews[0:2]

@register.filter('rate_college')
def rate_principal(reviews):
    temp=0.0
    if reviews:
        for review in reviews:
            temp+=review.rate_college
        rating=temp/len(reviews)
        return round(rating,1)
    return temp


@register.filter('rate_principal')
def rate_principal(reviews):
    temp=0.0
    if reviews:
        for review in reviews:
            temp+=review.rate_principal
        rating=temp/len(reviews)
        return round(rating,1)
    return temp

@register.filter('rate_director')
def rate_principal(reviews):
    temp=0.0
    if reviews:
        for review in reviews:
            temp+=review.rate_director
        rating=temp/len(reviews)
        return round(rating,1)
    return temp

@register.filter('rate_tpo')
def rate_principal(reviews):
    temp=0.0
    if reviews:
        for review in reviews:
            temp+=review.rate_tpo
        rating=temp/len(reviews)
        return round(rating,1)
    return temp
