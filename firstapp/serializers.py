from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self,data):
        name = data.get('first_name')
        time = data.get('reservation_time')

        qs = Reservation.objects.filter(first_name=name, reservation_time=time)
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        
        if qs.exists():
            raise serializers.ValidationError('This record already exist')
        
        return data

