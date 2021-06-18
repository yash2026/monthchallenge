from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect 
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string


dic_challenges = {
    "january":"Eat no meat month!",
    "february":"No game month!",
    "march":"Go for a walk daily!",
    "april":"Be safe and aware!",
    "may":"Best month and lovely days... Enjoy!",
    "june":"Holidays",
    "july":"Sometimes good and sometimes bad!",
    "august":"Awesome weather!",
    "september":"Eat no meat month!",
    "october":"Go for a walk daily!",
    "november":"Be safe and aware!",
    "december":None
    }
 

def index(request):
    months = list(dic_challenges.keys())

    return render(request , "month/index.html" , {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = list(dic_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
        
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args= [redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthlychallenges(request, month):
    try:
        challenge_text = dic_challenges[str(month)]
        return render(request,'month/challenges.html',{
            "text":challenge_text,
            "month_name": month.capitalize()
            })
    except:
        raise Http404()
    

