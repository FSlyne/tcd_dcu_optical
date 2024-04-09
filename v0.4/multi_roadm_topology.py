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



fibre = 'DCU_link_1'
fibre = 'Reel_Corning_25220'
fibre = 'Reel_Alcatel_10633'

AWSS_p1 = 'AWSS_p1' # 3
AWSS_p2 = 'AWSS_p2' # 1
ASignal = 'ARoF' # 2



line1 = 'AWSS_p2' # 1
line3 = 'AWSS_p1' # 3
line2 = 'ARoF' # 2

# 2023-04-04 16:10

patch_list_coherent = [
('ADVA_2_TF1_p1', 'Reel_Alcatel_10633', 'ADVA_2_TF1_p1')
]


# 2023-04-04 15:14

patch_list_Ay_2_DCU = [
('ADVA_2_TF1_p1', line2, 'ADVA_2_TF1_p1'),
(line3,'Reel_Alcatel_10633',line3),
(line1, 'DCU_link_1')
]

patch_list_Ay_3_DCU = [
('ADVA_2_TF1_p1', line2, 'ADVA_2_TF1_p1'),

(line3, 'Reel_Alcatel_10633' ,'Lumentum_3_p1', 'Reel_Corning_12646', line3),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_3_line'),
(line1, 'DCU_link_1')

]

patch_list_Ay_4_DCU = [
('ADVA_2_TF1_p1', line2, 'ADVA_2_TF1_p1'),

(line3, 'Reel_Alcatel_10633' ,'Lumentum_3_p1', 'Reel_Corning_12646', line3),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_4_line'),
('Lumentum_4_p1', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Lycom_25028', 'Lumentum_3_line'),
(line1, 'DCU_link_1')

]

# 2023-03-20    
# 

patch_list_Ay_4 = [
('ADVA_2_TF1_p1', line2, 'ADVA_2_TF1_p1'),

(line3, 'Reel_Alcatel_10633' ,'Lumentum_3_p1', 'Reel_Corning_12646', line3),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_4_line'),
('Lumentum_4_p1', 'Lumentum_4_p1'),
('Lumentum_4_line', 'Reel_Lycom_25028', 'Lumentum_3_line')

]

# 2023-03-15
# 

patch_list_Ay_3 = [
('ADVA_2_TF1_p1', line2, 'ADVA_2_TF1_p1'),

(line3, 'Reel_Alcatel_10633' ,'Lumentum_3_p1', 'Reel_Corning_12646', line3),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_3_line')

]


# 2023-02-28 10:53

patch_list_Ay_2 = [
('ADVA_2_TF1_p1', line2, 'ADVA_2_TF1_p1'),

(line3,'Reel_Alcatel_10633',line3)
]


# 2023-02-27

patch_list_Az = [
('ADVA_2_TF1_p1', 'splitter_3_p1'),
(ASignal, 'splitter_3_p2'),
(AWSS_p2, ASignal),
(AWSS_p1, 'ADVA_2_TF1_p1'),

# ('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Reel_Alcatel_10633', AWSS_p1)
('splitter_3_p1', fibre, AWSS_p1)
]

# 2023-02-20

patch_list_Ax = [
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),

('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'AWSS_p1', 'ADVA_1_8PSM_line')
]

fibre3 = 'AWSS_p1'
fibre2 = 'ARoF'

patch_list_Ay = [
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),

('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', fibre3, 'ADVA_1_8PSM_line'),

(fibre2,'Reel_Alcatel_10633',fibre2)
]

patch_list_A = [
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),


('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Lumentum_3_p1'),

('Lumentum_3_line',  fibre, 'Lumentum_3_line'),

('Lumentum_3_p1', 'ADVA_1_8PSM_line')
]

patch_list_B = [
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),


('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Lumentum_3_p1'),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_4_line'),

('Lumentum_4_p1', 'Lumentum_6_p1'),

('Lumentum_6_line', fibre, 'Lumentum_6_line'),
 
('Lumentum_6_p1', 'Lumentum_4_p1'),

('Lumentum_4_line',  'Reel_Corning_25255a', 'Lumentum_3_line'),

('Lumentum_3_p1', 'ADVA_1_8PSM_line'),

('ADVA_1_8PSM_p6','OSA_MS9710C_1')
]

patch_list_Bx = [ # B
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),


('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Lumentum_3_p1'),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_4_line'),

('Lumentum_4_p1', 'Lumentum_6_p1'),

('Lumentum_6_line', fibre, 'Lumentum_3_line'),

('ADVA_1_8PSM_p6','OSA_MS9710C_1')
]

patch_list_B_R2fail = [
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),


('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Lumentum_3_p1'),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_1_line'),

('Lumentum_1_p1', 'Lumentum_2_p1'),

('Lumentum_2_line', fibre, 'Lumentum_2_line'),
 
('Lumentum_2_p1', 'Lumentum_1_p1'),

('Lumentum_1_line',  'Reel_Corning_25255a', 'Lumentum_3_line'),

('Lumentum_3_p1', 'ADVA_1_8PSM_line'),

('ADVA_1_8PSM_p6','OSA_MS9710C_1')
]


patch_list_B_R2fail = [
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),


