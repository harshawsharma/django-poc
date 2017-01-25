from django.conf.urls import url, include
from posts import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name="post_list"),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail_post'),
    url(r'^create/$', views.PostCreateView.as_view(), name='create_post'),
    url(r'^delete/$', views.PostDeleteView.as_view(), name='delete_post'),
]
