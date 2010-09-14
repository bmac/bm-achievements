from django.conf.urls.defaults import *


urlpatterns = patterns('',
       (r'^(?P<slug>.*?)/', 'achievements.views.achievement'),
       (r'^', 'achievements.views.achievements_all'),
)
