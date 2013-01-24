from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Event
from wymeditor.admin import RichTextAdmin

class EventAdmin(RichTextAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Event, EventAdmin)

