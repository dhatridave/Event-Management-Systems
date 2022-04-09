from django.urls import path

from myapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('pages_register/',views.pages_register,name='pages_register'),
    path('pages_login/',views.pages_login,name='pages_login'),
    path('users_profile/',views.users_profile,name='users_profile'),
    path('otp/',views.otp,name='otp'),
    path('logout/',views.logout,name='logout'),




]
