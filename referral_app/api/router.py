from django.urls import path
from rest_framework.routers import DefaultRouter

from referral_app.api import views

router = DefaultRouter(trailing_slash=True)

urlpatterns = router.urls

urlpatterns.extend([
    path('api/v1/users/<int:pk>/send_ref', views.ReferralSend.as_view()),
    path('api/v1/users/<int:pk>', views.UserView.as_view()),
])
