from django.shortcuts import render, redirect
from .forms import ContactUsForm

# Create your views here.
def contact_view(request):
    if 'therapy' in request.META.get('HTTP_REFERER', ''):
        base_template = 'base_therapy.html'
    else:
        base_template = 'base_prodev.html'
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)  

    else:
        form = ContactUsForm()
    return render(request, 'contact/contact.html', {
        'form': form,
        'base_template': base_template
    })

