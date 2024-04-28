import json

from tcdona2.lumentum2 import *

roadm3=Lumentum('10.10.10.33')

channel_list=list(range(1,96))
channel_list=[1,11,21,31,41,45,48,56,60,65,70,75,80,85,90]

roadm3.make_grid(open_channels=channel_list)

roadm3.set_demux_constant_gain(10.0)

roadm3.set_demux_online()
