from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def indexx(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent!")
            return redirect('prodev:indexx')  # refresh to clear form after submit
    else:
        form = ContactUsForm()

    return render(request, 'prodev/indexx.html', {'form': form})

def prodev_contact(request):
    return render(request, 'contact/contact.html', {
        'base_template': 'base_prodev.html'
    })

