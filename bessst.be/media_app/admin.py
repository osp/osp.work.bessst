from django.contrib.contenttypes import generic
from models import Image, Document
from django.contrib import admin

class ImageInline(generic.GenericTabularInline):
    model = Image
    extra = 0

class DocumentInline(generic.GenericTabularInline):
    model = Document
    extra = 0

