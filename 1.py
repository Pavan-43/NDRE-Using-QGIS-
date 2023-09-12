import geopandas as gpd

polygons = gpd.read_file("C:\\Users\\Pavan\\OneDrive\\Desktop\\NDRE\\OPP_Farm_Data_04_05.geojson")

print("CRS of GeoJSON file:", polygons.crs)
