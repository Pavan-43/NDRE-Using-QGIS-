import geopandas as gpd
import rasterio
from rasterio.mask import mask

# Read the GeoJSON file with a single polygon
polygons = gpd.read_file(r"C:\\Users\\Pavan\\OneDrive\\Desktop\\NDRE\\output\\1611807886004.geojson")

# Reproject the GeoJSON file to match the CRS of the GeoTIFF file (EPSG:3857)
polygons = polygons.to_crs("EPSG:3857")

# Read the GeoTIFF file
with rasterio.open(r"C:\\Users\\Pavan\\OneDrive\\Desktop\\NDRE\\Copy of NDRE.tif") as src:
    # Clip the GeoTIFF file using the reprojected polygon
    clipped, transform = mask(src, polygons.geometry, crop=True)

    # Update the metadata of the clipped GeoTIFF file
    clipped_meta = src.meta.copy()
    clipped_meta.update({
        'height': clipped.shape[1],
        'width': clipped.shape[2],
        'transform': transform
    })

# Save the clipped GeoTIFF file
clipped_file = "C:\\Users\\Pavan\\OneDrive\\Desktop\\NDRE\\clipped_output.tif"
with rasterio.open(clipped_file, 'w', **clipped_meta) as dst:
    dst.write(clipped, indexes=src.indexes)

print("Clipping successful. The output is saved at:", clipped_file)
