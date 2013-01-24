from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Axis
from media_app.admin import ImageInline
from wymeditor.admin import RichTextAdmin

class AxisAdmin(RichTextAdmin):
    inlines = (ImageInline,)

admin.site.register(Axis, AxisAdmin)

