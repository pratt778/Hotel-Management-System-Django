from django.urls import path
from . import views
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.log,name='login'),
    path('logout',views.out,name='logout'),
    path('',views.home,name='home'),
    path('hotel/<uid>',views.hoteldetail,name="hotel_detail")
]
