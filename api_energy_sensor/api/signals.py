from django.db.models.signals import post_save
from django.dispatch import receiver
from sklearn.cluster import MeanShift, estimate_bandwidth
from numpy import asarray

from api.models import SensorRecord


@receiver(post_save, sender=SensorRecord)
def new_record(sender, instance, created, **kwargs):
    if (created is True and (SensorRecord.objects.count() % 1000)) == 0:
        cluster()


def cluster():
    values = SensorRecord.objects.values_list('id', 'power_active',
                                              'power_reactive',
                                              'power_appearent', 'current',
                                              'voltage', 'peaks_1', 'peaks_2',
                                              'peaks_3')
    values_without_id = [value[1:] for value in values]
    ids = [value[0] for value in values]
    values_without_id = asarray(values_without_id)
    bandwidth = estimate_bandwidth(values_without_id,
                                   quantile=0.2, n_samples=200)
    ms = MeanShift(bandwidth=bandwidth, cluster_all=False, bin_seeding=True)
    labels = ms.fit_predict(values_without_id)
    for idx, label in zip(ids, labels):
        SensorRecord.objects.filter(pk=idx).update(cluster_label=label)
