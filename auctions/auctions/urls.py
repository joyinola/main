from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('listing', views.listin,name='product'),
    path('<int:item_no>',views.new_bid,name='new_bid'),
    path('item/<int:item_id>',views.item,name='item'),
    path('watchlist/<int:itm_id>', views.watchlist, name='watchlist'),
    path('r_watchlist/<int:itm_no>',views.r_watchlist,name='r_watchlist'),
    path('al_watchlist', views.al_watchlist, name='al_watchlistt'),
    path('close_bid/<int:list_no>', views.close_bid, name='close_bid'), 
    path('my_listing', views.my_listing,name='my_listing'),
    path('category/<int:categoryy>',views.categories,name='category')  
    ]
