from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.log_out, name='log_out'),
    path('order/payment', views.payment, name='payment'),
    path('movies', views.movies, name='movies'),
    path('events', views.events, name='events'),
    path('sports', views.sports, name='sports'),
    path('activities', views.activities, name='activities'),
    path('profilePage', views.profilePage, name='profilePage'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('contactUs', views.contactUs, name='contactUs'),
]
