from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Project
from media_app.admin import ImageInline
from wymeditor.admin import RichTextAdmin

class ProjectAdmin(RichTextAdmin):
    prepopulated_fields = {'slug': ('title', 'subtitle')}
    inlines = (ImageInline,)
    filter_horizontal = ('producers',)
    list_display = ('__unicode__', 'subtitle', 'published', 'archived', 'axis', 'start_date', 'end_date', 'location', 'link')
    list_filter = ('archived', 'axis', 'location', 'start_date', 'published')
    fieldsets = (
        (_('General'), {
            'fields': (('published', 'archived'),('title', 'title_en', 'title_fr'), ('subtitle', 'subtitle_en', 'subtitle_fr'), 'slug')
        }),
        (_('Infos'), {
            'fields': ('axis', 'link', ('start_date','end_date'), ('location', 'location_en', 'location_fr'), 'producers')
        }),
        (_('Summary'), {
            'fields': ('summary', 'summary_en', 'summary_fr')
        }),
        (_('Description'), {
            'fields': ('description', 'description_en', 'description_fr')
        })
    )

admin.site.register(Project, ProjectAdmin)

