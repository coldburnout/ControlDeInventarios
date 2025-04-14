from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='dashboard-index'),
    path('personal/',views.personal, name='dashboard-personal'),
    path('productos/',views.productos, name='dashboard-productos'),
    path('ordenes/',views.ordenes, name='dashboard-ordenes'),
]