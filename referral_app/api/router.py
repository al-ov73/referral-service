from django.urls import path
from rest_framework.routers import DefaultRouter

from referral_app.api.views import UserView

router = DefaultRouter(trailing_slash=True)

urlpatterns = router.urls

urlpatterns.extend([
    path('users/<int:pk>', UserView.as_view()),
])
