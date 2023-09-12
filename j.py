# import json
# file = open("C:\\Users\\Pavan\\OneDrive\\Desktop\\NDRE\\OPP_Farm_Data_04_05.geojson" , "r")
# x=file.read()
# terminaldata = json.loads(x)

# print(terminaldata);

import os
import json

input_file = r"C:\Users\Pavan\OneDrive\Desktop\NDRE\OPP_Farm_Data_04_05.geojson"
output_dir = r"C:\Users\Pavan\OneDrive\Desktop\NDRE\output"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the input GeoJSON file
with open(input_file) as f:
    data = json.load(f)

# Iterate over each feature in the GeoJSON file
for feature in data["features"]:
    # Extract the polygon coordinates and attributes
    polygon = feature["geometry"]
    attributes = feature["properties"]

    # Create a new GeoJSON feature
    new_feature = {
        "type": "Feature",
        "properties": attributes,
        "geometry": polygon
    }

    # Generate a filename for the output file using a unique identifier
    identifier = attributes["polygon_id"]  
    # Modify this line based on your attribute name
    output_filename = os.path.join(output_dir, f"{identifier}.geojson")

    # Write the new feature to a separate GeoJSON file
    with open(output_filename, "w") as f:
        json.dump(new_feature, f)

    print(f"Saved {output_filename}")

print("Splitting complete.")
