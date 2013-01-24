from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Project
from media_app.admin import ImageInline
from wymeditor.admin import RichTextAdmin

class ProjectAdmin(RichTextAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = (ImageInline,)
    filter_horizontal = ('producers',)

admin.site.register(Project, ProjectAdmin)

