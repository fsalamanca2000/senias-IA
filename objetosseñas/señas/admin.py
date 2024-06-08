from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Señas

class SignAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(Señas, SignAdmin)