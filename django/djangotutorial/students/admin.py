from django.contrib import admin

from .models import Student

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "std_number", "age", "is_married")
    search_fields = ("name", "phone", "std_number")
    list_filter = ("is_married", "age")
    list_per_page = 18
