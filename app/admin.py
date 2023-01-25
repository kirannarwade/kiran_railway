from django.contrib import admin
from .models import Todo, Contact

# Register your models here.


# admin.site.register(Todo)       <----- Normal Way


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'date_time']    # <-- Advance Way

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'messege']    # <-- Advance Way