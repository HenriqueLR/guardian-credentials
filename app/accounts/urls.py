from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^sign_in/$','django.contrib.auth.views.login',{'template_name':'accounts/auth/login.html'},name='login'),
    url(r'^sign_out/$','django.contrib.auth.views.logout',{'next_page':'accounts:login'},name='logout'),
)