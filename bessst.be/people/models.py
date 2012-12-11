from django.db import models
from django.utils.translation import ugettext_lazy as _

class People(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    prefix = models.CharField(max_length=255, verbose_name=_("Prefix"), null=True, blank=True)
    firstname = models.CharField(max_length=255, verbose_name=_("First Name"), null=True, blank=True)
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this event."))
    #country = 
    city = models.CharField(max_length=80, verbose_name=_("City"))
    link = models.URLField(_("Link URL"))
    biography = models.TextField(_("Short biography"), blank=True)

    def __unicode__(self):
        return self.name
