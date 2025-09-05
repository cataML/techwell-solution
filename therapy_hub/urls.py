from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', contact_view, {"template_name": "therapy_hub/index.html"}, name='index'),
    path('about/', contact_view, {"template_name": "therapy_hub/about.html"}, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', contact_view, {"template_name": "therapy_hub/contact.html"}, name='contact'),
    path('booking/', views.booking, name='booking'),
]