from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView, ListView, list_detail
from django.views.generic.simple import redirect_to
from projects.models import Project
from resources.models import Resource
from flatpages.models import FlatPage
from axis.models import Axis

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bessst.views.home', name='home'),
    # url(r'^bessst/', include('bessst.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^$', TemplateView.as_view(template_name="home.html")),
    (r'^$', redirect_to, {'url': '/projects/'}),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/$', list_detail.object_list, {"queryset":Project.objects.all(), "extra_context": {"axis_list" : Axis.objects.all()}}),
    url(r'^projects/(?P<slug>[\w-]+)/$', DetailView.as_view(model=Project), name='project-detail'),
    url(r'^inspiratie/$', list_detail.object_list, {"queryset":Resource.objects.all()}),
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(model=FlatPage), name='flatpage-detail'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
