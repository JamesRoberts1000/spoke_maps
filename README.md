# Foodbank Hub and Spoke Visualization

This project is based on [willymaps/spoke](https://github.com/willymaps/spoke) and has been adapted to visualize foodbank networks in the UK.

View the map: https://jamesroberts1000.github.io/spoke_maps/

## Description

This interactive web map visualizes foodbank locations using a hub and spoke pattern. The visualization shows connections between a central point and the nearest foodbanks, helping to understand the distribution and accessibility of foodbanks in different areas.

## Features

- Interactive map centered on Dorchester, Dorset
- Dynamic hub and spoke visualization
- Shows 8 nearest foodbanks to any center point
- Automatically updates as you move the map
- Responsive line widths based on zoom level

## Technologies Used

- Mapbox GL JS for map rendering
- Turf.js for geospatial calculations
- D3.js for data handling
- GeoJSON for spatial data format

## Data

The project uses foodbank location data stored in GeoJSON format. The data is fetched and processed using Python, with results stored in `data/foodbanks.json`.

## Usage

Open `index.html` in a web browser to view the visualization. The map will:
- Center on Dorchester initially
- Show the 5 nearest foodbanks
- Update connections as you pan the map
- Adjust line widths based on zoom level

## Setup

1. Clone the repository
2. Update the Mapbox access token in `index.html` if needed
3. Run a local server to view the map
4. Use `fetch_foodbanks_data.py` to update foodbank data if needed