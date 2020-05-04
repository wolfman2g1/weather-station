#!/usr/bin/python3
import serial
import time
from influxdb import InfluxDBClient
import configparser

## check that config exists
try:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
except configparser.ParsingError as err:
    print("Config not Found", err)
## import config data from file
serial_port = parser.get('Serial', 'port')
serial_rate = parser.get('Serial', 'rate')
server = parser.get('Database', 'server')
db = parser.get('Database', 'db')
db_port = parser.get('Database', 'db_port')




def create_db():
    client = InfluxDBClient(host=server, port=db_port)
    client.create_database('weather')
    #start()


def store_data(json_data):
    client = InfluxDBClient(host=server, port=db_port)
    client.write_points('weather', json_data)


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


def start():
    create_db()
    ser = serial.Serial(serial_port, serial_rate, timeout=2)
    while True:
        data = ser.readlines()
        if len(data) > 0:
            goodData = data[0].decode("utf-8").rstrip().split(',')
            print(goodData)
            json_data = {"timestamp": time.time(),
                         "wind_Speed": mak_num(goodData[0]),
                         "wind_dir": goodData[1],
                         "temp_c": mak_num(goodData[2]),
                         "temp_f": mak_num(goodData[3].split(".")[0]),
                         "humidity": mak_num(goodData[4]),
                         "baro": mak_num(goodData[5].split(".")[0]),
                         "rain": mak_num(goodData[6])}
            
            #print(json_data)
    ser.close()


if __name__ == "__main__":
    start()
