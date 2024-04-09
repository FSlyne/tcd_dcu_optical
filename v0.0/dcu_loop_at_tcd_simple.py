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
#         ('DCU_link_1','Splitter_1_p1','DCU_link_1'), # 
#         ('Splitter_1_p2','OSA_MS9710C_1')
# ]

patch_list = [
        ('DCU_link_1','Lumentum_3_line'),
        ('Lumentum_3_line','Splitter_1_p1','DCU_link_1'),
        ('Splitter_1_p2','OSA_MS9710C_1'),
        ('Lumentum_3_p1', 'Lumentum_3_p1')
]
# 
# patch_list = [
#         ('DCU_link_1','Lumentum_3_line'),
#         ('Lumentum_3_line','DCU_link_1'),
#         ('Lumentum_3_p1', 'Lumentum_3_p1')
# ]


if option == 0:
    print("No Clear, Patching ...")
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
