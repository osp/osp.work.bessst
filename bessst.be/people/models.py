from django.db import models
from django.utils.translation import ugettext_lazy as _

class People(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    prefix = models.CharField(max_length=255, verbose_name=_("Prefix"), null=True, blank=True)
    firstname = models.CharField(max_length=255, verbose_name=_("First Name"), null=True, blank=True)
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this event."))
    #country = 
    address = models.CharField(max_length=100, verbose_name=_("Address"))
    city = models.CharField(max_length=80, verbose_name=_("Postal code + City"))
    phone = models.CharField(max_length=20, verbose_name=_("Phone number"))
    email = models.EmailField(max_length=100, verbose_name=_("Email"))
    link = models.URLField(_("Link URL"))
    biography = models.TextField(_("Short biography"), blank=True)

    def __unicode__(self):
        return self.name
