from fastapi import FastAPI, HTTPException
import geopandas as gpd
import json
from fastapi.responses import JSONResponse

class RwandaBoundariesAPI:
    def __init__(self, shapefile_path):
        try:
            self.gdf = gpd.read_file(shapefile_path)
            self.save_geojson("rwanda_boundaries.geojson")  # Save GeoJSON on initialization
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading shapefile: {str(e)}")

    def get_boundaries(self):
        """
        Retrieve Rwanda boundaries in GeoJSON format.
        """
        return self.gdf.to_json()

    def get_district_boundaries(self, district_name):
        """
        Retrieve boundaries of a specific district.
        """
        district_filtered = self.gdf[self.gdf["District"].str.lower() == district_name.lower()]

        if district_filtered.empty:
            raise HTTPException(status_code=404, detail="District not found")

        return district_filtered.to_json()

    def save_geojson(self, output_path):
        """
        Save the boundaries as a GeoJSON file.
        """
        try:
            self.gdf.to_file(output_path, driver="GeoJSON")
            print(f"GeoJSON file saved at: {output_path}")
        except Exception as e:
            print(f"Error saving GeoJSON: {e}")

# Initialize the API class and save GeoJSON
data_api = RwandaBoundariesAPI("./RwandaShapeFileAdministrativeBoundary/Villages_Boundaries_NISR.shp")

# FastAPI setup
app = FastAPI()

@app.get("/")
def read_root():
    """
    Returns a welcome message for the Rwanda Boundaries API.
    """
    return {"message": "Rwanda Boundaries API"}

@app.get("/boundaries")
def get_boundaries():
    """
    Returns the Rwanda boundaries in GeoJSON format.
    """
    return JSONResponse(content=json.loads(data_api.get_boundaries()))

@app.get("/boundaries/{district}")
def get_district_boundaries(district: str):
    """
    Returns the boundaries of a specific district.
    """
    return JSONResponse(content=json.loads(data_api.get_district_boundaries(district)))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
