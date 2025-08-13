from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'therapy_hub/index.html')

def about(request):
    return render(request, 'therapy_hub/about.html')

def services(request):
    return render(request, 'therapy_hub/services.html')


def therapy_contact(request):
    return render(request, 'contact/contact.html', {
        'base_template': 'base_therapy.html'
    })