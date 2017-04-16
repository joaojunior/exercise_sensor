import os
import json

from django.test import TestCase

from model_mommy import mommy

from api.models import SensorRecord


class TestApi(TestCase):
    def setUp(self):
        path = os.path.abspath(__file__)
        path = os.path.dirname(path)
        self.name_file = os.path.join(path, 'test_data/sensor_data.txt')
        self.name_file_error = os.path.join(path,
                                            'test_data/sensor_data_error.txt')
        self.name_file_example = os.path.join(path, 'test_data/events.txt')

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

    def test_send_sensor_ok(self):
        with open(self.name_file, 'r') as f:
            record = f.readline()
        response = self.client.post('/api/add_sensor_record/',
                                    json.dumps({'record': record}),
                                    content_type='application/json')
        self.assertEqual(201, response.status_code)
        expected = {'id': 1, 'device_id': 1}
        self.assertEqual(expected, response.json())


class TestStatsSGBDEmpty(TestCase):
    def test_number_events_in_each_cluster(self):
        response = self.client.get('/api/number_events_by_cluster/')
        expected = {}
        self.assertEqual(expected, response.json())

    def test_power_active_average_in_each_cluster(self):
        response = self.client.get('/api/average_power_active_by_cluster/')
        expected = {}
        self.assertEqual(expected, response.json())


class TestStats(TestCase):
    def setUp(self):
        # create data group 1
        mommy.make(SensorRecord, cluster_label=1, power_active=10)
        mommy.make(SensorRecord, cluster_label=1, power_active=15)
        # create data group 2
        mommy.make(SensorRecord, cluster_label=2, power_active=9)
        mommy.make(SensorRecord, cluster_label=2, power_active=6)
        mommy.make(SensorRecord, cluster_label=2, power_active=15)
        # create data group 3
        mommy.make(SensorRecord, cluster_label=3, power_active=0)
        mommy.make(SensorRecord, cluster_label=3, power_active=0)
        mommy.make(SensorRecord, cluster_label=3, power_active=0)
        mommy.make(SensorRecord, cluster_label=3, power_active=0)

    def test_number_events_in_each_cluster(self):
        response = self.client.get('/api/number_events_by_cluster/')
        expected = {'1': 2, '2': 3, '3': 4}
        self.assertEqual(expected, response.json())

    def test_power_active_average_in_each_cluster(self):
        response = self.client.get('/api/average_power_active_by_cluster/')
        expected = {'1': 12.5, '2': 10, '3': 0}
        self.assertEqual(expected, response.json())
