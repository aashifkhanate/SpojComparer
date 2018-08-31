from django.conf.urls import url
from compare.views import IndexView, ComparisonList, ComparisonListAPI
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', IndexView.as_view(), name = 'index'),
    url(r'^list/$', ComparisonList.as_view(), name = 'list'),
    url(r'^listAPI/$', ComparisonListAPI.as_view()),
]