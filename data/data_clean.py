import json
from datasets import load_dataset
from datetime import datetime

def convert_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat() 
    raise TypeError(f"Type {obj.__class__.__name__} not serializable")

ds = load_dataset("heegyu/news-category-dataset")

output_file_path = 'news_category_dataset.json'

merged_data = []

for split, dataset in ds.items():
    for example in dataset:
        merged_data.append(example)

with open(output_file_path, 'w') as output_file:
    json.dump(merged_data, output_file, default=convert_datetime, indent=2)

print(f"Dataset has been converted and saved as {output_file_path}.")
