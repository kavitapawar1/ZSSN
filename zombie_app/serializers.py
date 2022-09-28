from rest_framework import serializers
from .models import Survivor


class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ('id', 'name', 'age', 'gender', 'longitude', 'latitude', 'is_infected')
