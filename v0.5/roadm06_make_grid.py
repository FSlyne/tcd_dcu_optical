import json

from tcdona2.lumentum2 import *
from time import *

roadm6=Lumentum('10.10.10.30')

foreground_channels=list(range(1,96))

roadm6.make_grid(open_channels=foreground_channels)
sleep(5)

roadm6.set_demux_port([3],2)

roadm6.set_mux_online()
roadm6.set_demux_online()
roadm6.set_mux_constant_gain(15.0)
roadm6.set_demux_constant_gain(10.0)
roadm6.set_mux_online()
roadm6.set_demux_online()
