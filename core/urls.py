from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('feature/', views.feature, name='feature'),
    path('mycv/', views.mycv, name='mycv'),
    path('project/', views.project, name='project'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.error_404, name='error_404'),
]