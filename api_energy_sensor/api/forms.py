from django.forms import ModelForm

from api.models import SensorRecord


class SensorRecordForm(ModelForm):
    class Meta:
        model = SensorRecord
        exclude = []
