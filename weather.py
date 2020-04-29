#!/usr/bin/python3
import serial
import configparser

## load the config info
config = configparser.ConfigParser()
config.read('config.ini')
serial_port = config['Serial'['port']
serial_rate = config['Serial'].getint('rate')
db_server = config['Database']['server']
database = config['Database']['db']

# set up serial port
def connect_serial:
    ser = serial.Serial(serial_port, serial_rate)