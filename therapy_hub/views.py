from django.shortcuts import render, redirect
from .forms import ContactForm, BookingForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'therapy_hub/index.html')

def about(request):
    return render(request, 'therapy_hub/about.html')

def services(request):
    return render(request, 'therapy_hub/services.html')

def contact(request):
    return render(request, 'therapy_hub/contact.html')

def contact_view(request, template_name="therapy_hub/contact.html"):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully! ✅")
            return redirect('contact')  

    else:
        form = ContactForm()
    return render(request, template_name, {'form': form})

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking was successful! ✅")
            return redirect('booking')
    else:
        form = BookingForm()
    return render(request, 'therapy_hub/booking.html', {'form': form})

