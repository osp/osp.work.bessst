from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from media_app.models import Image, Document

class FlatPage(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this page."))
    content = models.TextField(_("Content"))
    infobox = models.TextField(_("Info Box"), help_text=_("Content which appears in the small box on the right side of the website."), blank=True)
    image_set = generic.GenericRelation(Image)
    documents = generic.GenericRelation(Document)

    def __unicode__(self):
        return self.title
    @models.permalink
    def get_absolute_url(self):
        return ('flatpage-detail', (), {'slug': str(self.slug)})
