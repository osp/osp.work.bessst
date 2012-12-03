from django.db import models
from django.utils.translation import ugettext_lazy as _

class Axis(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    description = models.TextField(verbose_name=_("Description"))
    #pictogram = ImageField(upload_to="")
    #color = 
