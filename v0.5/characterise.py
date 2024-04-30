import json

from tcdona2.lumentum2 import *

roadm3=Lumentum('10.10.10.33')
roadm4=Lumentum('10.10.10.32')
roadm5=Lumentum('10.10.10.31')
roadm6=Lumentum('10.10.10.30')
channel_list=list(range(1,96))

roadm4.make_grid(open_channels=channel_list)
roadm5.make_grid(open_channels=channel_list)
roadm6.make_grid(open_channels=channel_list)

tx_power=roadm3.get_mux_connection_output_power()
tx_power2 = roadm3.get_mux_monitored_power()
rcv_power=roadm4.get_demux_connection_input_power()

c=[(a[0],b[0],a[1], b[1], round(b[1]- a[1],2)) for a,b in zip(tx_power,rcv_power)]

print(c)

c=[(a[0],b[0],a[1], b[1], round(b[1]- a[1],2)) for a,b in zip(tx_power2,rcv_power)]

print(c)

# roadm4.set_demux_offline()
# flatten_value = get_flatten_value(power)
# power4=flatten(power)
# print(power4)
# roadm4.set_demux_atten(power3)
# roadm4.set_demux_online()
# sleep(5)
# 
# roadm4.set_mux_offline()
# roadm4.set_mux_constant_gain(10.0)
# roadm4.set_mux_online()

