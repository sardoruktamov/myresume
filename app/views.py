from django.shortcuts import render, redirect
from .models import (
    Contact_me, About,
    Skills, Portfolio,
    Experience, Education,
    References, Contact
)
from django.core.mail import send_mail
from django.conf import settings


def contactme(request):
    # if request.method == "GET":
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
    # else:
    #     full_name = request.POST['full_name']
    #     email = request.POST['email']
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     msg = 'Sizga shaxsiy saytingizdan ' + full_name + ' xabar yubordi. ' + '\n' + subject + ' xabar mavzusi: ' + '\n' + 'elektron pochtasi: ' + email + '\n' + 'xabar mazmuni: ' + '\n' + message
    #     send_mail(
    #         'Yangi xabar',
    #         msg,
    #         settings.EMAIL_HOST_USER,
    #         ['sardorbek.uktamov.1@mail.ru'],
    #         fail_silently=False,
    #     )
    #
    #     contact_user = Contact(
    #         full_name=full_name,
    #         email=email,
    #         subject=subject,
    #         message=message
    #     )
    #     contact_user.save()
    #     return render(request, 'index.html')



def sendmail(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        msg = 'Sizga shaxsiy saytingizdan ' + full_name + ' xabar yubordi. ' + '\n' + ' xabar mavzusi: ' + subject + '\n' + 'elektron pochtasi: ' + email + '\n' + 'xabar mazmuni: ' + '\n' + message
        send_mail(
            'Yangi xabar',
            msg,
            settings.EMAIL_HOST_USER,
            ['sardorbek.uktamov.1@mail.ru'],
            fail_silently=False,
        )

        contact_user = Contact(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )
        contact_user.save()
        return render(request, 'sendmail.html')
    else:
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
