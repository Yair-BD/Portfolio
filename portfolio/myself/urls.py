
from django.urls import path
from .views import *

urlpatterns = [
    path('', myself, name="my_self"),
]
