from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about-us.html', views.about_us, name='about_us'),
    path('services.html', views.services, name='services'),
    path('portfolio.html', views.portfolio, name='portfolio'),
]
