from rest_framework import serializers

from .models import Campaigns
from .models import locations


class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = '__all__'

        
class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = locations
        fields = '__all__'

