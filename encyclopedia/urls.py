from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.rand, name="rand"),
    path("searchh", views.searchh, name='searchh')
]
