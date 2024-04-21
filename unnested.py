import datasets
import collections
import time
import sys

code_counts = collections.defaultdict(int)

start = time.time()
data = datasets.Dataset.from_parquet("mimic_demo" + sys.argv[1] + "/data/*")

for patient in data:
        for measurement in patient['measurements']:
            code_counts[measurement['code']] += 1
print(time.time() - start)
