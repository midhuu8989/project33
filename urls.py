from studentdetails import views
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
 path('home/', views.home, name='home'),
 path('dashboard/', views.dashboard, name='dashboard'),
 path('register/', views.register, name='register'),
 path('login/',LoginView.as_view(),name='login'),
 #path('studentlogin/',LoginView.as_view(), name='adminlogin'),
 path('logout/', LogoutView.as_view(next_page="login"), name='logout')

]
