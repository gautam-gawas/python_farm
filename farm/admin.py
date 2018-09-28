from django.contrib import admin
from .forms import *
from .models import *

@admin.register(Farmer)
class AdminFarmer( admin.ModelAdmin):
	form = FarmerForm

@admin.register(Farm)
class AdminFarmer( admin.ModelAdmin):
	list_display = ('farmer','area','village','crop_grown','sowing_date')

@admin.register(Schedule)
class AdminSchedule( admin.ModelAdmin):
	list_display = ('farm','fertiliser','days_after_sowing','quantity_unit','quantity','price')