from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Specialization)
admin.site.register(Organization)
admin.site.register(Degree)
admin.site.register(Doctor)
admin.site.register(Organization_Staff)
admin.site.register(Patient)
admin.site.register(Patient_History)