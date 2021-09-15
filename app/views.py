from django.shortcuts import render
from .models import (
    Contact_me, About,
    Skills, Portfolio,
    Experience, Education,
    References
)


def contactme(request):
    contactme = Contact_me.objects.all()
    about = About.objects.all()
    skills = Skills.objects.all()
    portfolio = Portfolio.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    reference = References.objects.all()

    context = {
        'contactme': contactme,
        'about': about,
        'skills': skills,
        'portfolio': portfolio,
        'experience': experience,
        'education': education,
        'reference': reference
    }
    return render(request, 'index.html', context)
