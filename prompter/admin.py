from django.contrib import admin
from .models import Mode, Word


class ModeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'min_time_sec', 'max_time_sec')
    list_filter = ['name']


class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'importance', 'mode', 'use')
    list_filter = ['mode']


admin.site.register(Mode, ModeAdmin)
admin.site.register(Word, WordAdmin)
