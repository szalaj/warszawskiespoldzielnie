import geojson

def convert_geometrycollection_to_featurecollection(input_file, output_file):
    # Load the simplified GeoJSON file
    with open(input_file, 'r') as f:
        data = geojson.load(f)

    # Check if the root object is a GeometryCollection
    if data['type'] != 'GeometryCollection':
        raise ValueError("Input file is not a GeometryCollection")

    # Convert GeometryCollection to FeatureCollection
    features = []
    for geometry in data['geometries']:
        # Create a feature with geometry, add properties if needed
        feature = geojson.Feature(geometry=geometry, properties={})
        features.append(feature)
    
    feature_collection = geojson.FeatureCollection(features)
    print(feature_collection)
    # Save the converted GeoJSON
    with open(output_file, 'w') as f:
        geojson.dump(feature_collection, f)

    print(f"Converted GeoJSON saved to {output_file}")

# Paths to your files
input_file = 'warszawa_drogi2b.json'
output_file = 'warszawa_drogi2ba.geojson'

# Convert the file
convert_geometrycollection_to_featurecollection(input_file, output_file)
