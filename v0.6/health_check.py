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
          
roadm1 = Lumentum('10.10.10.38')
roadm3 = Lumentum('10.10.10.33')
roadm4 = Lumentum('10.10.10.32')
roadm5 = Lumentum('10.10.10.31')
roadm6 = Lumentum('10.10.10.30')


x=roadm3.edfa_get_info()
print("Roadm 3")
check_status("booster",x)
check_health("booster",x)
report_health("booster",x)
check_status("preamp",x)
check_health("preamp",x)
report_health("preamp",x)

x=roadm1.edfa_get_info()
print("Roadm 1")
check_status("booster",x)
check_health("booster",x)
report_health("booster",x)
check_status("preamp",x)
check_health("preamp",x)
report_health("preamp",x)

print("Roadm 6")
x=roadm6.edfa_get_info()
check_status("booster",x)
check_health("booster",x)
report_health("booster",x)
check_status("preamp",x)
check_health("preamp",x)
report_health("preamp",x)

print("Roadm 5")
x=roadm5.edfa_get_info()
check_status("booster",x)
check_health("booster",x)
report_health("booster",x)
check_status("preamp",x)
check_health("preamp",x)
report_health("preamp",x)

print("Roadm 4")
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


