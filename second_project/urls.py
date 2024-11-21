
from django.contrib import admin
from django.urls import path, include
from second_app import views

urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('second_app.urls')),
]
