from django.contrib import admin
from registrations.models import student_data, teacher_data
# Register your models here.
admin.site.register(student_data)
admin.site.register(teacher_data)
