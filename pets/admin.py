from django.contrib import admin
from .models import Pet, News


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'spec', 'age', 'breed', 'arrival_date')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(News)
class PetAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')