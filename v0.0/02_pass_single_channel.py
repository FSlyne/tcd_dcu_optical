import json

from tcdona2.lumentum2 import *

roadm3=Lumentum('10.10.10.33')

channel_list=list(range(1,96))

roadm3.make_grid()


roadm3.set_mux_unblock([44])
roadm3.set_demux_unblock([44])

roadm3.set_mux_constant_gain(15.0)
roadm3.set_demux_constant_gain(10.0)
