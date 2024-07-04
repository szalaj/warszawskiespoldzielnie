import geojson
from shapely.geometry import shape, mapping
from shapely.ops import transform
from functools import partial


def simplify_geometry(geometry, tolerance=0.001):
    """
    Simplify the geometry to reduce the number of points.
    :param geometry: GeoJSON geometry
    :param tolerance: Tolerance level for simplification
    :return: Simplified GeoJSON geometry
    """
    try:
        shp_geom = shape(geometry)
        simplified_geom = shp_geom.simplify(tolerance, preserve_topology=True)
        return mapping(simplified_geom)
    except Exception as e:
        print(f"Error simplifying geometry: {e}")
        return geometry

# Load your geojson file
with open('warszawa-drogi-wszystkie-s.geojson') as f:
    data = geojson.load(f)

# Simplify each feature in the GeoJSON
for feature in data['features']:
    if 'geometry' in feature and feature['geometry'] is not None:
        feature['geometry'] = simplify_geometry(feature['geometry'])
    else:
        print("Skipping feature with no geometry")

# Save the simplified GeoJSON
with open('simplified_roads.geojson', 'w') as f:
    geojson.dump(data, f)
