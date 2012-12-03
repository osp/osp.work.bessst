from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Event

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Event, EventAdmin)

