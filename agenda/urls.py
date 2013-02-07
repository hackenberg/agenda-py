from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('agenda.views',
    url(r'^$', 'index'),
    url(r'^(?P<course_id>\d+)/$', 'detail'),
)
