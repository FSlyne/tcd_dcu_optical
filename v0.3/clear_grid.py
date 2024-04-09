import json

from tcdona2.lumentum2 import *

roadm_ip_list=['10.10.10.29', '10.10.10.30',
               '10.10.10.31', '10.10.10.32',
               '10.10.10.37', '10.10.10.38'] # roadm7, roadm6, roadm5, roadm4, roadm2, roadm1

roadm_list=[]
for roadm_ip in roadm_ip_list:
    roadm=Lumentum(roadm_ip)
    roadm.wss_delete_connection(1,'all')
    roadm.wss_delete_connection(2,'all')

    roadm.set_mux_offline()
    roadm.set_demux_offline()
    
    roadm.set_mux_high_gain_mode()
    roadm.set_demux_high_gain_mode()
    
    roadm.set_mux_constant_gain(10)
    roadm.set_demux_constant_gain(10)
    
    roadm.set_mux_online()
    roadm.set_demux_online()


roadm3=Lumentum('10.10.10.33')

# channel_list=list(range(1,96))
# roadm3.make_grid(open_channels=channel_list)
# roadm3.set_mux_online()
# roadm3.set_demux_online()
# 
# exit()

roadm3.wss_delete_connection(1,'all')
roadm3.wss_delete_connection(2,'all')

roadm3.set_mux_offline()
roadm3.set_demux_offline()

roadm3.set_mux_high_gain_mode()
roadm3.set_demux_high_gain_mode()

roadm3.set_mux_constant_gain(10)
roadm3.set_demux_constant_gain(10)

roadm3.set_mux_online()
roadm3.set_demux_online()

# chunk=[
# ('193431.25', '193468.75', 1), # coherent
# ('193468.75', '193475.00', 2) # radio
# ]



