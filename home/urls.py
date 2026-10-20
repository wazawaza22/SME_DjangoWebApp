from django.urls import path
from . import views   # 

urlpatterns = [
    path('', views.dynamic_form, name='home'),
]