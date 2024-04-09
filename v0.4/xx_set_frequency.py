from tflex_params import *
import time
from time import sleep
import xmltodict
import numpy as np

tf = tflex("10.10.10.92")

# Read out available line_ports
config = tf.return_current_config()
line_ports = config.keys()
print(line_ports)

line_port2 = '1/2/n1'

logical_interface2 = 'ot100'
modulation2 = 'dp-qpsk'
target_power2 = .5
central_frequency2 =  194950000  # [MHz] 193825000 # 194950000

tf.set_interface_off(line_port2)
tf.set_admin_maintenance(line_port2 + '/' + logical_interface2)
tf.set_y()
tf.set_optical_power()
# sleep_counter = tf.change_configuration(line_port=line_port2, logical_interface=logical_interface2,
#                         modulation=modulation2, target_power=target_power2,
#                          central_frequency=central_frequency2)
# 
# pm_data = tf.read_pm_data(sleep_counter, line_port2, DEBUG=True)
tf.remove_admin_maintenance(line_port2 + '/' + logical_interface2)
print(tf.get_power_and_frequency(line_port2))
tf.set_interface_on(line_port2)

#print(pm_data)

print(tf.get_y())
print('###')