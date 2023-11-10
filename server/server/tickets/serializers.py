from rest_framework import serializers
from .models import Tickets, Amenities, AmenitiesTickets, CabinTypes, AmenitiesCabinType
from flight.serializers import SchedulesListSerializer
class TicketsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(TicketsSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Tickets
        fields = (
            "id",
            "user",
            "schedule",
            "cabin_type",
            "first_name",
            "last_name",
            "phone",
            "passport_number",
            "passport_country",
            "booking_reference",
            "confirmed",
        )

class CabinTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CabinTypes
        fields = '__all__'
class TicketsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = (
            "id",
            "user",
            "schedule",
            "cabin_type",
            "first_name",
            "last_name",
            "phone",
            "passport_number",
            "passport_country",
            "booking_reference",
            "confirmed",
        )
    
    schedule = SchedulesListSerializer()
    cabin_type = CabinTypesSerializer()

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = (
            'id',
            'service',
            'price',
        )

class AmenitiesTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenitiesTickets
        fields= '__all__'

class AmenitiesCabinTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenitiesCabinType
        fields= '__all__'