from tcdona2.lumentum2 import *


roadm3 = Lumentum('10.10.10.33')
roadm4 = Lumentum('10.10.10.32')

r3_conn = roadm3.wss_get_connections()
r4_conn = roadm4.wss_get_connections()


for i in range(1,96): 
     print(i,  "\t", r3_conn['mux']['conn-%d' % i]['blocked'], "\t",
          "%7.1f %7.1f %7.1f"%(
          r3_conn['demux']['conn-%d' % i]['output-power'],
          r3_conn['mux']['conn-%d' % i]['input-power'],
          r4_conn['demux']['conn-%d' % i]['input-power'],
          ))
     
print(roadm3.edfa_get_info())
