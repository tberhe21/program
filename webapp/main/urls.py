# this file defines URL patterns for the django application by mapping URLs to
# specific views defined in views.py for handling user requests

from django.urls import path, include
from . import views
from two_factor.urls import urlpatterns as tf_urls
from django.contrib.auth import views as auth_views
from .views import PatientCreateView, PatientUpdateView

urlpatterns = [

    path('', views.home, name='home'),
    path('', include(tf_urls)),
    path('home', views.home, name='home'),
    path('account/login/', auth_views.LoginView.as_view(), name='login'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('patients/', views.patients_list, name='patients_list'),
    path('patients/<int:pk>/',
         views.patient_detail, name='patient_detail'),
    path('search_patient/', views.search_patient, name='search_patient'),
    path('patients/add/', PatientCreateView.as_view(), name='add_patient'),
    path('patients/<int:pk>/edit/',
         PatientUpdateView.as_view(), name='edit_patient')

]
