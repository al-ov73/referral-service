from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from psycopg2.errors import UniqueViolation
from django.core.exceptions import ObjectDoesNotExist

from referral_app.api.permissions import IsOwnerOrReadOnly
from referral_app.api.serializers import ProfileSerializer
from referral_app.models import Profile


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (IsOwnerOrReadOnly, )

class ReferralSend(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        received_ref_code = request.data.get('ref')
        send_from_id = kwargs.get('pk')
        send_to = None
        try:
            send_to = Profile.objects.get(ref_code=received_ref_code)
            send_from = Profile.objects.get(id=send_from_id)
            send_to.ref_received.add(send_from)
            send_from.ref_active = False
            send_from.save()
            send_to.save()
        except ObjectDoesNotExist:
            return Response('User not found')

        return Response('Success')        
