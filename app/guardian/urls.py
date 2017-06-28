from django.conf.urls import include, url, patterns

urlpatterns = patterns('guardian.views',

    url(r'^add_credentials/$','add_credentials', name='add_credentials'),
    url(r'^delete_credentials/(?P<pk>\d+)$','delete_credentials', name='delete_credentials'),
    url(r'^detail_credentials/(?P<pk>\d+)$','detail_credentials', name='detail_credentials'),
    url(r'^edit_credentials/(?P<pk>\d+)$','edit_credentials', name='edit_credentials'),
)