('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Lumentum_3_p1'),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_1_line'),

('Lumentum_1_p1', 'Lumentum_2_p1'),

('Lumentum_2_line', fibre, 'Lumentum_2_line'),
 
('Lumentum_2_p1', 'Lumentum_1_p1'),

('Lumentum_1_line',  'Reel_Corning_25255a', 'Lumentum_3_line'),

('Lumentum_3_p1', 'ADVA_1_8PSM_line'),

('ADVA_1_8PSM_p6','OSA_MS9710C_1')
]


patch_list_C = [
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),


('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Lumentum_3_p1'),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_7_line'),
('Lumentum_7_p1', 'Lumentum_5_p1'),

('Lumentum_5_line', 'Reel_Lycom_25028', 'Lumentum_4_line'),

('Lumentum_4_p1', 'Lumentum_6_p1'),

('Lumentum_6_line', fibre, 'Lumentum_6_line'),
 
('Lumentum_6_p1', 'Lumentum_4_p1'),

('Lumentum_4_line',  'Reel_Corning_25255a',   'Lumentum_5_line'),

('Lumentum_5_p1', 'Lumentum_7_p1'),

('Lumentum_7_line', 'Reel_Corning_25220', 'Lumentum_3_line'),

('Lumentum_3_p1', 'ADVA_1_8PSM_line'),

('ADVA_1_8PSM_p6','OSA_MS9710C_1')
]

patch_list_Cx = [  #C
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),


('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Lumentum_3_p1'),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_7_line'),
('Lumentum_7_p1', 'Lumentum_5_p1'),

('Lumentum_5_line', 'Reel_Lycom_25028', 'Lumentum_4_line'),

('Lumentum_4_p1', 'Lumentum_6_p1'),

('Lumentum_6_line', fibre, 'Lumentum_3_line'),

('Lumentum_3_p1', 'ADVA_1_8PSM_line'),

('ADVA_1_8PSM_p6','OSA_MS9710C_1')
]

patch_list_Cy = [ #D
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),


('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Lumentum_3_p1'),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_7_line'),
('Lumentum_7_p1', 'Lumentum_5_p1'),

('Lumentum_5_line', 'Reel_Lycom_25028', 'Lumentum_4_line'),

('Lumentum_4_p1', 'Lumentum_4_p1'),

('Lumentum_4_line',  'Reel_Corning_25255a',   'Lumentum_5_line'),

('Lumentum_5_p1', 'Lumentum_6_p1'),

('Lumentum_6_line', fibre, 'Lumentum_3_line'),

('Lumentum_3_p1', 'ADVA_1_8PSM_line'),

('ADVA_1_8PSM_p6','OSA_MS9710C_1')
]

patch_list_D = [
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),


('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Lumentum_3_p1'),

('Lumentum_3_line', 'Reel_Lycom_25043', 'Lumentum_7_line'),
('Lumentum_7_p1', 'Lumentum_5_p1'),

('Lumentum_5_line', 'Reel_Lycom_25028', 'Lumentum_1_line'),
('Lumentum_1_p1', 'Lumentum_2_p1'),

('Lumentum_2_line', 'Reel_Alcatel_25332', 'Lumentum_4_line'),

('Lumentum_4_p1', 'Lumentum_6_p1'),

('Lumentum_6_line', fibre, 'Lumentum_6_line'),
 
('Lumentum_6_p1', 'Lumentum_4_p1'),

('Lumentum_4_line',  'Reel_Corning_25255a',   'Lumentum_2_line'),
('Lumentum_2_p1', 'Lumentum_1_p1'),

('Lumentum_1_line',  'Reel_Corning_25237',   'Lumentum_5_line'),

('Lumentum_5_p1', 'Lumentum_7_p1'),

('Lumentum_7_line', 'Reel_Corning_25220', 'Lumentum_3_line'),

('Lumentum_3_p1', 'ADVA_1_8PSM_line'),

('ADVA_1_8PSM_p6','OSA_MS9710C_1')
]

patch_list_with_comb = [
('Lumentum_3_p2','Lumentum_3_p2'),
('ADVA_1_TF1_p1', 'NULL'),
('ADVA_1_TF1_p2', 'NULL'),
('ADVA_2_TF1_p1', 'ADVA_1_8PSM_p1', 'ADVA_2_TF1_p1'),
('ADVA_2_TF1_p2', 'NULL'),


('ADVA_1_8PSM_line', 'ADVA_1_D20', 'ADVA_1_voa2', 'Lumentum_3_p1'),

('Lumentum_3_line',  fibre, 'Lumentum_3_line'),

('Lumentum_3_p1', 'ADVA_1_8PSM_line'),

('Lumentum_1_p1', 'Lumentum_2_p1'),
('Lumentum_2_line', 'ADVA_1_voa1', 'ADVA_1_8PSM_p5'),

('Laser_N7711A_1', 'Reel_Lycom_27066','Lumentum_2_line'),

('ADVA_1_8PSM_p6','OSA_MS9710C_1')
]

patch_list=patch_list_Ay_2_DCU


if option == 0:
#    plts.clearallconn()
    plts.apply_patch_list2(patch_list)
else:
    plts.get_patch_list_power(patch_list)
