# Hawaii-Weather-Explorer
Plan your dream vacation in Honolulu, Hawaii with this interactive weather analysis tool! Explore historical climate data, find the best time to visit, and discover local attractions. No APIs required - everything you need is included in the project. Start planning your perfect getaway now!

# Aloha from Honolulu! 🌴🌺

## Overview
Aloha! Welcome to your virtual getaway to Honolulu, Hawaii! 🌞 In this project, we embark on a journey to analyze the climate of this tropical paradise, providing you with valuable insights for your holiday planning. From pristine beaches to lush landscapes, get ready to immerse yourself in the beauty of Honolulu's weather data.

## Requirements
- Python 3
- Pandas
- Matplotlib
- SQLAlchemy
- Flask
- Jupyter Notebook (for data analysis)
- SQLite database (provided: hawaii.sqlite)

**Note:** While we won't be connecting to external APIs for our analysis, fear not! The data used for analysis is sourced directly from our project resources and the provided SQLite database. However, if you're feeling adventurous and want to integrate external APIs to spice things up, feel free to explore! 🏖️

## Instructions
### Part 1: Analyze and Explore the Climate Data
Welcome aboard our exploration journey! Let's dive into the crystal-clear waters of Honolulu's climate data:
1. Use Python and SQLAlchemy to connect to the SQLite database.
2. Reflect tables into classes using SQLAlchemy automap_base().
3. Ride the wave of precipitation analysis:
   - Find the most recent date in the dataset.
   - Catch a wave with the previous 12 months of precipitation data.
   - Plot the results and hang loose with some summary statistics.
4. Embark on a station analysis:
   - Calculate the total number of stations.
   - Ride the swell to find the most-active station.
   - Feel the warmth as we calculate the lowest, highest, and average temperatures for the most-active station.
   - Get the previous 12 months of temperature observation (TOBS) data for the most-active station and ride the crest with a histogram.
5. Close the SQLAlchemy session and let's catch some rays!

### Part 2: Design Your Climate App
1. Design a Flask API with routes:
   - /: Homepage with a list of available routes.
   - /api/v1.0/precipitation: Precipitation data for the last 12 months.
   - /api/v1.0/stations: List of stations.
   - /api/v1.0/tobs: Temperature observations for the last year of the most-active station.
   - /api/v1.0/<start> and /api/v1.0/<start>/<end>: Min, max, and average temperatures for specified date ranges.

2. Hang loose and run the Flask app to access the API endpoints.

## How to Run
1. Pack your virtual bags and clone the repository to your local machine.
2. Navigate to the repository directory.
3. Inside the repository, you'll find:
   - A 'resources' folder containing resources for the project.
   - An 'srs' folder with source files for the initial project stages.
   - The main directory, which includes:
     - The 'app.py' file, the Flask application for the project.
     - 'climate_resources.ipynb', the Jupyter Notebook for the initial climate analysis.

4. Fire up Jupyter Notebook for data analysis and ride the wave of exploration.
5. Get ready to surf the web as you run the Flask app to access the API. 🏄‍♂️
6. 
## Credits
- Big mahalo to Berkely Data Analytics and UC Berkeley Extension for their support in crafting this tropical getaway of a project!
- Shoutout to ChatGPT for providing assistance and guidance during the development of these projects.

### Source Code
A special acknowledgment to the contributors of the UCB-VIRT-DATA-PT-11-2023-U-LOLC GitHub repository for their invaluable code and resources used in this project.
