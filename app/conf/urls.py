from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
	url(r'^$', RedirectView.as_view(url='/main/',permanent=True), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^guardian/', include('guardian.urls', namespace='guardian')),
]
