from tcdona2.lumentum2 import *


roadm3 = Lumentum('10.10.10.33')
roadm4 = Lumentum('10.10.10.32')
roadm5 = Lumentum('10.10.10.31')

r3_conn = roadm3.wss_get_connections()
r4_conn = roadm4.wss_get_connections()
r5_conn = roadm5.wss_get_connections()

A=roadm3.get_mux_connection_output_power()
B=roadm4.get_mux_monitored_power()
C=roadm4.get_mux_connection_output_power()
D=roadm4.get_demux_connection_input_power()
E=roadm4.get_demux_monitored_power()
F=roadm5.get_mux_monitored_power()
G=roadm5.get_mux_connection_output_power()
H=roadm5.get_demux_connection_input_power()
J=roadm5.get_demux_monitored_power()


for i in range(0,95):
     a,b = A[i]
     c,d = B[i]
     e,f = C[i]
     g,h = D[i]
     i,j = E[i]
     k,l = F[i]
     m,n = G[i]
     o,p = H[i]
     q,r = J[i]
     print(i,  "%7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f"%(
          b,d,f,h,j,l,n,p,r
          ))
     
print(roadm3.edfa_get_info())
print(roadm4.edfa_get_info())
print(roadm5.edfa_get_info())