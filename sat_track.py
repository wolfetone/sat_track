#Date Begun: 19/8/2021
#Author: Wolfetone
#

#Imports
import requests
import json
import time 

#Constants
BASE_URL = "https://api.n2yo.com/rest/v1/satellite"
API_KEY = "C3LQLD-J5AEMK-UCFGQK-4RMA"
API_FUNC_TYPE = "positions"

#Functions
def iss_track(observer_latitude:float, observer_longitude:float, observer_altitude:float, data_type:str):
    """
    Return tracking information for the ISS. 
    Positional arguments:
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

    satellite_id = "25544"
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





count = True
while count:
    print("Current azimuth of the ISS: " + str(iss_track(38.971204, -122.858986, 428.81, 'azimuth')) + " degrees.")
    print("Current elevation of the ISS: " + str(iss_track(38.971204, -122.858986, 428.81, 'elevation')) + " degrees.\n") 
    time.sleep(7.5)