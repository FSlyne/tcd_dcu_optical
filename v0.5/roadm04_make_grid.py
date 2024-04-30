import json

from tcdona2.lumentum2 import *

roadm4=Lumentum('10.10.10.32')

ase_noise_channels=list(range(1,96))
# ase_noise_channels=[1,11,21,31,41,45,48,56,60,65,70,75,80,85,90]
tf_channel=52
arof1=53
arof2=54

foreground_channels=[tf_channel, arof1, arof2]

roadm4.make_grid(open_channels=foreground_channels)
roadm4.set_mux_port(ase_noise_channels,4)
roadm4.set_mux_unblock(ase_noise_channels)
roadm4.set_demux_unblock(ase_noise_channels)

sleep(5)
power=roadm4.get_demux_connection_input_power()

roadm4.set_demux_offline()
flatten_value = get_flatten_value(power)
power4=flatten(power)
print(power4)
roadm4.set_demux_atten(power3)
roadm4.set_demux_online()
sleep(5)

roadm4.set_mux_constant_gain(15.0)
roadm4.set_demux_constant_gain(10.0)

roadm4.set_mux_online()
roadm4.set_demux_online()
