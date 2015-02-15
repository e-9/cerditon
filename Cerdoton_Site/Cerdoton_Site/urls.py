from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Cerdoton_Site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cerdoton/', include('cerdoton_app.urls', namespace="cerdoton")),
    url(r'^admin/', include(admin.site.urls)),
)
