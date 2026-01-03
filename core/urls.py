from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('matches/', views.matches, name='matches'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('page/<slug:slug>/', views.page, name='page'),
]
