from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from media_app.models import Image, Document
from random import randint

class ResourceCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name (NL)"))
    name_en = models.CharField(max_length=255, verbose_name=_("Name (EN)"))
    name_fr = models.CharField(max_length=255, verbose_name=_("Name (FR)"))
    def __unicode__(self):
        return self.name

class Resource(models.Model):
    published = models.BooleanField(_("Published"), default=False)
    title = models.CharField(max_length=255, verbose_name=_("Title (NL)"))
    title_en = models.CharField(max_length=255, verbose_name=_("Title (EN)"), blank=True)
    title_fr = models.CharField(max_length=255, verbose_name=_("Title (FR)"), blank=True)
    category = models.ForeignKey(ResourceCategory, verbose_name=_("Category"))
    summary = models.TextField(_("Summary (NL)"), blank=True)
    summary_en = models.TextField(_("Summary (EN)"), blank=True)
    summary_fr = models.TextField(_("Summary (FR)"), blank=True)
    link = models.URLField(_("Link URL"))
    image_set = generic.GenericRelation(Image)
    documents = generic.GenericRelation(Document)
    #preview = models.ImageField(upload_to="")

    def __unicode__(self):
        return self.title

    def size_x(self):
        return randint(8, 12)

    class Meta:
        ordering = ["-id"]
