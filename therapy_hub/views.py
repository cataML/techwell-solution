from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm



# Create your views here.
def index(request):
    return render(request, 'therapy_hub/index.html')

def about(request):
    return render(request, 'therapy_hub/about.html')

def services(request):
    return render(request, 'therapy_hub/services.html')

def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(request, 'contact', {'name': form.cleaned_data['name']})
    else:
        form = ContactForm()
        return render(request, 'therapy_hub/contact.html', {'form': form})
