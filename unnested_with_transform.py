import datasets
import collections
import time
import sys

code_counts = collections.defaultdict(int)

start = time.time()
data = datasets.Dataset.from_parquet("mimic_demo" + sys.argv[1] + "/data/*")

for patient in data:
        events = []
        current_start = 0
        current_time = patient['measurements'][0]
        for i, measurement in enumerate(patient['measurements']):
            if current_time != measurement['time']:
                events.append({'time': current_time, 'measurements': patient['measurements'][current_start:i]})
                current_time = measurement['time']
                current_start = i
        events.append({'time': current_time, 'measurements': patient['measurements'][current_start:]})

        for event in events:
            for measurement in event['measurements']:
                code_counts[measurement['code']] += 1 

print(time.time() - start)
