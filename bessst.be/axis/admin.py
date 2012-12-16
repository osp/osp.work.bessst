from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Axis
from media_app.admin import ImageInline

class AxisAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)

admin.site.register(Axis, AxisAdmin)

