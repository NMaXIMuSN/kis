from django.db import models

# Create your models here.
class CabinTypes(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.name


class Tickets(models.Model):
    user = models.ForeignKey("amonic.User", on_delete=models.CASCADE)
    schedule = models.ForeignKey("flight.Schedule", on_delete=models.CASCADE)
    cabin_type = models.ForeignKey("tickets.CabinTypes", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=255)
    passport_country = models.ForeignKey("amonic.Country", on_delete=models.CASCADE)
    confirmed = models.SmallIntegerField(default=False)
    booking_reference = models.CharField(max_length=6)

    # def __str__(self):
    #     # return self.pk

class Amenities(models.Model):
    service = models.CharField(max_length=255)
    price = models.IntegerField()

class AmenitiesTickets(models.Model):
    amenity = models.ForeignKey("tickets.Amenities", on_delete=models.CASCADE)
    ticket = models.ForeignKey("tickets.Tickets", on_delete=models.CASCADE)
    price = models.IntegerField()

class AmenitiesCabinType(models.Model):
    amenities = models.ForeignKey("tickets.Amenities", on_delete=models.CASCADE)
    cabin_type = models.ForeignKey("tickets.CabinTypes", on_delete=models.CASCADE)
