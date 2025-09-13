from django.contrib import admin
from app.models import UserStatistic, OpenData

@admin.register(UserStatistic)
class UserStatisticAdmin(admin.ModelAdmin):
    list_display = ('user', 'region', 'field', 'soil_type', 'avarage_price', 'climate_class')

@admin.register(OpenData)
class OpenDataAdmin(admin.ModelAdmin):
    list_display = ('text',)