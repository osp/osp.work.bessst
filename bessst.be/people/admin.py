from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import People

class PeopleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('firstname', 'prefix', 'name')}

admin.site.register(People, PeopleAdmin)

