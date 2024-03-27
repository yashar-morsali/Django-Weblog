from django.urls import path
from . import views
from Weblog import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index , name='index')
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
