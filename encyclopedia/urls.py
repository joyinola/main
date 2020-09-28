from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name='search'),
    path('new', views.create, name='new'),
    path('random',views.randm, name='random'),
    path('edit/<str:data>', views.edit, name='edit'),
    path("<str:entry>", views.view, name="view")
]
