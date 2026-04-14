from rest_framework import serializers
from .models import Reservation
from .services import *

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def create(self, validated_data):
        return create_reservation(validated_data)
