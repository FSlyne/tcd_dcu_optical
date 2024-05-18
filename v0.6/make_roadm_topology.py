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
('ADVA_1_TF1_p2', 'Lumentum_4_p1', 'ADVA_1_TF1_p2'),
# ('fibre_03', 'Lumentum_4_p2', 'fibre_03'),
('Lumentum_4_line', 'Reel_Corning_12646', 'Lumentum_4_line' ),
('BB_source', 'Lumentum_3_line'),
# ('Lumentum_3_p1', 'OSA_MS9710C_1')
#('Lumentum_3_p1','Lumentum_3_p1'),
#('Lumentum_3_line', 'Lumentum_4_p4')
('Lumentum_3_p1','Lumentum_4_p4'),
]

patch_list2 = [
('ADVA_1_TF1_p2', 'Lumentum_4_p1', 'ADVA_1_TF1_p2'),
# ('fibre_03', 'Lumentum_4_p2', 'fibre_03'),
('Lumentum_4_line', 'Reel_Corning_12646','Lumentum_5_line'),
('Lumentum_5_p1', 'Lumentum_5_p1'),
('Lumentum_5_line','Reel_Lycom_25043','Lumentum_4_line'),
('BB_source', 'Lumentum_3_line'),
# ('Lumentum_3_p1', 'OSA_MS9710C_1')
#('Lumentum_3_p1','Lumentum_3_p1'),
#('Lumentum_3_line', 'Lumentum_4_p4')
('Lumentum_3_p1','Lumentum_4_p4'),
]

patch_list3 = [
('ADVA_1_TF1_p2', 'Lumentum_4_p1', 'ADVA_1_TF1_p2'),
# ('fibre_03', 'Lumentum_4_p2', 'fibre_03'),
('Lumentum_4_line', 'Reel_Corning_12646','Lumentum_5_line'),
('Lumentum_5_p1', 'Lumentum_5_p1'),
('Lumentum_5_line','Reel_Lycom_25043','Lumentum_6_line'),
('Lumentum_6_p1', 'Lumentum_6_p1'),
('Lumentum_6_line', 'Reel_Lycom_25028', 'Lumentum_4_line'),
('BB_source', 'Lumentum_3_line'),
# ('Lumentum_3_p1', 'OSA_MS9710C_1')
#('Lumentum_3_p1','Lumentum_3_p1'),
#('Lumentum_3_line', 'Lumentum_4_p4')
('Lumentum_3_p1','Lumentum_4_p4'),
]

patch_list4 = [
('ADVA_1_TF1_p2', 'Lumentum_4_p1', 'ADVA_1_TF1_p2'),
# ('fibre_03', 'Lumentum_4_p2', 'fibre_03'),
('Lumentum_4_line', 'Reel_Corning_12646','Lumentum_5_line'),
('Lumentum_5_p1', 'Lumentum_5_p1'),
('Lumentum_5_line','Reel_Lycom_25043','Lumentum_6_line'),
('Lumentum_6_p1', 'Lumentum_6_p1'),
('Lumentum_6_line', 'Reel_Lycom_25028','Lumentum_1_line'),
('Lumentum_1_p1', 'Lumentum_1_p1'),
('Lumentum_1_line', 'Reel_Corning_25220','Lumentum_4_line'),
('BB_source', 'Lumentum_3_line'),
# ('Lumentum_3_p1', 'OSA_MS9710C_1')
#('Lumentum_3_p1','Lumentum_3_p1'),
#('Lumentum_3_line', 'Lumentum_4_p4')
('Lumentum_3_p1','Lumentum_4_p4'),
]


patch_list2 = [
('BB_source', 'Lumentum_3_p1'),
('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_3_line' ),
('Lumentum_3_p1', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Lycom_25028', 'Lumentum_4_line' ),
('Lumentum_4_p1', 'OSA_MS9710C_1')
]

patch_list3 = [
('BB_source', 'Lumentum_3_p1'),
('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_3_line' ),
('Lumentum_3_p1', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Lycom_25028', 'Lumentum_4_line' ),
('Lumentum_4_p1', 'Lumentum_5_p1'),
('Lumentum_5_line', 'Reel_Corning_25255a', 'Lumentum_5_line' ),
('Lumentum_5_p1', 'OSA_MS9710C_1')
]

patch_list4 = [
('BB_source', 'Lumentum_3_p1'),
('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_3_line' ),
('Lumentum_3_p1', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Lycom_25028', 'Lumentum_4_line' ),
('Lumentum_4_p1', 'Lumentum_5_p1'),
('Lumentum_5_line', 'Reel_Corning_25255a', 'Lumentum_5_line' ),
('Lumentum_5_p1', 'Lumentum_6_p1'),
('Lumentum_6_line', 'Reel_Corning_25220', 'Lumentum_6_line' ),
('Lumentum_6_p1', 'OSA_MS9710C_1')
]

patch_list = patch_list1

if option == 0:
#    plts.clearallconn()
    plts.apply_patch_list2(patch_list)
else:
    plts.get_patch_list_power(patch_list)
