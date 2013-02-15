from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Project
from media_app.admin import ImageInline
from wymeditor.admin import RichTextAdmin

class ProjectAdmin(RichTextAdmin):
    prepopulated_fields = {'slug': ('title', 'subtitle')}
    inlines = (ImageInline,)
    filter_horizontal = ('producers',)
    list_display = ('__unicode__', 'subtitle', 'axis', 'location', 'link')
    list_filter = ('axis', 'location')
    fieldsets = (
        (_('General'), {
            'fields': (('published', 'archived'),'title', 'subtitle', 'slug')
        }),
        (_('Infos'), {
            'fields': ('axis', 'link', ('start_date','end_date'), 'location', 'producers', 'summary', 'description')
        })
    )

admin.site.register(Project, ProjectAdmin)

