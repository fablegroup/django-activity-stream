import os
from django.contrib import admin
from django.views.static import serve
from django.urls import include, re_path


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': os.path.join(os.path.dirname(__file__), 'media')}),
    re_path(r'auth/', include('django.contrib.auth.urls')),
    re_path(r'testapp/', include('testapp.urls')),
    re_path(r'', include('actstream.urls')),
]
