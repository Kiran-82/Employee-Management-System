from django.contrib import admin
from .models import Employee, Admin

admin.site.register(Employee)
admin.site.register(Admin)