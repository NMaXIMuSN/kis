from django.contrib import admin
from tickets.models import CabinTypes, Tickets, Amenities, AmenitiesCabinType, AmenitiesTickets
# Register your models here.
@admin.register(Tickets)
class OfficeAdmin(admin.ModelAdmin):
    pass


@admin.register(CabinTypes)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(Amenities)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(AmenitiesCabinType)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(AmenitiesTickets)
class RoleAdmin(admin.ModelAdmin):
    pass
