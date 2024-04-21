import datasets
import os

data = datasets.Dataset.from_parquet("mimic_demo/data/*")

def move_to_single_time(patient):
    first_time = patient['measurements'][0]['time']
    for measurement in patient['measurements']:
        measurement['time'] = first_time
    return patient

moved = data.map(move_to_single_time)

moved.save_to_disk("mimic_demo_moved_ram")
os.mkdir('mimic_demo_moved_disk')
os.mkdir('mimic_demo_moved_disk/data')

moved.to_parquet("mimic_demo_moved_disk/data/data.parquet", compression='zstd')

