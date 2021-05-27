import sys
#import pyserial
import serial
import datetime
import time
import json
import numpy as np
import pandas as pd
import serial
ser = serial.Serial(port='COM6', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

while 1:
    data = ser.readline()

    # 先頭の「:」を取り除く
    data = data[2:]
    spilitdatum = data.decode('utf-8').split(":")

    dict = {}

    # key,value型にしてディクショナリに保存
    for spilitdata in spilitdatum:

        s_key = spilitdata.split("=")[0]
        s_val = spilitdata.split("=")[1]

        dict[s_key] = s_val
    print(dict)