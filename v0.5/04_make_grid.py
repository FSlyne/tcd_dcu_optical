import json

from tcdona2.lumentum2 import *

roadm4=Lumentum('10.10.10.32')

channel_list=list(range(1,96))
channel_list=[52,53,54]

roadm4.make_grid(open_channels=channel_list)

roadm4.set_mux_constant_gain(15.0)
roadm4.set_demux_constant_gain(10.0)

roadm4.set_mux_online()
roadm4.set_demux_online()
