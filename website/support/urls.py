from django.conf.urls import url
from support import views

app_name = 'support'

urlpatterns = [
    url(r"^downloads/$", views.downloads, name='downloads'),
]
