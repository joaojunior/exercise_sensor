from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from sensor_parser.parser import parser_sensor2dict

from api.forms import SensorRecordForm


class ApiResource(DjangoResource):
    preparer = FieldsPreparer(fields={
            'id': 'id',
            'device_id': 'device_id',
        })

    def is_authenticated(self):
        """
        It is not a good idea return True always here. But, I'm writing
        I simple exercise and I don't like to add authenticated here!
        """
        return True

    def create(self):
        record = self.data['record']
        record = parser_sensor2dict(record)
        form = SensorRecordForm(record)
        record = form.save()
        return record