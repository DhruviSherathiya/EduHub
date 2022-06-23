from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('signIn',views.signIn,name='signIn'),
    path('loginAction',views.loginAction,name='loginAction'),
    path('home',views.home,name='home'),
    path('subject/home',views.homepg,name='homepg'),
    path('subject/<str:sname>',views.subject,name='subject'),
    path('profile',views.profile,name='profile'),
    path('signout',views.signout,name='signout'),
    path('delete/<str:topic>', views.delete, name='delete'),
]