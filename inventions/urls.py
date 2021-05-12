from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('list', views.list, name='list'),
    path('inventions/', views.InventionListView.as_view(), name='inventions'),
    path('inventions/categories/<str:category_name>/', views.InventionListView.as_view(), name='invention_category'),
    path('inventions/<int:pk>/', views.InventionDetailView.as_view(), name='invention_detail'),
]
