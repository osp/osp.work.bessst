from django.db import models
from django.utils.translation import ugettext_lazy as _
from axis.models import Axis
from people.models import People
from django.contrib.contenttypes import generic
from media_app.models import Image

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this event."))
    authors = models.ManyToManyField(People, verbose_name=_("Authors"), related_name="author_set")
    producers = models.ManyToManyField(People, verbose_name=_("Producers"), related_name="producer_set")
    location = models.CharField(max_length=80, verbose_name=_("Location"), null=True)
    axis = models.ForeignKey(Axis, verbose_name=_("Axis"))
    summary = models.TextField(_("Summary"))
    description = models.TextField(_("Description"))
    image_set = generic.GenericRelation(Image)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('project-detail', (), {'slug': str(self.slug)})
