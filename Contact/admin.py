from django.contrib import admin
from django.urls import path 
import json
from django.http import JsonResponse
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=(
        'ClientName',
        'Email',
        'Message'
    )


admin.site.register(Contact,ContactAdmin)