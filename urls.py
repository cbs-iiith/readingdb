
from django.conf.urls.defaults import *
urlpatterns = patterns('',
  ('^avail/(\d+)', 'powerdb.readingdb.views.availability'),
  ('^n/(?P<streamid>\d+)', 'powerdb.readingdb.views.npoints'),
  ('^n/', 'powerdb.readingdb.views.npoints'),
)