from django.urls import path
from .views import contactme

urlpatterns = [
    path('', contactme, name="contactme")
    ]