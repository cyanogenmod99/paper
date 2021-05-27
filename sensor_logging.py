import sys
#import pyserial
import serial
import datetime
import time
import json
import numpy as np
import pandas as pd

def serial_to_csv(s, f, ts, now, sensor_id):
    # read 1
    data = s.readline()
    # separate by [,]
    m = str(data).split(",")
    if (len(m) == 16):
        if (m[1] != ''):
            try:
                ts = float(m[1])
            except ValueError:
                ts = -100
            sensor_id = m[5]
            try:
                x = int(m[12])
            except ValueError:
                x = np.nan
            try:
                y = int(m[13])
            except ValueError:
                y = np.nan
            try:
                z = int(m[14])
            except ValueError:
                z = np.nan
            now = datetime.datetime.now()
            print(sensor_id)
            
        else:
            try:
                x = int(m[12])
            except ValueError:
                x = np.nan
            try:
                y = int(m[13])
            except ValueError:
                y = np.nan
            try:
                z = int(m[14])
            except ValueError:
                z = np.nan
            ts += 0.01
            now += td
        
        
        # csv 
        new_data = '{:.2f},{},{},{},{},{}\n'.format(ts, now, sensor_id, x, y, z)
        f.write(new_data)
        print(new_data)
        
    return ts, now, sensor_id

# make file
acc_log_path = './test.csv'  #change name
try:
    f = open(acc_log_path, 'x')
except FileExistsError:
    print('file already exist')
    sys.exit(0)

# serial port setting
#port_name_1 = '/dev/tty.usbserial-MW2TK513'
#try:
#    s1 = serial.Serial(port_name_1, 115200, timeout=0.01)
#except serial.serialutil.SerialException:
#    print('serial port not found')
#    sys.exit(0)


# port_name_2 = '/dev/tty.usbserial-MW4QGRZB'
# try:
#     s2 = serial.Serial(port_name_2, 115200, timeout=0.01)
# except serial.serialutil.SerialException:
#     print('serial port not found')
#     sys.exit(0)

# port_name_3 = '/dev/tty.usbserial-MW3F8QM9'
# try:
#     s3 = serial.Serial(port_name_3, 115200, timeout=0.01)
# except serial.serialutil.SerialException:
#     print('serial port not found')
#     sys.exit(0)

#port_name_4 = '/dev/tty.usbserial-MW4QGTKE'
#try:
#    s4 = serial.Serial(port_name_4, 115200, timeout=0.01)
#except serial.serialutil.SerialException:
#    print('serial port not found')
#    sys.exit(0)

# port_name_5 = '/dev/tty.usbserial-MW3F8UGG'
# try:
#     s5 = serial.Serial(port_name_5, 115200, timeout=0.01)
# except serial.serialutil.SerialException:
#     print('serial port not found')
#     sys.exit(0)

port_name_6 = 'COM6'
try:
    s6 = serial.Serial(port='COM6', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0.01)
except serial.serialutil.SerialException:
    print('serial port not found')
    sys.exit(0)

#port_name_7 = 'COM7'
#try:
#    s7 = serial.Serial(port_name_7, 115200, timeout=0.01)
#except serial.serialutil.SerialException:
#    print('serial port not found')
#    sys.exit(0)

f.write('ts,datetime,sensor_id,x,y,z\n')

# ts1 = ts2 = ts3 = ts4 = ts5 = ts6 = 
# ts1 = ts4 = ts7 = 0.0
ts6 = 0.0
# sensor_id_1 = sensor_id_2 = sensor_id_3 = sensor_id_4 = sensor_id_5 = sensor_id_6 = 
#sensor_id_1 = sensor_id_4 = sensor_id_7 = ''
sensor_id_6 = ''
x = y = z = 0.0

start_time = time.time()
# now1 = now2 = now3 = now4 = now5 = now6 = 
#now1 = now4 = now7 = datetime.datetime.now()
now = datetime.datetime.now()
td = datetime.timedelta(milliseconds=10)

try:
    while 1:
        # csv
        #ts1, now1, sensor_id_1 = serial_to_csv(s1, f, ts1, now1, sensor_id_1)
        # ts2, now2, sensor_id_2 = serial_to_csv(s2, f, ts2, now2, sensor_id_2)
        # ts3, now3, sensor_id_3 = serial_to_csv(s3, f, ts3, now3, sensor_id_3)
        #ts4, now4, sensor_id_4 = serial_to_csv(s4, f, ts4, now4, sensor_id_4)
        # ts5, now5, sensor_id_5 = serial_to_csv(s5, f, ts5, now5, sensor_id_5)
        ts6, now6, sensor_id_6 = serial_to_csv(s6, f, ts6, now6, sensor_id_6)
        #ts7, now7, sensor_id_7 = serial_to_csv(s7, f, ts7, now7, sensor_id_7)
       
except KeyboardInterrupt:
    print('\nInterrupted')

f.close()

# time
tact_time = int(time.time() - start_time)
if tact_time >= 60:
    minutes = int(tact_time // 60)
    seconds = int(tact_time % 60)
    tact_time = '{}min {}sec'.format(minutes, seconds)
else:
    tact_time = '{}sec'.format(tact_time)
print('tact_time:{}'.format(tact_time))

#tact_time_log_path = './data/tact.txt'
#with open(tact_time_log_path, mode='a') as f:
#    f.write('{}: {}\n'.format(acc_log_path, tact_time))

#s1.close()
# s2.close()
# s3.close()
#s4.close()
# s5.close()
s6.close()
#s7.close()
sys.exit(0)
    
