from django.conf.urls import patterns, include, url

urlpatterns = patterns('newsletter.views',
    url(r'^signup/$', 'signup'),
)
