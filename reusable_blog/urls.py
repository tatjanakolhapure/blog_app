from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.post_link),
    url(r'^(?P<id>\d+)$',views.post_detail),
    url(r'^top/$',views.top_views),
    url(r'^top/(?P<id>\d+)$',views.post_detail),
    url(r'^new/$', views.new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post, name='edit'),
    url(r'^(?P<tag>[a-z]{4,})$', views.related_posts),
]

