from django.urls import path
from . import views

app_name = 'division'

urlpatterns = [
    # /blog/
    path('', views.homepage, name='homepage'),
    # /blog/create
    path('contactus/', views.simpanContactUs, name='simpan_contactus'),
    # /blog/create

]
