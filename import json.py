import json 
import os

fp = "C:\\Users\\Pavan\\OneDrive\\Desktop\\NDRE\\OPP_Farm_Data_04_05.geojson"
op = "c:/Users/Pavan/OneDrive/Desktop/Crop Health.py"
os.makedirs(op,exist_ok=True)

with open(fp) as file:
    data = json.load(file)
for feature in data['features']:
    feature_id = feature['id', 'Name']
    output_file_path = os.path.join(op, f'feature_{feature_id}.geojson')
    
    feature_data = {
        'type': 'FeatureCollection',
        'features': [feature]
    }
    
    with open(output_file_path, 'w') as output_file:
        json.dump(feature_data, output_file, indent=2)
    
    print(f'Split feature {feature_id} into {output_file_path}')
