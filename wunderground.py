#!/usr/bin/python3
try:
    import requests
    import configparser
except Exception as err:
    print('some Python modules are missing {}'.format_map(err))

# check that config exists
try:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
except configparser.ParsingError as err:
    print("Config not Found {}".format_map(err))

station_id = parser.get('WUNDERGROUND', 'station_id')
station_pass = parser.get('WUNDERGROUND', 'station_pass')

class Upload(object):
   def send_data(self, data):
       endpoint = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
       date_str = "&dateutc=now"
       action_str = "&action=updateraw"
''' need to get the data dict and parse it'''
''' need to add the data to the request string'''
'''r= requests.get(
    WUurl +
    WUcreds +
    date_str +
    "&humidity=" + humidity_str +
    action_str)'''
'''print("Received " + str(r.status_code) + " " + str(r.text))'''
