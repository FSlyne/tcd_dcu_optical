import json

from tcdona2.lumentum2 import *

roadm_ip_list=['10.10.10.33', '10.10.10.32'] # roadm3

# centre 194950 Ghz
chunk_50ghz=[
('194925.00', '194975.00', 1), # coherent
]

chunk_62_5ghz =[
('194918.75', '194981.25', 1), # coherent
]

chunk_87_5ghz =[
('194906.3', '194993.8', 1), # coherent
]

chunk_100ghz =[
('194900.0', '195000.0', 1), # coherent
]

chunk = chunk_50ghz

roadm_list=[]
for roadm_ip in roadm_ip_list:
    roadm=Lumentum(roadm_ip)
    roadm.wss_delete_connection(1,'all')
    roadm.wss_delete_connection(2,'all')
    roadm.make_channel_chunk_demux(chunk)
    roadm.make_channel_chunk_mux(chunk)
    
    #roadm.set_mux_offline()
    #roadm.set_demux_offline()
    
    #roadm.set_mux_high_gain_mode()
    #roadm.set_demux_high_gain_mode()
    
    #roadm.set_mux_constant_gain(5)
    #roadm.set_demux_constant_gain(15)
    
    #roadm.set_mux_online()
    #roadm.set_demux_online()
    
    roadm_list.append(roadm)

# channel_list=list(range(1,96))
# roadm3.make_grid(open_channels=channel_list)
# roadm3.set_mux_online()
# roadm3.set_demux_online()
# 
# exit()
