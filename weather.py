#!/usr/bin/python3
try:
    import serial
    import time
    import configparser
    import json
    from influxdb import InfluxDBClient
    import logging
    from retrying import retry
except Exception as err:
    print('some Python modules are missing {}'.format_map(err))

# set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# check that config exists
try:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
except configparser.ParsingError as err:
    print("Config not Found {}".format_map(err))

# import config data from file
serial_port = parser.get('Serial', 'port')
serial_rate = parser.get('Serial', 'rate')

# import datastore option

datastore = parser.get('DATASTORE', 'influx')

influx_server = parser.get('INFLUX', 'influx_server')
user = parser.get('INFLUX', 'user')
password = parser.get('INFLUX', 'password')
database = parser.get('INFLUX', 'database')
retention = parser.get('INFLUX', 'retention')

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


#@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def sendToInflux(payload={}):
    client = InfluxDBClient(host=influx_server, username=user, password=password, database=database, port=8086,
                            ssl=False)

    try:
        client.write_points(json.dumps(payload))

    except Exception as e:
        logger.exception(e)


def start():
    ser = serial.Serial(serial_port, serial_rate, timeout=2)
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    while True:
        json_data = {}
        data = ser.readlines()
        try:
            goodData = data[0].decode("utf-8").rstrip().split(',')
            json_data = {
                         "wind_Speed": mak_num(goodData[0]),
                         "wind_dir": goodData[1],
                         "temp_c": mak_num(goodData[2]),
                         "temp_f": mak_num(goodData[3]),
                         "humidity": mak_num(goodData[4]),
                         "baro": mak_num(goodData[5]),
                         "rain": mak_num(goodData[6])
                         }


        except:
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            time.sleep(5)
        # occasionally we seem to loose connnection to rabbitmq so if that happens we'll wait 15 seconds then try again
        while True:
            try:
               sendToInflux(json_data)
            except:
               time.sleep(15)


    ser.close()


if __name__ == "__main__":
    client = InfluxDBClient(host=influx_server, username=user, password=password, database=database, port=8086,
                            ssl=False)
    client.create_database(database)
    client.create_retention_policy(database, duration='60d', replication='1', database=database)
    start()
