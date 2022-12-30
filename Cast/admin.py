from django.contrib import admin
from .models import Cast
# Register your models here.
class CastAdmin(admin.ModelAdmin):
    list_display=(
        'Name',
        'ActorId',
        'ActorMovie',
        'Role'
    )
admin.site.register(Cast,CastAdmin)