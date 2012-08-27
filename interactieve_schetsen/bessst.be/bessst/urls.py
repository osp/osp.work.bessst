try:
    from django.conf.urls import patterns, include, url
except ImportError: # Django 1.3
    from django.conf.urls.defaults import patterns, include, url
    
from django.views.generic import TemplateView

from django.contrib import admin
from bessst import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bessst.views.home', name='home'),
    # url(r'^bessst/', include('bessst.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
