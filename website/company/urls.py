from django.conf.urls import url
from company import views

app_name = 'company'

urlpatterns = [
    url(r"^about_us/$", views.about_us, name="about_us"),
    url(r"^customers/$", views.customers, name="customers"),
    url(r"^contact/$", views.contact, name='contact'),
]
