import json

from tcdona2.lumentum2 import *
from time import *

roadm3=Lumentum('10.10.10.33')

channel_list=list(range(1,96))
# channel_list=[1,11,21,31,41,45,48,56,60,65,70,75,80,85,90]

# roadm3.make_grid(open_channels=channel_list, channel_width=37.5)

comb_opt=2

if comb_opt == 1: 
    sleep(5)
    power=roadm3.get_demux_connection_input_power()
    power3=flatten(power)
    roadm3.set_demux_offline()
    roadm3.set_demux_atten(power3)
#    roadm3.set_demux_constant_gain(10.0)
    roadm3.set_demux_online()
else:
    sleep(5)
    power=roadm3.get_demux_connection_input_power()
    power3=flatten(power)
    print(power3)
    roadm3.set_demux_offline()
    roadm3.set_demux_atten(power3)
#    roadm3.set_demux_constant_gain(10.0)
    roadm3.set_demux_online()
    power=roadm3.get_mux_monitored_power()
    power3=flatten(power)
    print(power3)
    roadm3.set_mux_offline()
    roadm3.set_mux_atten(power3)
#    roadm3.set_mux_constant_gain(10.0)
    roadm3.set_mux_online()