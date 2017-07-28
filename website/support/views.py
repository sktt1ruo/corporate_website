from django.shortcuts import render


# Create your views here.
def downloads(request):
    return render(request, 'support/downloads.html')
