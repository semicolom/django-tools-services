from django.urls import path

from . import views

app_name = 'services'
urlpatterns = [
    path('', views.ServicesView.as_view(), name='list'),
    path('<slug:slug>/', views.ServiceDetailView.as_view(), name='detail'),
]
