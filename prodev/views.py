from django.shortcuts import render

# Create your views here.
def indexx(request):
    return render(request, 'prodev/indexx.html')