# Rwanda Boundaries API

## Overview
This project provides a FastAPI-based API service that retrieves Rwanda's administrative boundaries. It uses a shapefile of Rwanda's administrative boundaries and exposes endpoints for querying the data in GeoJSON format. Additionally, there is a script (`filter_all_district.py`) to filter the districts and save them separately.

## Features
- Retrieve Rwanda's boundaries in GeoJSON format.
- Retrieve the boundaries of a specific district by name.
- Filter and save each district's boundaries as a separate GeoJSON file.

## Project Structure

- `main.py`: The FastAPI application that exposes the API.
- `filter_all_district.py`: A script that filters each district from the shapefile and saves it as a separate GeoJSON file.
- `requirements.txt`: The dependencies for the project.

## API Endpoints

### 1. `/`
- **Method**: GET
- **Description**: Returns a welcome message for the Rwanda Boundaries API.
- **Response**:
  ```json
  {"message": "Rwanda Boundaries API"}

### 2. `/boundaries`
- Method: GET
- Description: Returns the entire Rwanda - boundaries in GeoJSON format.
- Response: A GeoJSON representation of - Rwanda's boundaries.
### 3. `/boundaries/{district}`
- Method: GET
- Description: Returns the boundaries of a specific district.
- Parameters:
    - district: The name of the district (case-insensitive).
- Response: A GeoJSON representation of the specified district's boundaries.

### Installation
To run this project, you'll need to install the necessary dependencies. You can do this by running the following command:
`pip install -r requirements.txt `

### Requirements
The requirements.txt includes the following packages:

- geopandas
- fastapi
- uvicorn
- shapely
- flask-cors
- geopandas folium

### Running the FastAPI Application

Once you have the dependencies installed, you can run the FastAPI application with the following command:

`uvicorn main:app --reload` This will start the server on ```http://127.0.0.1:8000/```.

### Example Requests
`GET http://127.0.0.1:8000/`: Returns a welcome message.
`GET http://127.0.0.1:8000/boundaries`: Returns the GeoJSON of Rwanda boundaries.
`GET http://127.0.0.1:8000/boundaries/Kigali`: Returns the GeoJSON of Kigali district boundaries.

### `filter_all_district.py` Script
This script reads the shapefile of Rwanda's administrative boundaries and filters the data by each district. It saves each district's boundaries as a separate GeoJSON file in the Filtered_Districts directory.

### How to Run the Script
1. Ensure that the shapefile (Villages_Boundaries_NISR.shp) is available at the specified path.
2. Run the script using the following command:

`python
python filter_all_district.py
`

The script will generate separate GeoJSON files for each district and store them in the Filtered_Districts directory.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

###### How to use in a code editor:
- Open your code editor (e.g., VS Code, PyCharm).
- Create a new file named README.md.
- Paste the markdown content into this file.
- This README.md will guide users through understanding and running the API as - - well as using the filtering script.


***Simply copy and save the content provided into a `.md` file. When you open this file in any markdown editor or viewer, it will display as a well-formatted guide.***


