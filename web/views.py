from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        if request.method == "POST":
            name = request.POST.get('name')
            message_email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            data = {
                'name': name,
                'email': message_email,
                'subject': subject,
                'message': message,
            }
            message = '''
            New message: {}

            From:{}
            '''.format(data['message'], data['email'])

            send_mail(
                data['subject'],
                message,
                '',
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
