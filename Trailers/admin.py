from django.contrib import admin
from .models import Trailer
from django.utils.html import format_html
# Register your models here.

class TrailerAdmin(admin.ModelAdmin):
    display=[
        'img_preview',
        'MovieName',
        'playButton',
    ]
    list_display=display
    def img_preview(self,obj): #new
        return format_html('<img src = "{url}" style="width:30px !important"/>'.format(
             url = obj.Poster
         ))
    def playButton(self,obj):
        return format_html('<a href="{link}" class="btn btn-outline-success btn-sm">Play</a>'.format(link = obj.Link))
admin.site.register(Trailer,TrailerAdmin)