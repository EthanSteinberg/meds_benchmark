import datasets
import os

data = datasets.Dataset.from_parquet("mimic_demo_nested/data/*")

def move_to_single_time(patient):
    result = patient['events'][0]
    for event in patient['events'][1:]:
        for measurement in event['measurements']:
            result['measurements'].append(measurement)

    patient['events'] = [result]
    return patient

moved = data.map(move_to_single_time)

moved.save_to_disk("mimic_demo_nested_moved_ram")
os.mkdir('mimic_demo_nested_moved_disk')
os.mkdir('mimic_demo_nested_moved_disk/data')

moved.to_parquet("mimic_demo_nested_moved_disk/data/data.parquet", compression='zstd')

