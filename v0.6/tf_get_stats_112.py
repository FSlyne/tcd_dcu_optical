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

sleep_counter=5

line_port2 = '1/1/n2'


#print(tf.get_power_and_frequency(line_port2))

#print(tf.get_y())

perf_dict = tf.read_pm_data(sleep_counter, line_port2, DEBUG=True)

print(perf_dict)

print("Optical Receive Power, Q-Factor, SNR, OSNR, FEC ber")
print(perf_dict['CarrierTF_indefinite_opt-rcv-pwr'],
perf_dict['QualityTF_indefinite_q-factor'],
perf_dict['QualityTF200g16Q_indefinite_signal-to-noise-ratio'],
perf_dict['QualityTF200g16Q_indefinite_optical-signal-to-noise-ratio'],
# '{:.2e}'.format(float( perf_dict['FEC:indefinite:fec-ber'])),
# perf_dict['FEC:15min:fec-uncorrected-blocks']
)


#params = tf.get_params(line_port2)
#print(params)

#print('###')
# QualityTF100gQ 
