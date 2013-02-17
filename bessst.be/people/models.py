from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

class People(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    prefix = models.CharField(max_length=255, verbose_name=_("Prefix"), null=True, blank=True)
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this event."))
    #country = 
    address = models.CharField(max_length=100, verbose_name=_("Address"), null=True, blank=True)
    city = models.CharField(max_length=80, verbose_name=_("Postal code + City"), null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name=_("Phone number"), null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name=_("Email"), null=True, blank=True)
    link = models.URLField(_("Link URL"), null=True, blank=True)
    biography = models.TextField(_("Short biography"), blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_full_name(self):
        try:
            return self.individual.get_full_name()
        except:
            return self.__unicode__()

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.get_full_name())
        super(People, self).save(*args, **kwargs)

class Individual(People):
    firstname = models.CharField(max_length=255, verbose_name=_("First Name"), null=True, blank=True)

    def get_full_name(self):
        fullname = ""
        if self.firstname: fullname += self.firstname + u' '
        if self.prefix: fullname += self.prefix + u' '
        if self.name: fullname += self.name
        return fullname

    def __unicode__(self):
        return self.get_full_name()

class Organization(People):
    contact_person = models.ForeignKey(Individual, verbose_name=_("Contact Person"), related_name="contact_person", null=True, blank=True)
    individuals = models.ManyToManyField(Individual, verbose_name=_("Individuals"), related_name="individual_set", blank=True)
    def __unicode__(self):
        return self.name


class Friend(Individual):
    location_latitude = models.FloatField(verbose_name=_("Latitude of my Silence Location"))
    location_longitude = models.FloatField(verbose_name=_("Longitude of my Silence Location"))
    location_explanation = models.TextField(_("Explanation of my Silence Location"))
    newsletter = models.BooleanField(verbose_name=_("Receive Newsletter"))
    display = models.BooleanField(verbose_name=_("Display my name"), default=True)
        
    def __unicode__(self):
        return self.get_full_name()
