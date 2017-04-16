from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'add_sensor_record/', include(views.ApiResource.urls())),
    url(r'number_events_by_cluster/', views.NumberEvents.as_detail()),
    url(r'average_power_active_by_cluster/', views.PowerActive.as_detail()),
]
