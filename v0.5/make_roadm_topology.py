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


patch_list = [
('BB_source', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Lycom_25043', 'Lumentum_4_line' ),
('Lumentum_4_p1', 'OSA_MS9710C_1')
]


if option == 0:
#    plts.clearallconn()
    plts.apply_patch_list2(patch_list)
else:
    plts.get_patch_list_power(patch_list)
