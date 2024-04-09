import sys
import time
from tcdona2.polatis3 import *
from tcdona2.lumentum2 import *
import random
import time

iterations=1
samples=5
settle_time=10

roadm1=Lumentum('10.10.10.38')
roadm2=Lumentum('10.10.10.37')

channel_list=list(range(1,96))
channel_list=(30,50,60,70)

roadm1.make_grid(open_channels=channel_list)
#time.sleep(10)
#power=roadm1.get_demux_connection_input_power()
#power2=flatten(power)
#power2 = [0] * 96
#print(power2)
#roadm1.set_demux_atten(power2)

roadm2.make_grid(open_channels=channel_list)



