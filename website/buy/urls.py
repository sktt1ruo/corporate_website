from django.conf.urls import url, include
from buy import views

app_name = 'buy'

urlpatterns = [
    url(r"^distributors/$", views.distributors, name='distributors'),
    url(r"^terms_of_service/$", views.terms_of_service, name='terms_of_service'),
]
