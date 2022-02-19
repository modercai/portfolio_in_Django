from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        if request.method == "POST":
            name = request.POST['name']
            message_email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']

            send_mail(
                subject,
                message,
                message_email,
                ['malatefriday12@gmail.com'],
                fail_silently=False
            )
        return render(request, 'contact.html', {'name': name})
    return render(request, 'contact.html', {'form': form})


def about_us(request):
    return render(request, 'about-us.html', {})


def services(request):
    return render(request, 'services.html', {})


def portfolio(request):
    return render(request, 'portfolio.html', {})
