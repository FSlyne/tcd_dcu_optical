import json

from tcdona2.lumentum2 import *
from time import *

roadm2=Lumentum('10.10.10.37')

foreground_channels=list(range(1,96))

roadm2.make_grid(open_channels=foreground_channels)
sleep(5)

roadm2.set_demux_port([3],2)

roadm2.set_mux_online()
roadm2.set_demux_online()
roadm2.set_mux_constant_gain(15.0)
roadm2.set_demux_constant_gain(10.0)
roadm2.set_mux_online()
roadm2.set_demux_online()
