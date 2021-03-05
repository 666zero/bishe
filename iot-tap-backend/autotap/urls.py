

from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('fix/', views.fix, name='fix'),
    path('reproduce/', views.reproduce, name='reproduce'),
    path('synthesize/', views.synthesize, name='synthesize'),
    path('multisp/', views.multisp, name='multisp'),
    path('debug/', views.debug, name='debug')
]
