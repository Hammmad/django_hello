from .models import Reservation

def create_reservation(validated_data):
    name = validated_data.get('first_name')
    time = validated_data.get('reservation_time')

    if Reservation.objects.filter(first_name=name, time=time).exists():
        raise Exception("Slot already booked")
    
    return Reservation.objects.create(**validated_data)