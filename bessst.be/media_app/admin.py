from django.contrib.contenttypes import generic
from models import Image

class ImageInline(generic.GenericTabularInline):
    model = Image
    extra = 0

