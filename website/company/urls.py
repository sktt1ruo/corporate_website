from django.conf.urls import url
from company import views

app_name = 'company'

urlpatterns = [
    url(r"^contact/$", views.contact, name='contact'),
]
