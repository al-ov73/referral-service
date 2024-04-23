from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin

from referral_app.api.permissions import IsOwnerOrReadOnly
from referral_app.api.serializers import ProfileSerializer
from referral_app.models import Profile


# class UserView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (IsOwnerOrReadOnly, )
