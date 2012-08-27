try:
    from django.conf.urls import patterns, include, url
except ImportError: # Django 1.3
    from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('newsletter.views',
    url(r'^signup/$', 'signup'),
)
