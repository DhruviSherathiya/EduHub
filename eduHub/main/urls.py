from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('signIn',views.signIn,name='signIn'),
    path('loginAction',views.loginAction,name='loginAction'),
    path('home',views.home,name='home'),
    path('subject/<str:sname>',views.subject,name='subject')
]