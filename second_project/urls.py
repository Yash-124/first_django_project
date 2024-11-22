
from django.contrib import admin
from django.urls import path, include
from second_app import views
from django.conf import settings # new
from  django.conf.urls.static import static #new

urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('second_app.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)