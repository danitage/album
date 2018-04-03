from django.urls import path, include
from album import views

urlpatterns = [
path('',views.first_view, name='hola'),
path('category/',views.category,name='category-list'),
path('category/detail/<int:category_id>/', views.category_detail, name='category-detail'),

path('photo/', views.PhotoListView.as_view(), name='photo-list'),
path('photo/detail/<int:pk>/', views.PhotoListView.as_view(), name='photo-detail'),

]
