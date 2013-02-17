from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Resource, ResourceCategory
from media_app.admin import ImageInline, DocumentInline
from wymeditor.admin import RichTextAdmin

class ResourceAdmin(RichTextAdmin):
    inlines = (ImageInline, DocumentInline)

admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceCategory)

