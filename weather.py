#!/usr/bin/python3
import serial
import time
import configparser

ser = serial.Serial('COM3', 115200, timeout=2)

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

while True:
    data = ser.readlines()
    if len(data) > 0:
        goodData = data[0].decode("utf-8").rstrip().split(',')
        print(goodData)
        json_data = { "timestamp": time.time(),
                      "wind_Speed": mak_num(goodData[0]),
                      "wind_dir": goodData[1],
                      "temp_c": mak_num(goodData[2]),
                      "temp_f": mak_num(goodData[3].split(".")[0]),
                      "humidity": mak_num(goodData[4]),
                      "baro": mak_num(goodData[5].split(".")[0]),
                      "rain": mak_num(goodData[6])}
        print(json_data)

ser.close()
