from django.db import models
from django.utils.translation import ugettext_lazy as _
from projects.models import Project
from axis.models import Axis

class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this event."))
    project = models.ForeignKey(Project, verbose_name=_("Related project"))
    #axis = models.ForeignKey(Axis, verbose_name=_("Axis")) # only if there's no related project
    start_date = models.DateField(_("Start date"))
    end_date = models.DateField(_("End date"))
    summary = models.TextField(_("Summary"))
    description = models.TextField(_("Description"))
