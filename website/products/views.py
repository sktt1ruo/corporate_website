from django.shortcuts import render


# Create your views here.
def imu(request):
    return render(request, 'products/imu/imu.html')


def imu_product(request, id):
    page = 'products/imu/' + id + '.html'
    return render(request, page)


def vimu(request):
    return render(request, 'products/vimu/vimu.html')


def vimu_product(request, id):
    page = 'products/vimu/' + id + '.html'
    return render(request, page)


def software(request):
    return render(request, 'products/software.html')


def applications(request):
    return render(request, 'products/applications.html')
