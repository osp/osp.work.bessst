from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Individual, Organization, People

class IndividualAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('firstname', 'prefix', 'name')}

class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('prefix', 'name')}

admin.site.register(People)
admin.site.register(Individual, IndividualAdmin)
admin.site.register(Organization, OrganizationAdmin)

