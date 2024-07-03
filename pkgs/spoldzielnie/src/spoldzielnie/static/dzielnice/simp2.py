import json

# Step 1: Load the GeoJSON data from a file
with open('warszawa_drogi.geojson', 'r') as file:
    geojson_data = json.load(file)

# Step 2: Iterate through each feature, removing "properties" and "id"
for feature in geojson_data['features']:
    if 'properties' in feature:
        del feature['properties']
    if 'id' in feature:
        del feature['id']

# Step 3: Save the modified GeoJSON data back to a file or use it directly
# To save back to a file:
with open('warszawa_drogi2.geojson', 'w') as file:
    json.dump(geojson_data, file, indent=4)

# Or use the modified data directly in your program