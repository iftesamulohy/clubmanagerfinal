from django.contrib import admin

from club.models import Club, HomeSlider,Image,Event,Registrations,Slider
from solo.admin import SingletonModelAdmin

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name']
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Registrations)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['user']
@admin.register(HomeSlider)
class HomeSliderAdmin(SingletonModelAdmin):
    list_display = ['name']