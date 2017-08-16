from django.conf.urls import url
from products import views

app_name = 'products'

urlpatterns = [
    url(r"^imu/$", views.imu, name='imu'),
    url(r'^imu/(\d+)/$', views.imu_product, name='imu_product'),
    url(r"^vimu/$", views.vimu, name='vimu'),
    url(r'^vimu/(\d+)/$', views.vimu_product, name='vimu_product'),
    url(r'^software/$', views.software, name='software'),
    url(r'^applications/$', views.applications, name='applications'),
]
