from tcdona2.lumentum2 import *

def check_status(element, edfa_info):
     status= ""
     if edfa_info[element]['control_mode'] != 'constant-gain':
          status = status + "Not in Constant gain mode. "
     if edfa_info[element]['maintenance-state'] != 'in-service':
          status = status + "Not in Service. "
          
     if len(status)>0:
          print(element, "problem", status)
     else:
          print(element, "all okay")
          
def check_health(element,edfa_info):
     status=""
     gain=edfa_info[element]['output_power'] - edfa_info[element]['input_power']
     if edfa_info[element]['target_gain'] > gain:
          status = status + "Gain Saturation %.1f > %.1f ." % (edfa_info[element]['target_gain'], gain)
          
     atten=edfa_info[element]['voa_output_power'] - edfa_info[element]['voa_input_power']
     if edfa_info[element]['voa_attenuation'] > atten:
          status = status + "VOA suppress %.1f > %.1f ." % (edfa_info[element]['voa_attenuation'], atten)
     
     if edfa_info[element][ 'output_power'] < 15:
          status = status + "Too low Power. "

     if len(status)>0:
          print(element, "problem ", status)
     else:
          print(element, "all okay")
          
def report_health(element, edfa_info):
     print(edfa_info[element]['maintenance-state'],
           "G:", edfa_info[element]['target_gain'],
           "I:",edfa_info[element]['input_power'],
           "O:",edfa_info[element]['output_power'],
           "VI",edfa_info[element]['voa_input_power'],
           "VO",edfa_info[element]['voa_output_power']
           )
          

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


for i in range(0,94):
     a,r3muxi = A[i] 
     c,r4muxi = B[i] # mon
     e,r4muxo = C[i] # out
     g,r4demuxi = D[i] # in
     i,r4demuxo = E[i] # mon
     k,r5muxi = F[i] # mon
     m,r5muxo = G[i] # out
     o,r5demuxi = H[i] # in
     q,r5demuxo = J[i] # mon
     
     r5mux = r5muxi-r5muxo
     if i == 1: r5mux_base = r5mux
     r5demux = r5demuxi-r5demuxo
     if i == 1: r5demux_base = r5demux
     r4mux = r4muxi-r4muxo
     if i == 1: r4mux_base = r4mux 
     r4demux = r4demuxi-r4demuxo
     if i == 1: r4demux_base = r4demux 
     
     print(i,  "%7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f %7.1f"%(
          r3muxi,
          r5muxi, r5muxo, r5demuxi, r5demuxo,
          r4muxi, r4muxo, r4demuxi, r4demuxo,
          r5mux,
          r5demux,
          r4mux,
          r4demux,
          r5mux - r5mux_base,
          r5demux - r5demux_base,
          r4mux - r4mux_base,
          r4demux - r4demux_base,
          ))

x=roadm5.edfa_get_info()
check_status("booster",x)
check_health("booster",x)
report_health("booster",x)
check_status("preamp",x)
check_health("preamp",x)
report_health("preamp",x)
x=roadm4.edfa_get_info()
check_status("booster",x)
check_health("booster",x)
report_health("booster",x)
check_status("preamp",x)
check_health("preamp",x)
report_health("preamp",x)

exit()

print(roadm3.edfa_get_info())
print(roadm4.edfa_get_info())
print(roadm5.edfa_get_info())


