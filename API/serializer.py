from rest_framework import serializers

from .models import Temperature
# from .models import locations


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'

# class locationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = locations
#         fields = '__all__'

