import sys
import time
from tcdona2.polatis3 import *

option=1
if len(sys.argv) == 1:
    option=1
else:
    option=0

# Setting up Polatis
print ("Setting up the Polatis ...")
plts = Polatis('10.10.10.28','3082')
plts.login()

# patch_list = [
#         ('Lumentum_3_line', 'DCU_link_1','Splitter_1_p1','Lumentum_3_line'), # 
#         ('Splitter_1_p2','OSA_MS9710C_1'),
#         ('Lumentum_3_p1','Lumentum_3_p1'),
#         ('Lumentum_1_p1', 'Lumentum_2_p1'), # noise generation
# #        ('Lumentum_2_line','Lumentum_3_p2'), # 
#         ('Laser_N7711A_1', 'Lumentum_2_line'), # inject laser into Lumentum line
# ]

patch_list = [
        ('Laser_N7711A_1', 'Lumentum_2_line'), # inject laser into Lumentum line
        ('Lumentum_1_p1', 'Lumentum_2_p1'),
         ('Lumentum_2_line','Splitter_1_p1','DCU_link_1'), # noise generation
        ('Splitter_1_p2','OSA_MS9710C_1'),
#        ('Lumentum_2_line','Lumentum_3_p2'), # 
]

if option == 0:
    plts.clearallconn()
    print("Patching ...")
    for patch in patch_list:
        plts.patching2(*patch)
    time.sleep(3)
    print("Monitoring ...")
    for patch in patch_list:
        plts.get_patch_power(*patch)
    time.sleep(3)
else:
    print("Monitoring ...")
    for patch in patch_list:
        plts.get_patch_power(*patch)

