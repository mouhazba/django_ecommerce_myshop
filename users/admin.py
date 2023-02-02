from django.contrib import admin

from .models import Managers


# Register your models here.
@admin.register(Managers)
class ManagersAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'password', ]
