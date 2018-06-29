from rest_framework import serializers

from .models import Campaigns


class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = '__all__'
