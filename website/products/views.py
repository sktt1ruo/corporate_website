from django.shortcuts import render


# Create your views here.
def imu(request):
    return render(request, 'products/imu/imu.html')


def imu_product(request, id):
    page = 'products/imu/' + id + '.html'
    return render(request, page)

def emg_mmg(request):
    return render(request, 'products/emg_mmg/emg_mmg.html')

def emg_mmg_product(request, id):
    page = 'products/emg_mmg/' + id + '.html'
    return render(request, page)
