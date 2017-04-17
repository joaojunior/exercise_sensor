# Introduction

This is a exercise in a job interview.
Section Definition, Clustering and, Your task is part of document send by company.  

# Definition
You have installed an energy sensor in your house, and when you took a look at the events it
was sending, this was the format you were faced with:
```
Device: ID=1; Fw=16071801; Evt=2; Alarms: CoilRevesed=OFF; Power: Active=1753W; Reactive=279var; Appearent=403VA; Line: Current=7.35900021; Voltage=230.08V; Phase=-43,841rad; Peaks: 7.33199978;7.311999799999999;7.53000021;7.48400021;7.54300022;7.62900019;7.36499977;7.28599977;7.37200022;7.31899977; FFT Re: 9748;46;303;33;52;19;19;39;-455; FFT Img: 2712;6;-792;-59;1386;-19;963;33;462; UTC Time: 2016-10-4 16:47:50; hz: 49.87; WiFi Strength: -62; Dummy: 20
```
These events, although really dirty and unintuitive, provide useful electrical information that you
want to use in a simple Machine Learning application that relies on what is called Clustering.
Power includes the three different power values the sensor can measure, transients are also
called peaks, and calculated by Fast Fourier Transforms are the the harmonics, which are
complex numbers. Powers, transients, harmonics and all other measured values are vastly
documented in the literature.

# Clustering
Clustering is the name given to a set of machine learning algorithms used to find unknown
patterns in data. By applying a series of statistical techniques, these algorithms are able to
identify similar data samples and label them accordingly. As the end result, a clustering
algorithm will return an array of labels, with the same size as the array of samples it was given,
where each item will be the label to which the sample at the same index was assigned.

# Your task
You need to create web services that are capable of receiving the events one by one, parse
them to a cleaner, standardized format, save them to a SQL database and, when the event
count reaches 1000, the whole set of events should be sent, in the format required by the
`scikit-learn` library for its clustering algorithms, to feed the following code:
```
from sklearn.cluster import MeanShift, estimate_bandwidth
bandwidth = estimate_bandwidth(data, quantile=0.2, n_samples=200)
ms =MeanShift(bandwidth=bandwidth, cluster_all=False, bin_seeding=True)
labels = ms.fit_predict(data)
```
The variable `data` should contain only the active, reactive and apparent power values, the
current and voltage, and the first three transients. Make sure that no other values are included.
You should get the set of labels returned by the ​fit_predict() method and save it in your SQL
database, assigning the respective label to each event. This service should also be able to send
the parsed, labeled data when requested.
One of the services you create should generate a report containing, at least:
- The number of events associated to each cluster
- The active power average for the events assigned to each cluster.

Feel free to divide this task and create as many services as you think appropriate.

# Solution
The solution have two main parts: 1) The library to parser an record to a dictionary python and 2) An api rest.

The api rest have three urls:
- `/api/add_sensor_record/`: This url receive a record, in format explain above, try to parser and save data. This url only accept post. If is possible parser the data and save in database, this url return a `status_code: 201` and a json with `id` and `device_id` of the new record. If any problem happens when try to parser a specific field in a record, this url return a `status_code: 500` and a json with name of the field with error. For any other errors, this url return a `status_code: 500` 
- `/api/number_events_by_cluster/`: This url return the number of events in each cluster. This url only accept get. The return of this url is a json where a key is a label of the cluster and the value is the quantity of records in this cluster.
- `/api/average_power_active_by_cluster/`: This url return the average power active in each cluster. This url only accept get. The return of this url is a json where a key is a label of the cluster and the value is the average of power active in this cluster.

# How to run
To run this solution only execute `make run`
This command will:
- Install all dependencies in requirements.txt
- Run migrate command to create all tables in database
- run gunicorn

After this, we can use api in the address: `http://127.0.0.1:8000/`

# Examples
Here we send a new record to api:
```
curl -X POST -H "Content-Type: application/json" -d '{"record": "Device: ID=1; Fw=16071801; Evt=2; Alarms: CoilRevesed=OFF; Power: Active=1753W; Reactive=279var; Appearent=403VA; Line: Current=7.35900021; Voltage=230.08V; Phase=-43,841rad; Peaks: 7.33199978;7.311999799999999;7.53000021;7.48400021;7.54300022;7.62900019;7.36499977;7.28599977;7.37200022;7.31899977; FFT Re: 9748;46;303;33;52;19;19;39;-455; FFT Img: 2712;6;-792;-59;1386;-19;963;33;462; UTC Time: 2016-10-4 16:47:50; hz: 49.87; WiFi Strength: -62; Dummy: 20" }' http://127.0.0.1:8000/api/add_sensor_record/
```
And we receive a response with a json, similar below:
```
{"device_id": 1, "id": 1012}
```

To verify the quantity of records in each cluster:
```
curl -X GET http://127.0.0.1:8000/api/number_events_by_cluster/
```
And we receive a response with a json, similar below:
```
{"0": 334, "1": 281, "2": 144, "3": 104, "4": 61, "5": 18, "-1": 70}
```

To verify the average of power active in each cluster:
```
curl -X GET http://127.0.0.1:8000/api/average_power_active_by_cluster/
```
And we receive a response with a json, similar below:
```
{"0": 323.7544910179641, "1": 1716.7686832740214, "2": 1227.826388888889, "3": 2239.2403846153848, "4": 2626.4918032786886, "5": 3590.4444444444443, "-1": 1611.8428571428572}
```
