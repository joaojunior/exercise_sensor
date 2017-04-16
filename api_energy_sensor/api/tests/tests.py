import os

from django.test import TestCase

import json


class TestApi(TestCase):
    def setUp(self):
        path = os.path.abspath(__file__)
        path = os.path.dirname(path)
        self.name_file_error = os.path.join(path,
                                            'test_data/sensor_data_error.txt')

    def test_send_post_empty(self):
        response = self.client.post('/api/add_sensor_record/',
                                    json.dumps({}),
                                    content_type='application/json')
        self.assertEqual(500, response.status_code)

    def test_send_sensor_record_wrong(self):
        with open(self.name_file_error, 'r') as f:
            record = f.readline()
        response = self.client.post('/api/add_sensor_record/',
                                    json.dumps({'record': record}),
                                    content_type='application/json')
        self.assertEqual(500, response.status_code)
