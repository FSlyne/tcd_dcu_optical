import json

from tcdona2.lumentum2 import *

roadm6=Lumentum('10.10.10.30')

foreground_channels=list(range(1,96))
# ase_noise_channels=[1,11,21,31,41,45,48,56,60,65,70,75,80,85,90]

roadm6.set_demux_port(foreground_channels,1)
