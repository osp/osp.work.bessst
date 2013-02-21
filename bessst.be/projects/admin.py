# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Project
from media_app.admin import ImageInline
from wymeditor.admin import RichTextAdmin
from orderable.admin import OrderableAdmin

class ProjectAdmin(RichTextAdmin, OrderableAdmin):
    model = Project
    prepopulated_fields = {'slug': ('title', 'subtitle')}
    inlines = (ImageInline,)
    filter_horizontal = ('producers',)
    # Couldn’t get this to work together with the orderable: 
    # list_display = ('__unicode__', 'subtitle', 'published', 'archived', 'axis', 'start_date', 'end_date', 'location', 'link', 'sort_order')
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
    class Media:
        js = ('http://code.jquery.com/jquery-1.8.3.js',
              'http://code.jquery.com/ui/1.9.2/jquery-ui.js',)

admin.site.register(Project, ProjectAdmin)

