from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'add_sensor_record/', include(views.ApiResource.urls())),
]
