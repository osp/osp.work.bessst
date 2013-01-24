from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Individual, Organization, People
from wymeditor.admin import RichTextAdmin

class IndividualAdmin(RichTextAdmin):
    prepopulated_fields = {'slug': ('firstname', 'prefix', 'name')}

class OrganizationAdmin(RichTextAdmin):
    prepopulated_fields = {'slug': ('prefix', 'name')}

admin.site.register(Individual, IndividualAdmin)
admin.site.register(Organization, OrganizationAdmin)

