from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from media_app.models import Image, Document

class FlatPage(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title (NL)"))
    title_en = models.CharField(max_length=255, verbose_name=_("Title (EN)"))
    title_fr = models.CharField(max_length=255, verbose_name=_("Title (FR)"))
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this page."))
    content = models.TextField(_("Content (NL)"))
    content_en = models.TextField(_("Content (EN)"), blank=True)
    content_fr = models.TextField(_("Content (FR)"), blank=True)
    infobox = models.TextField(_("Info Box (NL)"), help_text=_("Content which appears in the small box on the right side of the website."), blank=True)
    infobox_en = models.TextField(_("Info Box (EN)"), help_text=_("Content which appears in the small box on the right side of the website."), blank=True)
    infobox_fr = models.TextField(_("Info Box (FR)"), help_text=_("Content which appears in the small box on the right side of the website."), blank=True)
    image_set = generic.GenericRelation(Image)
    documents = generic.GenericRelation(Document)

    def __unicode__(self):
        return self.title
    @models.permalink
    def get_absolute_url(self):
        return ('flatpage-detail', (), {'slug': str(self.slug)})
