from django.contrib import admin

from flight.models import Aircraft, Airport, Route, Schedule 
# Register your models here.

@admin.register(Aircraft)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Airport)
class OfficeAdmin(admin.ModelAdmin):
    pass


@admin.register(Route)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class UserAdmin(admin.ModelAdmin):
    pass
