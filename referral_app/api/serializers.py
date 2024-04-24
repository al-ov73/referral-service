from rest_framework import serializers
from referral_app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'phone',
            'ref_code',
            'ref_received',
            'ref_active'
        )
