#Date Begun: 19/8/2021
#Author: Wolfetone
#

#Imports
import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()
#Constants
BASE_URL = "https://api.n2yo.com/rest/v1/satellite"
API_KEY = os.getenv('API_Key')
API_FUNC_TYPE = "positions"

#Functions
def track_satellite(satellite_id:int, observer_latitude:float, observer_longitude:float, observer_altitude:float, data_type:str):
    """
    Return tracking information for a satellite. 
    Positional arguments:
        satellite_id: the identification number of the satellite.
        observer_latitude: the latitude (in decimal degrees) of the observer's current position. 
        observer_longitude: the longitude (in decimal degrees) of the observer's current position. 
        observer_altitude: the altitude (in meters) above sea level of the observer's current position. 
        data_type: the type of data to return
            azimuth
            elevation
            satlatitude
            satlongitude
            ra
            dec
    """
    position_predictions = "1"

    endpoint_url = f"{BASE_URL}/{API_FUNC_TYPE}/{satellite_id}/{observer_latitude}/{observer_longitude}/{observer_altitude}/{position_predictions}/&apiKey={API_KEY}"

    api_request = requests.get(endpoint_url).json()

    # Satellite azimuth with respect to observer's location (degrees)
    if data_type == 'azimuth':
        return api_request['positions'][0]['azimuth']
    # Satellite elevation with respect to observer's location (degrees)
    if data_type == 'elevation':
        return api_request['positions'][0]['elevation'] 
    # Satellite latitude in decimal degrees 
    if data_type == 'satlatitude':
        return api_request['positions'][0]['satlatitude']
    # Satellite longitude in decimal degrees 
    if data_type == 'satlongitude':
        return api_request['positions'][0]['satlongitude']
    # Satellite right ascension in degrees 
    if data_type == 'ra':
        return api_request['positions'][0]['ra']
    # Satellite declination in degrees 
    if data_type == 'dec':
        return api_request['positions'][0]['dec']
        
def search_id():




count = True
while count:
    print("Current azimuth of the ISS: " + str(track_satellite(25544, 45.971204, -132.858986, 428.81, 'azimuth')) + " degrees.")
    print("Current elevation of the ISS: " + str(track_satellite(25544, 45.971204, -132.858986, 428.81, 'elevation')) + " degrees.\n") 
    time.sleep(7.5)