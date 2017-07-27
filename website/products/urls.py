from django.conf.urls import url
from products import views

app_name = 'products'

urlpatterns = [
    url(r"^imu$", views.imu, name='imu'),
    url(r'^imu/(\d+)/$', views.imu_product, name='imu_product'),
    url(r"^emg_mmg$", views.emg_mmg, name='emg_mmg'),
    url(r'^emg_mmg/(\d+)/$', views.emg_mmg_product, name='emg_mmg_product'),
]
