from django.conf.urls import patterns, url
from gezimeclise.profiles.views import ProfileListView, ProfileDetailView

urlpatterns = patterns('',
                       url(r'^$', ProfileListView.as_view(),
                           name="profile_list"),
                       url(r'^(?P<username>[-\w]+)/$', ProfileDetailView.as_view(),
                           name="profile_detail"),
                       )
