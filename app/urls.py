from django.urls import path
from .views import contactme, sendmail

urlpatterns = [
    path('', contactme, name="contactme"),
    path('sendmail/', sendmail, name="sendmail"),
    ]