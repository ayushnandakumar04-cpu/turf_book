"""
URL configuration for turf_book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from turf_crud.views import TurfListCreateView,TurfListRetrieveView
from turf_crud_v2 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('turf/',TurfListCreateView.as_view()),
    path('turf/<int:pk>/',TurfListRetrieveView.as_view()),
    path('v2/turf/',views.TurfListCreateView.as_view()),
    path('v2/turf/<int:pk>/',views.TurfRetrieveUpdateDeleteView.as_view()),
     path('v2/admin/register/',views.AdminRegister.as_view()),
]
