from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        message_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

    # sending emails
        send_mail(
            subject,
            message,
            message_email,
            ['friday@gmail.com'],
        )
        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})


def about_us(request):
    return render(request, 'about-us.html', {})


def services(request):
    return render(request, 'services.html', {})


def portfolio(request):
    return render(request, 'portfolio.html', {})
