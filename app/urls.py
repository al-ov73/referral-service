from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('<int:pk>/show/', views.ProfileShowView.as_view(), name='users_show'),
    path('', views.ProfileFormCreateView.as_view(), name='index'),
]
