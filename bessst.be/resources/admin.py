from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Resource, ResourceCategory
from media_app.admin import ImageInline, DocumentInline
from wymeditor.admin import RichTextAdmin

class ResourceAdmin(RichTextAdmin):
    list_display = ('title', 'published', 'category', 'link')
    list_filter = ('published', 'category', 'link')
    inlines = (ImageInline, DocumentInline)
    fieldsets = (
        (_('General'), {
            'fields': ('published', ('title', 'title_en', 'title_fr'), 'category', 'link')
        }),
        (_('Summary'), {
            'fields': (('summary', 'summary_en', 'summary_fr'))
        })
    )

admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceCategory)

