from django.urls import path
from re_domain import views


urlpatterns = [
    path('<str:s>', views.index)
]
