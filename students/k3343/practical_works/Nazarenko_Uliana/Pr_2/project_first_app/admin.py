from django.contrib import admin
from .models import Owner, Car, Ownership, Drivers_license

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(Drivers_license)
