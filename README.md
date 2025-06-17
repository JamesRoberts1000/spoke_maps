# Food bank Hub and Spoke Visualisation

This project is based on [willymaps/spoke](https://github.com/willymaps/spoke) and has been adapted to visualise food bank networks in the UK.

View the map: https://jamesroberts1000.github.io/spoke_maps/

## Description

This interactive web map visualises food bank locations using a hub and spoke pattern. The visualisation shows connections between a central point and the nearest food banks, helping to understand the distribution and accessibility of food banks in different areas.

## Features

- Interactive map centered on Dorchester, Dorset
- Dynamic hub and spoke visualisation
- Shows 8 nearest food banks to any center point
- Automatically updates as you move the map
- Responsive line widths based on zoom level

## Technologies Used

- Mapbox GL JS for map rendering
- Turf.js for geospatial calculations
- D3.js for data handling
- GeoJSON for spatial data format

## Data

The project uses food bank location data stored in GeoJSON format. The data is fetched and processed using Python, with results stored in `data/foodbanks.json`.

## Usage

Open `index.html` in a web browser to view the visualisation. The map will:
- Center on Dorchester initially
- Show the 5 nearest food banks
- Update connections as you pan the map
- Adjust line widths based on zoom level

## Setup

1. Clone the repository
2. Update the Mapbox access token in `index.html` if needed
3. Run a local server to view the map
4. Use `fetch_foodbanks_data.py` to update food bank data if needed