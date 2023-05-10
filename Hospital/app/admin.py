from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Booking)
admin.site.register(Rooms)
admin.site.register(Patients_Chart)
admin.site.register(Appointment_Chart)
admin.site.register(Patient_Payment)

