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
('BB_source', 'Lumentum_3_line'),
('Lumentum_3_p1', 'Lumentum_3_p1'),
('Lumentum_3_line', 'Reel_Corning_12646', 'Lumentum_4_line' ),
]

patch_list2 = [
('BB_source', 'Lumentum_3_line'),
('Lumentum_3_p1', 'Lumentum_3_p1'),
('Lumentum_3_line', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Corning_12646', 'Lumentum_4_line' ),
]

# 2024-04-20 - 2024-05-30
patch_list3 = [
('BB_source', 'Lumentum_3_line'),
('Lumentum_3_p1', 'Lumentum_3_p1'),
('Lumentum_3_line', 'Lumentum_5_p1'),
('Lumentum_5_line','Reel_Corning_25220', 'Lumentum_5_line' ),
('Lumentum_5_p1', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Corning_12646', 'Lumentum_4_line' ),
('Lumentum_4_p1', 'OSA_MS9710C_1')
]


patch_list4 = [
('BB_source', 'Lumentum_3_line'),
('Lumentum_3_p1', 'Lumentum_3_p1'),
('Lumentum_3_line', 'Reel_Alcatel_10848', 'Lumentum_6_line'),
# short path
('Lumentum_6_p1', 'Lumentum_1_p1'),
('Lumentum_1_line', 'Reel_Alcatel_11895', 'Lumentum_1_line' ),
# long path
('Lumentum_6_p2', 'Lumentum_5_p1'),
('Lumentum_5_line','Reel_Corning_25220', 'Lumentum_5_line' ),
('Lumentum_5_p1', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Corning_12646', 'Lumentum_4_line' ),
('Lumentum_4_p1', 'OSA_MS9710C_1')
]

patch_list5 = [
('BB_source', 'Lumentum_3_line'),
('Lumentum_3_p1', 'Lumentum_3_p1'),
('Lumentum_3_line', 'Reel_Alcatel_10848', 'Lumentum_6_line'),
# short path
('Lumentum_6_p1', 'Lumentum_1_p1'),
('Lumentum_1_line', 'Reel_Alcatel_11895', 'Lumentum_1_line' ),
# long path
('Lumentum_6_p2', 'Lumentum_5_p1'),
('Lumentum_5_line','Reel_Corning_25220', 'Lumentum_5_line' ),
('Lumentum_5_p1', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Corning_12646', 'Lumentum_4_line' ),
('Lumentum_4_p1', 'OSA_MS9710C_1'),
# teraflex
('ADVA_1_TF1_p2', 'Lumentum_3_p2'),
('ADVA_2_TF1_p1', 'Lumentum_3_p3'),
('Lumentum_4_p2','Splitter_2_p1'),
('Lumentum_1_p2','Splitter_2_p2'),
('Splitter_2_p1', 'ADVA_1_TF1_p2'),
('Splitter_2_p2', 'ADVA_2_TF1_p1')
]

# Reel_Corning_50441
# Reel_Corning_50450
# Reel_Corning_50458a
# Reel_Corning_50168

# Reel_Lycom_27066
# Reel_Corning_25220
# Reel_Lycom_25043
# Reel_Lycom_25028

# Reel_Alcatel_10848
# Reel_Alcatel_11895
# Reel_Corning_12646


patch_list6 = [
('BB_source', 'Lumentum_3_line'),
('Lumentum_3_p1', 'Lumentum_3_p1'),
('Lumentum_3_line', 'Reel_Corning_50438', 'Lumentum_6_line'),
# short path
('Lumentum_6_p1', 'Lumentum_1_p1'),
('Lumentum_1_line', 'Reel_Corning_39845', 'Reel_Alcatel_10848','Lumentum_1_line' ),
# long path
('Lumentum_1_p1', 'Lumentum_5_p1'),
('Lumentum_5_line','Reel_Lycom_27066', 'Reel_Corning_25220','Lumentum_5_line' ),
('Lumentum_5_p1', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Lycom_25043', 'Reel_Lycom_25028', 'Lumentum_4_line' ),
# teraflex
('ADVA_1_TF1_p2', 'Lumentum_3_p2'),
('ADVA_2_TF1_p1', 'Lumentum_3_p3'),
('Lumentum_4_p2', 'ADVA_1_TF1_p2'),
('Lumentum_4_p3', 'ADVA_2_TF1_p1')
]


patch_list = patch_list6

if option == 0:
#    plts.clearallconn()
    plts.apply_patch_list2(patch_list)
else:
    plts.get_patch_list_power(patch_list)