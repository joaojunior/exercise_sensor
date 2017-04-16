# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.IntegerField()),
                ('fw', models.IntegerField()),
                ('evt', models.IntegerField()),
                ('coil_revesed', models.CharField(max_length=3)),
                ('power_active', models.FloatField()),
                ('power_reactive', models.FloatField()),
                ('power_appearent', models.FloatField()),
                ('current', models.FloatField()),
                ('voltage', models.FloatField()),
                ('phase', models.FloatField()),
                ('peaks_1', models.FloatField()),
                ('peaks_2', models.FloatField()),
                ('peaks_3', models.FloatField()),
                ('peaks_4', models.FloatField()),
                ('peaks_5', models.FloatField()),
                ('peaks_6', models.FloatField()),
                ('peaks_7', models.FloatField()),
                ('peaks_8', models.FloatField()),
                ('peaks_9', models.FloatField()),
                ('peaks_10', models.FloatField()),
                ('fft_re_1', models.FloatField()),
                ('fft_re_2', models.FloatField()),
                ('fft_re_3', models.FloatField()),
                ('fft_re_4', models.FloatField()),
                ('fft_re_5', models.FloatField()),
                ('fft_re_6', models.FloatField()),
                ('fft_re_7', models.FloatField()),
                ('fft_re_8', models.FloatField()),
                ('fft_re_9', models.FloatField()),
                ('fft_img_1', models.FloatField()),
                ('fft_img_2', models.FloatField()),
                ('fft_img_3', models.FloatField()),
                ('fft_img_4', models.FloatField()),
                ('fft_img_5', models.FloatField()),
                ('fft_img_6', models.FloatField()),
                ('fft_img_7', models.FloatField()),
                ('fft_img_8', models.FloatField()),
                ('fft_img_9', models.FloatField()),
                ('time', models.DateTimeField()),
                ('hz', models.FloatField()),
                ('wifi_strength', models.FloatField()),
                ('dummy', models.FloatField()),
            ],
        ),
    ]
