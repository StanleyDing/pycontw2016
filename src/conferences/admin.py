from django.contrib import admin

from .models import Conference


class ConferenceAdmin(admin.ModelAdmin):
    model = Conference
    fields = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}
