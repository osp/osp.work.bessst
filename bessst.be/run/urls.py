from datetime import date

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView, ListView, list_detail
from django.views.generic.simple import redirect_to
from projects.models import Project
from events.models import Event
from resources.models import Resource
from flatpages.models import FlatPage
from axis.models import Axis

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bessst.views.home', name='home'),
    # url(r'^bessst/', include('bessst.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += i18n_patterns('',
    url(r'^$', list_detail.object_list, {"queryset":Axis.objects.all(), 'template_name':'home.html'}, name='home'),
    url(r'^projects/$', 'projects.views.projects', name='projects'),
    url(r'^projects/(?P<slug>[\w-]+)/$', DetailView.as_view(model=Project), name='project-detail'),
    url(r'^axis/(?P<slug>[\w-]+)/$', 'projects.views.projects', name='axis-detail'),
    
    url(r'^agenda/$', list_detail.object_list, {"queryset":Event.objects.filter(published=True, end_date__gt=date.today()),}, name='agenda'),
    url(r'^agenda/archive/$', list_detail.object_list, {"queryset":Event.objects.filter(published=True, start_date__lt=date.today()), 'extra_context': {'archive': True}}, name='agenda-archive'),
    url(r'^agenda/(?P<slug>[\w-]+)/$', DetailView.as_view(model=Event), name='event-detail'),
    
    url(r'^inspiration/$', list_detail.object_list, {"queryset":Resource.objects.filter(published=True)}, name='inspiration'),
    url(r'^community/$', 'people.views.community', name='community'),
    url(r'^atlas/$', 'people.views.atlas', name='atlas'),
    url(r'^atlas/(?P<id>[0-9]+)/$', 'people.views.atlas', name='atlas'),
    url(r'^e-mail/$', 'people.views.e_mail_list', name='e_mail_list'),
    
    url(r'^label-form/$', 'people.views.label_form', name='label_form'),
    
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(model=FlatPage), name='flatpage-detail'),
)

# Serve asset files in DEBUG:
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
