import re


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self):
        self.message = 'The record is incorrect'


class FieldError(Error):
    def __init__(self, field):
        message = 'Error during processing the field {0} in record'
        self.message = message.format(field)


def parser_sensor2dict(record):
    result = {}
    regex_number = re.compile('(-?\d+[.]\d+|-?\d+)')
    mask_str = '(OFF|ON|\d\d\d\d-\d\d?-\d\d? \d\d?:\d\d?:\d\d?)'
    regex_string = re.compile(mask_str)
    fields = ['device_id', 'fw', 'evt', 'coil_revesed', 'power_active',
              'power_reactive', 'power_appearent', 'current', 'voltage',
              'phase', 'peaks_1', 'peaks_2', 'peaks_3', 'peaks_4',
              'peaks_5', 'peaks_6', 'peaks_7', 'peaks_8', 'peaks_9',
              'peaks_10', 'fft_re_1', 'fft_re_2', 'fft_re_3', 'fft_re_4',
              'fft_re_5', 'fft_re_6', 'fft_re_7', 'fft_re_8', 'fft_re_9',
              'fft_img_1', 'fft_img_2', 'fft_img_3', 'fft_img_4',
              'fft_img_5', 'fft_img_6', 'fft_img_7', 'fft_img_8',
              'fft_img_9', 'time', 'hz', 'wifi_strength', 'dummy']
    for idx, field in enumerate(fields):
        fields[idx] = (field, regex_number)
    fields[3] = ('coil_revesed', regex_string)
    fields[38] = ('time', regex_string)
    if isinstance(record, str) is False:
        raise InputError
    record = record.replace(',', '.')
    record = record.split(';')
    if len(record) != 42:
        raise InputError
    for idx, (field, regex) in enumerate(fields):
        value = regex.findall(record[idx])
        if len(value) == 1:
            result[field] = value[0]
        else:
            raise FieldError(field)
    return result
