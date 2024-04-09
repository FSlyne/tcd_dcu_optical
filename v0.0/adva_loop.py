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



# fibre = 'DCU_link_1'
fibre = 'Reel_Corning_25220'


patch_list = [
('Lumentum_3_line', 'ADVA_1_8PSM_p1'),
('ADVA_1_TF1_p1', 'ADVA_D20', 'ADVA_1_8PSM_p2'),
('ADVA_1_8PSM_line', fibre),
(fibre, 'Lumentum_3_line')
]

patch_list = [
('Lumentum_3_line', 'Splitter_1_p1', fibre,   'Lumentum_3_line'),
('Splitter_1_p2', 'Reel_Lycom_27066', 'OSA_MS9710C_1'),
]

patch_list = [ # works
('ADVA_1_TF1_p2', 'ADVA_1_8PSM_p1', 'ADVA_1_TF1_p2'),
('ADVA_1_8PSM_line', 'Splitter_1_p1', 'ADVA_1_8PSM_line'),
('Splitter_1_p2',  'OSA_MS9710C_1')
]

patch_list = [ # works
('ADVA_1_TF1_p2', 'Lumentum_3_p1', 'ADVA_1_TF1_p2'),
('Lumentum_3_line', 'Reel_Lycom_27066', 'Lumentum_3_line')
]

# 'Reel_Lycom_27066'

patch_list = [
('Lumentum_3_line', 'Splitter_1_p1', fibre,   'Lumentum_3_line'),
('Splitter_1_p2', 'Reel_Lycom_27066', 'OSA_MS9710C_1'),
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_2_TF1_p1','Lumentum_3_p1', 'ADVA_2_TF1_p1' )
]




if option == 0:
#    plts.clearallconn()
    plts.apply_patch_list(patch_list)
else:
    plts.get_patch_list_power(patch_list)