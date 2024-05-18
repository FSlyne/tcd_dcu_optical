import json

from tcdona2.lumentum2 import *

roadm1=Lumentum('10.10.10.38')

foreground_channels=list(range(1,96))
# ase_noise_channels=[1,11,21,31,41,45,48,56,60,65,70,75,80,85,90]

roadm1.make_grid(open_channels=foreground_channels)
roadm1.set_demux_port(foreground_channels,1)
roadm1.set_demux_unblock(foreground_channels)
