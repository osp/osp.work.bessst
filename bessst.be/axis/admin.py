from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Axis
from media_app.admin import ImageInline
from wymeditor.admin import RichTextAdmin
from orderable.admin import OrderableAdmin

class AxisAdmin(RichTextAdmin, OrderableAdmin):
    inlines = (ImageInline,)
    class Media:
        js = ('http://code.jquery.com/jquery-1.8.3.js',
              'http://code.jquery.com/ui/1.9.2/jquery-ui.js',)

admin.site.register(Axis, AxisAdmin)

