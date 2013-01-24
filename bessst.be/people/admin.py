from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Individual, Organization, People
from wymeditor.admin import RichTextAdmin

class IndividualAdmin(RichTextAdmin):
    prepopulated_fields = {'slug': ('firstname', 'prefix', 'name')}
    fieldsets = (
        (_('General'), {
            'fields': (('name', 'prefix', 'firstname'), 'slug')
        }),
        (_('Coordinates'), {
            'fields': (('address', 'city'), 'phone', 'email', 'link')
        }),
        (_('More'), {
            'fields': ('biography',)
        })
    )

class OrganizationAdmin(RichTextAdmin):
    prepopulated_fields = {'slug': ('prefix', 'name')}
    fieldsets = (
        (_('General'), {
            'fields': (('name', 'prefix'), 'slug')
        }),
        (_('Coordinates'), {
            'fields': ('contact_person', ('address', 'city'), 'phone', 'email', 'link')
        }),
        (_('More'), {
            'fields': ('biography',)
        })
    )

admin.site.register(Individual, IndividualAdmin)
admin.site.register(Organization, OrganizationAdmin)

