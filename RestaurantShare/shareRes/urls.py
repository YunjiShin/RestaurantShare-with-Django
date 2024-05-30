"""
URL configuration for RestaurantShare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/delete',views.Delete_restaurant, name='resDelete'),
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name='resDetailPage'),
    path('restaurantDetail/updatePage/update',views.Update_restaurant, name='resUpdate'),
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name='resUpdatePage'),
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'),
    path('restaurantCreate/create',views.Create_restaurant, name='resCreate'),
    path('categoryCreate/', views.categoryCreate, name='cateCreatePage'),
    path('categoryCreate/create', views.Create_category, name='cateCreate'),
    path('categoryCreate/delete', views.Delete_category, name='cateDelete'),
]
