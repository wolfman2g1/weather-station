#!/usr/bin/python3
import serial
import time
from influxdb import InfluxDBClient
from influxdb import exceptions
import configparser
import json

# check that config exists
try:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
except configparser.ParsingError as err:
    print("Config not Found", err)
# import config data from file
serial_port = parser.get('Serial', 'port')
serial_rate = parser.get('Serial', 'rate')
server = parser.get('Database', 'server')
db = parser.get('Database', 'db')
db_port = parser.get('Database', 'db_port')


# timestamp = time.strftime('%Y-%m-%dT%H:%M:%S')


def create_db():
    client = InfluxDBClient(host=server, port=db_port)
    print('Create Database: ' + db)
    client.create_database(db)
    # start()


def set_up(json_data):
    measurement = 'weather_data'
    number_of_points = 10
    timestamp = int(time.time() * 1000)
    json_data = json_data
    data = []
    data.append(
        {
            "measurement": measurement,
            "timestamp": timestamp,
            "fields": {
                "data": json_data
            }
        }
    )
    store_data(data)


def store_data(data):
    client = InfluxDBClient(host=server, port=db_port)
    try:
        client.write_points(data, database=db,
                            protocol='line', time_precision='ms')
    except exceptions.InfluxDBClientError as err:
        print("Uh oh", err)


def mak_num(thing):
    try:
        thing2 = int(thing.split(".")[0])
    except:
        thing2 = 0
    return thing2


def mak_float(thing):
    try:
        if "." in thing:
            thing2 = float(thing)
        else:
            thing2 = float(thing + ".0")
    except:
        thing2 = 0
    return thing2
def make_empty(thing):
    try:
        if "??" in thing:
            thing = " "
    except:
        thing = "null"
    return thing


def start():
    create_db()
    ser = serial.Serial(serial_port, serial_rate, timeout=2, )
    while True:
        data = ser.readlines()
        if len(data) > 0:
            measurement_name = 'weather_data'
            goodData = data[0].decode("utf-8").rstrip().split(',')
            timedata = int(time.time() * 1000)
            wind_Speed = mak_num(goodData[0])
            wind_dir = make_empty(goodData[1])
            temp_c = mak_num(goodData[2])
            temp_f = mak_num(goodData[3].split(".")[0])
            humidity = mak_num(goodData[4])
            baro = mak_num(goodData[5].split(".")[0])
            rain = mak_num(goodData[6])
            data = []
            data.append(
                "{measurement},wind_direction={wind_dir},wind_velocity={wind_speed},fahrenheit={tempF}, celcius={tempC}, humidit={relative_hum}, preasure={qnh}, rain={precip}, time={timeinfo}".format(
                    measurement=measurement_name, wind_dir=wind_dir, wind_speed=wind_Speed, tempF=temp_f, tempC=temp_c, relative_hum=humidity, qnh=baro, precip=rain, timeinfo=timedata
                ))
            #json_data = json.dumps(list_data, indent=2)
            store_data(data)


            # print(list_data)
    ser.close()


if __name__ == "__main__":
    start()
