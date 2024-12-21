from django.contrib import admin
from .models import Station

# Register your models here.

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'media_directory', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

