from django.contrib import admin
from app.models import Todo, Contact, ContactUs

# Register your models here.


@admin.register(Todo)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'desc', 'date_created']
    list_filter = ('user',)

# @admin.register(Contact)
# class ContactModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'phone', 'desc', 'datetime']
#     list_filter = ('user',)

# admin.site.register(ContactUs)

@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email', 'mobile_number', 'hobbies', 'messege', 'date_time']
    list_filter = ('user',)
