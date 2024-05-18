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

line_port2 = '1/1/n2'

logical_interface2 = 'ot100'
modulation2 = 'dp-qpsk'
target_power2 = .6
central_frequency2 =  191450000  # [MHz] 193825000 # 194950000

tf.set_interface_off(line_port2)
sleep_counter = tf.change_configuration(line_port=line_port2, logical_interface=logical_interface2,
                        modulation=modulation2, target_power=target_power2,
                        central_frequency=central_frequency2)

tf.set_interface_on(line_port2)


perf_dict = tf.read_pm_data(sleep_counter, line_port2, DEBUG=True)

print("Optical Receive Power, Q-Factor, SNR, OSNR, FEC ber")
print(perf_dict['CarrierTF_indefinite_opt-rcv-pwr'],
perf_dict['QualityTF_indefinite_q-factor'],
perf_dict['QualityTF100gQpsk_indefinite_signal-to-noise-ratio'],
perf_dict['QualityTF100gQpsk_indefinite_optical-signal-to-noise-ratio'],
'{:.2e}'.format(float( perf_dict['FEC:indefinite:fec-ber'])),
perf_dict['FEC:15min:fec-uncorrected-blocks'])


params = tf.get_params(line_port2)
print(params)