from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Event
from wymeditor.admin import RichTextAdmin

class EventAdmin(RichTextAdmin):
    list_display = ('title', 'published', 'start_date', 'end_date', 'project')
    list_filter = ('start_date', 'end_date', 'project')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (_('General'), {
            'fields': ('published','title', 'slug')
        }),
        (_('Infos'), {
            'fields': ('project', ('start_date', 'end_date'), 'summary', 'description')
        })
    )

admin.site.register(Event, EventAdmin)

