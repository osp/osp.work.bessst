from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import FlatPage
from media_app.admin import ImageInline
from wymeditor.admin import RichTextAdmin

class FlatPageAdmin(RichTextAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = (ImageInline,)

admin.site.register(FlatPage, FlatPageAdmin)

