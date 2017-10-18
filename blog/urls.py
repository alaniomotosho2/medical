from django.conf.urls import url
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
# post views
 url(r'^$', views.post_list, name='post_list'),
#url(r'^$', views.PostListView.as_view(), name='post_list'),
url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$',views.post_detail,
name='post_detail'),
url(r'^(?P<post_id>\d+)/share/$', views.post_share,name='post_share'),
url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list,name='post_list_by_tag'),
url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
url(r'^latest_post/$', views.latest_post,name='latest_post'),
url(r'^about/$', views.about,name='about'),
url(r'^download/$', views.download,name='download'),
url(r'^query/$', views.query,name='query'),
]