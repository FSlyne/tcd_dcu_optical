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

patch_list1 = [
('BB_source', 'Lumentum_7_p1'),
('Lumentum_7_line', 'Reel_Lycom_25043', 'Lumentum_7_line' ),
('Lumentum_7_p1', 'OSA_MS9710C_1')
]

patch_list2a = [
('fibre_03', 'ADVA_1_8PSM_p1', 'OSA_MS9710C_1'),
('ADVA_1_TF1_p2', 'ADVA_1_8PSM_p2', 'ADVA_1_TF1_p2'),
('ADVA_1_8PSM_line','ADVA_1_8PSM_line')
]

patch_list2b = [
('fibre_03', 'ADVA_1_8PSM_p1', 'fibre_03'),
('ADVA_1_TF1_p2', 'ADVA_1_8PSM_p2', 'ADVA_1_TF1_p2'),
('ADVA_1_8PSM_line','ADVA_1_8PSM_line')
]

patch_list2b = [
('fibre_03', 'ADVA_1_8PSM_p1', 'fibre_03'),
('ADVA_1_TF1_p2', 'ADVA_1_8PSM_p2', 'ADVA_1_TF1_p2'),
('ADVA_1_8PSM_line','ADVA_1_D20', 'ADVA_1_8PSM_line')
]

patch_list3 = [
('fibre_03', 'ADVA_1_8PSM_p1', 'fibre_03'),
('ADVA_1_TF1_p1', 'ADVA_1_8PSM_p2', 'ADVA_1_TF1_p1'),
('ADVA_1_8PSM_line','ADVA_1_D20', 'Lumentum_7_p1'),
('Lumentum_7_line', 'Reel_Lycom_25043', 'Lumentum_7_line'),
('Lumentum_7_p1', 'ADVA_1_8PSM_line')
]

patch_list4 = [
('fibre_03', 'splitter_3_p1'),
('ADVA_1_TF1_p1', 'splitter_3_p2'),
('splitter_3_p1', 'Lumentum_7_p1'),
('Lumentum_7_line', 'Reel_Lycom_25043', 'Lumentum_7_line'),
('Lumentum_7_p1', 'splitter_4_p1'),
('splitter_4_p1','ADVA_1_TF1_p1'),
('splitter_4_p2', 'fibre_03')
]



patch_list = patch_list4

if option == 0:
#    plts.clearallconn()
    plts.apply_patch_list2(patch_list)
else:
    plts.get_patch_list_power(patch_list)
