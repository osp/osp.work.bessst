from django.db import models
from django.utils.translation import ugettext_lazy as _

class ResourceCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    def __unicode__(self):
        return self.name

class Resource(models.Model):
    published = models.BooleanField(_("Published"), default=False)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    axis = models.ForeignKey(ResourceCategory, verbose_name=_("Category"))
    summary = models.TextField(_("Summary"), blank=True)
    link = models.URLField(_("Link URL"))
    #preview = models.ImageField(upload_to="")

    def __unicode__(self):
        return self.title

