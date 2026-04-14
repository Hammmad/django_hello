from .models import Reservation

def create_reservation(validated_data):
    first_name = validated_data.get('first_name')
    reservation_time = validated_data.get('reservation_time')

    if Reservation.objects.filter(first_name=first_name, reservation_time=reservation_time).exists():
        raise Exception("Slot already booked")
    
    return Reservation.objects.create(**validated_data)