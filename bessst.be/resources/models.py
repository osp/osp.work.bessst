from django.db import models
from django.utils.translation import ugettext_lazy as _

class Resource(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    summary = models.TextField(_("Summary"))
    link = models.URLField(_("Link URL"))
    #preview = models.ImageField(upload_to="")

