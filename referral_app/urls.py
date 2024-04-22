from django.contrib import admin
from django.urls import path

from referral_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('<int:pk>/show/', views.ProfileAPIView.as_view(), name='users_show'),
    path('', views.ProfileFormCreateView.as_view(), name='index'),
]
