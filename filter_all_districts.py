import geopandas as gpd
import os

# Define file paths
geojson_path = "rwanda_boundaries.geojson"
output_folder = "Filtered_Districts"

# Ensure the GeoJSON file exists
if not os.path.exists(geojson_path):
    print(f"❌ Error: GeoJSON file '{geojson_path}' not found!")
    exit(1)

try:
    # Load the Rwanda boundaries GeoJSON file
    gdf = gpd.read_file(geojson_path)
    print("✅ Successfully loaded rwanda_boundaries.geojson")
except Exception as e:
    print(f"❌ Error reading GeoJSON file: {str(e)}")
    exit(1)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Check if "District" column exists
if "District" not in gdf.columns:
    print("❌ Error: 'District' column not found in the GeoJSON file!")
    exit(1)

# Get unique district names
unique_districts = gdf["District"].dropna().unique()

# Process each district
for district in unique_districts:
    try:
        # Filter data for the district
        filtered_gdf = gdf[gdf["District"] == district]

        # Define filename (replace spaces with underscores)
        filename = f"{output_folder}/{district.replace(' ', '_')}.geojson"

        # Save filtered district data
        filtered_gdf.to_file(filename, driver="GeoJSON")
        print(f"✅ Saved: {filename}")
    except Exception as e:
        print(f"❌ Error saving district '{district}': {str(e)}")

print("🎉 All districts have been processed successfully!")
