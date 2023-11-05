from django.contrib import admin
from tickets.models import CabinTypes, Tickets
# Register your models here.
@admin.register(Tickets)
class OfficeAdmin(admin.ModelAdmin):
    pass


@admin.register(CabinTypes)
class RoleAdmin(admin.ModelAdmin):
    pass