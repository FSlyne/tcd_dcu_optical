
import json

from tcdona2.lumentum2 import *
from time import *

roadm4=Lumentum('10.10.10.32')

channel_list=list(range(1,96))
print(channel_list)
roadm4.set_mux_atten(channel_list, 6.0)
