from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=512)
    country = models.ForeignKey("amonic.Country", on_delete=models.CASCADE)
    iata_code = models.CharField(max_length=3)


class Route(models.Model):
    distance = models.IntegerField()
    flight_time = models.IntegerField(default=0)
    departure_airport = models.ForeignKey("flight.Airport", on_delete=models.CASCADE, related_name="departure")
    arrival_airport = models.ForeignKey("flight.Airport", on_delete=models.CASCADE, related_name="arrival")


class Aircraft(models.Model):
    name = models.CharField(max_length=256,)
    make_model = models.CharField(max_length=256)
    total_seats = models.SmallIntegerField()
    economy_seats = models.SmallIntegerField()
    business_seats = models.SmallIntegerField()


class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    aircraft = models.ForeignKey("flight.Aircraft", on_delete=models.CASCADE,)
    route = models.ForeignKey("flight.Route", on_delete=models.CASCADE,)
    flight_number = models.CharField(max_length=16)
    economy_price = models.IntegerField()
    confirmed = models.SmallIntegerField(default=False)

    @property
    def get_business_price(self):
        return self.economy_price * 1.35

    @property
    def get_first_class_price(self):
        return self.get_business_price * 1.30
