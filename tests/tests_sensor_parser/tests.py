import unittest
import os


from sensor_parser.parser import parser_sensor2dict, InputError, FieldError


class TestParser(unittest.TestCase):
    def setUp(self):
        path = os.path.abspath(__file__)
        path = os.path.dirname(path)
        self.name_file = os.path.join(path, 'data/sensor_data.txt')
        self.name_file_error = os.path.join(path, 'data/sensor_data_error.txt')

    def test_parser_record_ok(self):
        expect = {'device_id': '1', 'fw': '16071801', 'evt': '2',
                  'coil_revesed': 'OFF', 'power_active': '1753',
                  'power_reactive': '279', 'power_appearent': '403',
                  'current': '7.35900021', 'voltage': '230.08',
                  'phase': '-43.841', 'peaks_1': '7.33199978',
                  'peaks_2': '7.311999799999999', 'peaks_3': '7.53000021',
                  'peaks_4': '7.48400021', 'peaks_5': '7.54300022',
                  'peaks_6': '7.62900019', 'peaks_7': '7.36499977',
                  'peaks_8': '7.28599977', 'peaks_9': '7.37200022',
                  'peaks_10': '7.31899977', 'fft_re_1': '9748',
                  'fft_re_2': '46', 'fft_re_3': '303', 'fft_re_4': '33',
                  'fft_re_5': '52', 'fft_re_6': '19', 'fft_re_7': '19',
                  'fft_re_8': '39', 'fft_re_9': '-455', 'fft_img_1': '2712',
                  'fft_img_2': '6', 'fft_img_3': '-792', 'fft_img_4': '-59',
                  'fft_img_5': '1386', 'fft_img_6': '-19',
                  'fft_img_7': '963', 'fft_img_8': '33',
                  'fft_img_9': '462', 'time': '2016-10-4 16:47:50',
                  'hz': '49.87', 'wifi_strength': '-62', 'dummy': '20'}
        with open(self.name_file, 'r') as f:
            record = f.readline()
        self.assertEqual(expect, parser_sensor2dict(record))

    def test_parser_record_size_incorrect(self):
        record = 'Device: ID=1; Fw=16071801'
        with self.assertRaises(InputError):
            parser_sensor2dict(record)

    def test_parser_record_empty(self):
        record = ''
        with self.assertRaises(InputError):
            parser_sensor2dict(record)

    def test_field_in_record_is_incorrect(self):
        with open(self.name_file_error, 'r') as f:
            record = f.readline()
        with self.assertRaises(FieldError):
            parser_sensor2dict(record)
