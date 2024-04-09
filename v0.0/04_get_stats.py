from tflex_params import *
import time
from time import sleep
import xmltodict
import numpy as np

tf = tflex("10.10.10.92")

# Read out available line_ports
config = tf.return_current_config()
line_ports = config.keys()

sleep_counter=5

line_port2 = '1/2/n1'

pm_data = tf.read_pm_data(sleep_counter, line_port2, DEBUG=True)

print(pm_data)

#params = tf.get_params(line_port2)
#print(params)

#print('###')
