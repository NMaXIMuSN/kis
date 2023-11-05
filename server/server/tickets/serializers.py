from rest_framework import serializers
from .models import Tickets
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