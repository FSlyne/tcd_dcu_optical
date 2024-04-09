from tflex_params import *
import time
from time import sleep
import xmltodict
import numpy as np

tf = tflex("10.10.10.92")

# Read out available line_ports
config = tf.return_current_config()
line_ports = config.keys()
# 
# line_port1 = '1/1/n1'
# 
# logical_interface1 = 'ot100'
# modulation1 = 'dp-qpsk'
# target_power1 = 2.
# central_frequency1 =  193450000 # [MHz] 193450000
# 
# sleep_counter = tf.change_configuration(line_port=line_port1, logical_interface=logical_interface1,
#                         modulation=modulation1, target_power=target_power1,
#                         central_frequency=central_frequency1)
# 
# tf.set_interface_on(line_port1)
# 
# pm_data = tf.read_pm_data(sleep_counter, line_port1, DEBUG=True)
# 
# print(pm_data)

line_port2 = '1/2/n1'

logical_interface2 = 'ot100'
modulation2 = 'dp-qpsk'
target_power2 = 1.
central_frequency2 =  194950000  # [MHz] 193825000

sleep_counter = tf.change_configuration(line_port=line_port2, logical_interface=logical_interface2,
                        modulation=modulation2, target_power=target_power2,
                        central_frequency=central_frequency2)

tf.set_interface_on(line_port2)

pm_data = tf.read_pm_data(sleep_counter, line_port2, DEBUG=True)


print(pm_data)
print('###')