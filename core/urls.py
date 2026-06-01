from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course/', views.course, name='course'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('retreat/', views.retreat_list, name='retreat'),
    path('retreat/<int:pk>/', views.retreat_detail, name='retreat_detail'),
    path('contact/', views.contact, name='contact'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
    path('chakra/<int:pk>/', views.chakra_detail, name='chakra_detail'),
    path('submit/', views.submit_lead, name='submit_lead'),
    path('reviews/', views.reviews, name='reviews'),
    path('lang/<str:lang>/', views.set_language, name='set_language'),
]
