from django.conf.urls import url, include

from . import views

urlpatterns = [
url(r'write_para$', views.write_para, ),
url(r'get_cache_by_id$', views.get_cache_by_id, ),
url(r'show_books$', views.show_books, ),
url(r'get_recent_time$', views.get_recent_time, ),
]
