from .models import MySiteUser
from django.contrib import admin

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


admin.site.register(MySiteUser, UserAdmin)
