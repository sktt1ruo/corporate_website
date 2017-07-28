from django.shortcuts import render


# Create your views here.
def distributors(request):
    return render(request, 'buy/distributors.html')


def terms_of_service(request):
    return render(request, 'buy/terms_of_service.html')
