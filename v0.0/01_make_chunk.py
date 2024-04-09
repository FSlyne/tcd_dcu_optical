import json

from tcdona2.lumentum2 import *

roadm3=Lumentum('10.10.10.33')

roadm3.make_one_wide_channel_mux()
roadm3.make_one_wide_channel_demux()

roadm3.set_mux_unblock([1])
roadm3.set_demux_unblock([1])

roadm3.set_mux_constant_gain(10.0)
roadm3.set_demux_constant_gain(10.0)



