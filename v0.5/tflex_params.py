from ncclient import manager
from ncclient.xml_ import *
import xmltodict
import logging
import time


class tflex:
    def __init__(self, ip_address):
        self.conn = manager.connect(host=ip_address,
                           port=830,
                           username="admin",
                           password="CHGME.1a",
                           timeout=60,
                           hostkey_verify=False)
        self.conn.raise_mode = 0  # on RPCError, do not throw any exceptions
        self._config = {}
        self._get_config()


    def change_configuration(self, line_port, logical_interface, modulation, target_power, central_frequency):
        sleep_counter = 0
        if self._config[line_port]['admin_state'] != "acor-stt:is":
            self.set_interface_on(line_port)
        if self._config[line_port]['logical_interface'] != logical_interface:
            if self._config[line_port]['logical_interface']:
                self.delete_logical_interface(line_port)
            self.create_logical_interface(line_port, logical_interface)
            sleep_counter = 150
        if self._config[line_port]['modulation'] != modulation:
            self.set_admin_maintenance(line_port + '/' + logical_interface)
            self.set_interface_modulation(line_port, modulation)
            self.remove_admin_maintenance(line_port + '/' + logical_interface)
            sleep_counter = 150
        try:
            if not self._config[line_port]['frequency'] == central_frequency and self._config[line_port]['target-output-power'] == target_power:
                self.set_power_and_frequency(line_port=line_port, power=target_power, frequency=central_frequency)
                sleep_counter = 30
        except:
            self.set_power_and_frequency(line_port=line_port, power=target_power, frequency=central_frequency)
            sleep_counter = 30
        return sleep_counter
    
    def change_configuration_blocking(self, line_port, logical_interface, modulation, target_power, central_frequency, DEBUG=True):
        sleep_counter = 0
        if self._config[line_port]['admin_state'] != "acor-stt:is":
            self.set_interface_on(line_port)
        if self._config[line_port]['logical_interface'] != logical_interface:
            if self._config[line_port]['logical_interface']:
                self.delete_logical_interface(line_port)
            self.create_logical_interface(line_port, logical_interface)
            sleep_counter = 150
        if self._config[line_port]['modulation'] != modulation:
            self.set_admin_maintenance(line_port + '/' + logical_interface)
            self.set_interface_modulation(line_port, modulation)
            self.remove_admin_maintenance(line_port + '/' + logical_interface)
            sleep_counter = 150
        if not self._config[line_port]['frequency'] == central_frequency and self._config[line_port]['target-output-power'] == target_power:
            self.set_power_and_frequency(line_port=line_port, power=target_power, frequency=central_frequency)
            sleep_counter = 30
            
            
        offline = True
        stable = False
        time.sleep(sleep_counter)

        while offline:
            response = self.get_operational_state(line_port)
            response_details = xmltodict.parse(response.xml)
            status = response_details['rpc-reply']['data']['components']['component']['state']['oper-status']
            if DEBUG:
                print(status)
            offline = None if status == 'ACTIVE' else True
            time.sleep(5)
    
        while not stable:
            pm_data = self.get_params(line_port=line_port)
            if pm_data['QualityTF_indefinite_q-factor']:
                Q_factor = float(pm_data['QualityTF_indefinite_q-factor'])
                time.sleep(5)
                pm_data_verification = self.get_params(line_port=line_port)
                stable = abs(Q_factor - float(pm_data_verification['QualityTF_indefinite_q-factor'])) < 0.05
                if DEBUG:
                    print(Q_factor, float(pm_data_verification['QualityTF_indefinite_q-factor']))
            else:
                time.sleep(15)
        pm_data = self.get_params(line_port=line_port)
        if DEBUG:
            print(pm_data['QualityTF_indefinite_q-factor'])
        return pm_data


    def return_current_config(self):
        return self._config

    def _get_config(self):
        response = self.get_interface()
        response_details = xmltodict.parse(response.xml)
        config = response_details['rpc-reply']['data']['terminal-device']['logical-channels']['channel']
        

        # get line_ports and logical interfaces
        for config_details in config:
            if 'odu4' not in config_details['config']['description']:
                line_port = config_details['config']['description'].split('/ot')[0]
                self._config[line_port] = {}
                self._config[line_port]['line_port'] = line_port
                self._config[line_port]['logical_interface'] = config_details['config']['description'].split(line_port +
                                                                                                             '/')[1]
                self._config[line_port]['index'] = config_details['config']['index']
        for line_port in self._config.keys():
            # get admin state
            response = self.get_port_admin_state(line_port)
            response_details = xmltodict.parse(response.xml)
            self._config[line_port]['admin_state'] = response_details['rpc-reply']['data']['managed-element']['interface']['physical-interface']['state']['admin-state']

            # get modulation
            response = self.get_interface_modulation(line_port)
            response_details = xmltodict.parse(response.xml)
            self._config[line_port]['modulation'] = response_details['rpc-reply']['data']['managed-element']['interface']['logical-interface']['otsia']['otsi']['optical-channel-configuration']['modulation']

            # read power and frequency
            response = self.get_power_and_frequency(line_port)
            response_details = xmltodict.parse(response.xml)
            for component_details in response_details['rpc-reply']['data']['components']['component']:
                if 'config' in component_details.keys():
                    assert component_details['config']['name'] == 'optch ' + line_port
                    try:
                        self._config[line_port]['frequency'] = component_details['optical-channel']['config']['frequency']
                        self._config[line_port]['target-output-power'] = component_details['optical-channel']['config']['target-output-power']
                    except:
                        pass

    def get_operational_state(self, line_port):
        request = f'''
                    <components xmlns="http://openconfig.net/yang/platform">
                      <component>
                        <name>port {line_port}</name>
                        <state>
                          <oper-status/>
                        </state>
                      </component>
                    </components>
                    '''
        flt = ("subtree", request)
        return self.conn.get(filter=flt)
    

    def get_interface(self):
        request = '''
        <terminal-device xmlns="http://openconfig.net/yang/terminal-device">
        <logical-channels>
        <channel>
        <config>
        <index/>
        <description/>
        </config>
        </channel>
        </logical-channels>
        </terminal-device>
        '''

        flt = ("subtree", request)

        return self.conn.get_config(source="running", filter=flt)

    def delete_logical_interface(self, line_port):
        request = f'''
                <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                <terminal-device xmlns="http://openconfig.net/yang/terminal-device">
                    <logical-channels>
                        <channel nc:operation="delete">
                            <config>
                                <index>{self._config[line_port]['index']}</index>
                                <description>{line_port}</description>
                            </config>
                        </channel>
                    </logical-channels>
                </terminal-device>
                </nc:config>
                '''
        response = self.conn.edit_config(target="running", config=request)
        assert 'ok' in xmltodict.parse(response.xml)['rpc-reply'].keys(), print(response)
        self._config[line_port]['logical_interface'] = None
        return response

    def create_logical_interface(self, line_port, logical_interface):
        request = f'''
                     <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                          <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
                              <entity-name>1</entity-name>
                              <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
                              <name>{self._config[line_port]['line_port'] + '/' + logical_interface}</name>
                                  <logical-interface/>
                              </interface>
                          </managed-element>
                     </nc:config>
                     '''
        response = self.conn.edit_config(target="running", config=request)
        assert 'ok' in xmltodict.parse(response.xml)['rpc-reply'].keys(), print(response)
        self._config[line_port]['logical_interface'] = logical_interface
        self._config[line_port]['modulation'] = self.get_interface_modulation(line_port)
        return response

    def get_interface_modulation(self, line_port):
        request = f'''<managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element"
                               xmlns:f8-ne="http://www.advaoptical.com/aos/netconf/adva-f8-ne"
                               xmlns:acor-me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
                                <entity-name>1</entity-name>
                                  <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
                                    <name>{self._config[line_port]['line_port'] + '/' + self._config[line_port]['logical_interface']}</name>
                                    <logical-interface>
                                      <entity-name>{self._config[line_port]['logical_interface']}</entity-name>
                                      <otsia xmlns="http://www.advaoptical.com/aos/netconf/aos-domain-otn">
                                        <otsi>
                                          <id>1</id>
                                          <optical-channel-configuration>
                                            <modulation/>
                                          </optical-channel-configuration>
                                        </otsi>
                                      </otsia>
                                    </logical-interface>
                                  </interface>
                                </managed-element>
                                '''
        flt = ("subtree", request)
        return self.conn.get_config(source="running", filter=flt)

    def set_interface_modulation(self, line_port, modulation):
        request = f'''
                    <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                        <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element"
                               xmlns:f8-ne="http://www.advaoptical.com/aos/netconf/adva-f8-ne"
                               xmlns:acor-me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
                                <entity-name>1</entity-name>
                                  <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
                                    <name>{self._config[line_port]['line_port'] + '/' + self._config[line_port]['logical_interface']}</name>
                                    <logical-interface>
                                      <entity-name>{self._config[line_port]['logical_interface']}</entity-name>
                                      <otsia xmlns="http://www.advaoptical.com/aos/netconf/aos-domain-otn">
                                        <otsi>
                                          <id>1</id>
                                          <optical-channel-configuration>
                                            <modulation>{modulation}</modulation>
                                            <state-of-polarization-tracking>normal-tracking</state-of-polarization-tracking>
                                          </optical-channel-configuration>
                                        </otsi>
                                      </otsia>
                                    </logical-interface>
                                  </interface>
                                </managed-element>
                              </nc:config>
                                '''
        response = self.conn.edit_config(target="running", config=request)
        assert 'ok' in xmltodict.parse(response.xml)['rpc-reply'].keys(), print(response)
        self._config[line_port]['modulation'] = modulation
        return response

    def get_power_and_frequency(self, line_port):
        request = f'''
        <oc-platform:components xmlns:oc-platform="http://openconfig.net/yang/platform">
        <oc-platform:component>
        <oc-platform:config>
        <oc-platform:name>optch {line_port}</oc-platform:name>
        </oc-platform:config>
        <oc-opt-term:optical-channel xmlns:oc-opt-term="http://openconfig.net/yang/terminal-device">
        <oc-opt-term:config>
        <oc-opt-term:frequency/>
        <oc-opt-term:target-output-power/>
        </oc-opt-term:config>
        </oc-opt-term:optical-channel>
        </oc-platform:component>
        </oc-platform:components>
        '''
        flt = ("subtree", request)

        return self.conn.get_config(source="running", filter=flt)

    def set_power_and_frequency(self, line_port, power, frequency):
        request = f'''
        <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <oc-platform:components xmlns:oc-platform="http://openconfig.net/yang/platform">
        <oc-platform:component>
        <oc-platform:config>
        <oc-platform:name>optch {line_port}</oc-platform:name>
        </oc-platform:config>
        <oc-opt-term:optical-channel xmlns:oc-opt-term="http://openconfig.net/yang/terminal-device">
        <oc-opt-term:config>
        <oc-opt-term:frequency>{frequency}</oc-opt-term:frequency>
        <oc-opt-term:target-output-power>{power:.1f}</oc-opt-term:target-output-power>
        </oc-opt-term:config>
        </oc-opt-term:optical-channel>
        </oc-platform:component>
        </oc-platform:components>
        </nc:config>
        '''
        response = self.conn.edit_config(target="running", config=request)
        assert 'ok' in xmltodict.parse(response.xml)['rpc-reply'].keys(), print(response)
        self._config[line_port]['frequency'] = frequency
        self._config[line_port]['target-output-power'] = power
        return response
    
    def set_power(self, line_port, power):
        request = f'''
        <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <oc-platform:components xmlns:oc-platform="http://openconfig.net/yang/platform">
        <oc-platform:component>
        <oc-platform:config>
        <oc-platform:name>optch {line_port}</oc-platform:name>
        </oc-platform:config>
        <oc-opt-term:optical-channel xmlns:oc-opt-term="http://openconfig.net/yang/terminal-device">
        <oc-opt-term:config>
        <oc-opt-term:target-output-power>{power:.1f}</oc-opt-term:target-output-power>
        </oc-opt-term:config>
        </oc-opt-term:optical-channel>
        </oc-platform:component>
        </oc-platform:components>
        </nc:config>
        '''
        response = self.conn.edit_config(target="running", config=request)
        assert 'ok' in xmltodict.parse(response.xml)['rpc-reply'].keys(), print(response)
        self._config[line_port]['target-output-power'] = power
        return response
    
    def set_frequency(self, line_port, frequency):
        request = f'''
        <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <oc-platform:components xmlns:oc-platform="http://openconfig.net/yang/platform">
        <oc-platform:component>
        <oc-platform:config>
        <oc-platform:name>optch {line_port}</oc-platform:name>
        </oc-platform:config>
        <oc-opt-term:optical-channel xmlns:oc-opt-term="http://openconfig.net/yang/terminal-device">
        <oc-opt-term:config>
        <oc-opt-term:frequency>{frequency}</oc-opt-term:frequency>
        </oc-opt-term:config>
        </oc-opt-term:optical-channel>
        </oc-platform:component>
        </oc-platform:components>
        </nc:config>
        '''
        response = self.conn.edit_config(target="running", config=request)
        assert 'ok' in xmltodict.parse(response.xml)['rpc-reply'].keys(), print(response)
        self._config[line_port]['frequency'] = frequency
        return response

    def set_interface_on(self, line_port):
        return self.set_interface_state(1, line_port)
    
    def set_interface_off(self, line_port):
        return self.set_interface_state(0, line_port)

    def set_interface_state(self, state, line_port):
        if state == 0:
            adva_state = "acor-stt:oos"
        else:
            adva_state = "acor-stt:is"
            
        request = f'''
        <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
        <entity-name>1</entity-name>
        <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">   
        <name>{self._config[line_port]['line_port'] + '/' + self._config[line_port]['logical_interface']}</name>
        <physical-interface>
        <state xmlns:acor-stt="http://www.advaoptical.com/aos/netconf/aos-core-state-types">
        <admin-state>{adva_state}</admin-state>
        </state>
        </physical-interface>
        </interface>
        </managed-element>
        </nc:config>
        '''
        response = self.conn.edit_config(target="running", config=request)
        assert 'ok' in xmltodict.parse(response.xml)['rpc-reply'].keys(), print(response)
        return response
    
    def get_interface_state(self, line_port):
        request = f'''
        <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
        <entity-name>1</entity-name>
        <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">   
        <name>{line_port}</name>
        <physical-interface>
        <state xmlns:acor-stt="http://www.advaoptical.com/aos/netconf/aos-core-state-types">
        </state>
        </physical-interface>
        </interface>
        </managed-element>
        '''

        flt=("subtree", request)
        return self.conn.get_config(source="running", filter=flt)

    def get_x(self, line_port):
        request = f'''
        <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
        <entity-name>1</entity-name>
        <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">   
        <name>{line_port}</name>
        <physical-interface>
        </physical-interface>
        </interface>
        </managed-element>
        '''

        flt=("subtree", request)
        return self.conn.get_config(source="running", filter=flt)
    
    def set_optical_power(self):
        request = f'''
                    <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element" xmlns:f8-ne="http://www.advaoptical.com/aos/netconf/adva-f8-ne" xmlns:acor-me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
      <entity-name>1</entity-name>
      <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
        <name>1/2/n1</name>
        <physical-interface xmlns:acor-factt="http://www.advaoptical.com/aos/netconf/aos-core-facility-types">
          <port-type>acor-factt:network-port</port-type>
          <port-id>1</port-id>
          <user-label/>
          <lr-phys-optical>
            <opt-setpoint>5</opt-setpoint>
          </lr-phys-optical>
        </physical-interface>
      </interface>
    </managed-element>
    </nc:config>
        '''
        response = self.conn.edit_config(target="running", config=request)
        return response       

    def get_y(self):
        request = f'''
      <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
	    <entity-name>1</entity-name>
	      <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">	
          <name>1/2/n1</name>
	        <physical-interface>
            <lr-phys-optical>
              <tuned-frequency></tuned-frequency>
            </lr-phys-optical>
	        </physical-interface>
	      </interface>
      </managed-element>
        '''

        flt=("subtree", request)
        return self.conn.get_config(source="running", filter=flt)

    def set_y(self):
        request = f'''
        <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
	    <entity-name>1</entity-name>
	      <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">	
          <name>1/2/n1</name>
	        <physical-interface>
            <lr-phys-optical>
              <tuned-frequency>194950000</tuned-frequency>
            </lr-phys-optical>
	        </physical-interface>
	      </interface>
      </managed-element>
          </nc:config>
        '''
        response = self.conn.edit_config(target="running", config=request)
        return response
    
    # def set_interface_bitspersymbol(self,bitspersymbol):
    #     request = '''
    #     <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element"
    #                xmlns:f8-ne="http://www.advaoptical.com/aos/netconf/adva-f8-ne"
    #                xmlns:acor-me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
    #     <entity-name>1</entity-name>
    #       <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
    #         <name>%s</name>
    #         <logical-interface>
    #           <entity-name>ot600</entity-name>
    #           <otsia xmlns="http://www.advaoptical.com/aos/netconf/aos-domain-otn">
    #             <otsi>
    #               <id>1</id>
    #               <optical-channel-configuration>
    #                <bits-per-symbol>%1f</bits-per-symbol>
    #               </optical-channel-configuration>
    #             </otsi>
    #           </otsia>
    #         </logical-interface>
    #       </interface>
    #     </managed-element>
    #     </nc:config>
    #     ''' % (self.interface, bitspersymbol)
    #
    #     return self.conn.edit_config(target="running", config=request)
    
    # def set_interface_filtershape(self,filtershape):
    #     request = '''
    #     <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element"
    #                xmlns:f8-ne="http://www.advaoptical.com/aos/netconf/adva-f8-ne"
    #                xmlns:acor-me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
    #     <entity-name>1</entity-name>
    #       <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
    #         <name>%s</name>
    #         <logical-interface>
    #           <entity-name>ot600</entity-name>
    #           <otsia xmlns="http://www.advaoptical.com/aos/netconf/aos-domain-otn">
    #             <otsi>
    #               <id>1</id>
    #               <optical-channel-configuration>
    #                 <filter-shape>%s</filter-shape>
    #               </optical-channel-configuration>
    #             </otsi>
    #           </otsia>
    #         </logical-interface>
    #       </interface>
    #     </managed-element>
    #     </nc:config>
    #     ''' % (self.interface, filtershape)
    #
    #     return self.conn.edit_config(target="running", config=request)
    #
    # def set_interface_filterrolloff(self,filterrolloff):
    #     request = '''
    #     <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element"
    #                xmlns:f8-ne="http://www.advaoptical.com/aos/netconf/adva-f8-ne"
    #                xmlns:acor-me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
    #     <entity-name>1</entity-name>
    #       <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
    #         <name>%s</name>
    #         <logical-interface>
    #           <entity-name>ot600</entity-name>
    #           <otsia xmlns="http://www.advaoptical.com/aos/netconf/aos-domain-otn">
    #             <otsi>
    #               <id>1</id>
    #               <optical-channel-configuration>
    #                 <filter-roll-off>%1f</filter-roll-off>
    #               </optical-channel-configuration>
    #             </otsi>
    #           </otsia>
    #         </logical-interface>
    #       </interface>
    #     </managed-element>
    #     </nc:config>
    #     ''' % (self.interface, filterrolloff)
    #
    #     return self.conn.edit_config(target="running", config=request)
    #
    # def set_interface_polarizationtracking(self,polarisationtracking):
    #     request = '''
    #     <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element"
    #                xmlns:f8-ne="http://www.advaoptical.com/aos/netconf/adva-f8-ne"
    #                xmlns:acor-me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
    #     <entity-name>1</entity-name>
    #       <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
    #         <name>%s</name>
    #         <logical-interface>
    #           <entity-name>ot600</entity-name>
    #           <otsia xmlns="http://www.advaoptical.com/aos/netconf/aos-domain-otn">
    #             <otsi>
    #               <id>1</id>
    #               <optical-channel-configuration>
    #                 <state-of-polarization-tracking>%s</state-of-polarization-tracking>
    #               </optical-channel-configuration>
    #             </otsi>
    #           </otsia>
    #         </logical-interface>
    #       </interface>
    #     </managed-element>
    #     </nc:config>
    #     ''' % (self.interface, polarisationtracking)
    #
    #     return self.conn.edit_config(target="running", config=request)

    def set_admin_maintenance(self, element):
        """

        :param element: line_port or logical interface e.g. 1/2/n1 or 1/2/n1/ot200
        :return:
        """
        request = f'''
     <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
     <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element"
                   xmlns:f8-ne="http://www.advaoptical.com/aos/netconf/adva-f8-ne"
                   xmlns:acor-me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
        <entity-name>1</entity-name>
        <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
          <name>{element}</name>
          <physical-interface xmlns:acor-factt="http://www.advaoptical.com/aos/netconf/aos-core-facility-types">
            <state xmlns:acor-stt="http://www.advaoptical.com/aos/netconf/aos-core-state-types">
              <admin-is-sub-states>acor-stt:mt</admin-is-sub-states>
            </state>
          </physical-interface>
        </interface>
      </managed-element>
      </nc:config>
        '''
        
        return self.conn.edit_config(target="running", config=request)  

    def remove_admin_maintenance(self, element):
        """

        :param element: line_port or logical interface e.g. 1/2/n1 or 1/2/n1/ot200
        :return:
        """
        request = f'''
        <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
          <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element"
                       xmlns:f8-ne="http://www.advaoptical.com/aos/netconf/adva-f8-ne"
                       xmlns:acor-me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
            <entity-name>1</entity-name>
            <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
              <name>{element}</name>
              <physical-interface xmlns:acor-factt="http://www.advaoptical.com/aos/netconf/aos-core-facility-types">
                <state xmlns:acor-stt="http://www.advaoptical.com/aos/netconf/aos-core-state-types">
                  <admin-is-sub-states nc:operation="delete">acor-stt:mt</admin-is-sub-states>
                </state>
              </physical-interface>
            </interface>
          </managed-element>
           </nc:config>
        '''
        
        return self.conn.edit_config(target="running", config=request)
    
    def get_port_admin_state(self, line_port):
        request = f'''
      <managed-element xmlns="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
            <entity-name>1</entity-name>
            <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
                <name>{line_port}</name>
                <physical-interface>
                    <state xmlns:acor-stt="http://www.advaoptical.com/aos/netconf/aos-core-state-types">
                        <admin-state/>
                    </state>
                </physical-interface>
            </interface>
        </managed-element>
        '''

        flt=("subtree", request)
        return self.conn.get_config(source="running", filter=flt)


    def get_params(self, line_port):
        perf_dict = {}
    
        request_pm_data = f'''
        <get-pm-data xmlns="http://www.advaoptical.com/aos/netconf/aos-core-pm"
                     xmlns:fac="http://www.advaoptical.com/aos/netconf/aos-core-facility"
                     xmlns:me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element"
                     xmlns:otn="http://www.advaoptical.com/aos/netconf/aos-domain-otn">
          <target-entity>/me:managed-element[me:entity-name="1"]/fac:interface[fac:name="{self._config[line_port]['line_port'] + '/' + self._config[line_port]['logical_interface']}"]/fac:logical-interface/otn:otsia/otn:otsi[id="1"]</target-entity>
          <pm-data>
            <pm-current-data/>
          </pm-data>
        </get-pm-data>
        '''
    
        reply_pm_data = self.conn.dispatch(to_ele(request_pm_data))
        perf_details = xmltodict.parse(reply_pm_data.xml)
    
        perf_categories = perf_details['rpc-reply']['pm-data']['pm-current-data']
    
        for perf_cat in perf_categories:
            name=perf_cat['name']
            interval=perf_cat['bin-interval'].split("-")[2]
            montypemonval=perf_cat['montype-monval']
            if isinstance(montypemonval, list):
                for mtmv in montypemonval:
                    mt=mtmv['mon-type'].split(":")[1]
                    mv=mtmv['mon-val']
                    perf_dict["_".join([name,interval,mt])] = mv
                    # print(name,interval,mt,mv)
            else:
                mt=montypemonval['mon-type'].split(":")[1]
                mv=montypemonval['mon-val']
                perf_dict["_".join([name,interval,mt])] = mv
                #print(name,interval,mt)

        # print(perf_dict)
        otu_type = 'otu-c2pa'
        response = self.get_otu_type(line_port)
        response_details = xmltodict.parse(response.xml)
        # print(response_details['rpc-reply']['data']['managed-element']['interface']['logical-interface'].keys())
        if 'otu4' in response_details['rpc-reply']['data']['managed-element']['interface']['logical-interface'].keys():
            otu_type = 'otu4'

    
        request_fec_ber = f'''
        <get-pm-data xmlns="http://www.advaoptical.com/aos/netconf/aos-core-pm"
                     xmlns:me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element"
                     xmlns:fac="http://www.advaoptical.com/aos/netconf/aos-core-facility"
                     xmlns:adom-oduckpa="http://www.advaoptical.com/aos/netconf/aos-domain-otn-oduckpa"
                     xmlns:otn="http://www.advaoptical.com/aos/netconf/aos-domain-otn">
          <target-entity>/me:managed-element[me:entity-name="1"]/fac:interface[fac:name="{self._config[line_port]['line_port'] + '/' + self._config[line_port]['logical_interface']}"]/fac:logical-interface/otn:{otu_type}</target-entity>
          <pm-data>
            <pm-current-data/>
          </pm-data>
        </get-pm-data>
        '''
    
        reply_fec_ber = self.conn.dispatch(to_ele(request_fec_ber))
    
        perf_details = xmltodict.parse(reply_fec_ber.xml)
        
        #print(perf_details)
        
        if 'pm-data' in perf_details['rpc-reply'].keys():
            perf_categories=perf_details['rpc-reply']['pm-data']['pm-current-data']
            for perf_cat in perf_categories:
                name = perf_cat['name']
                interval = perf_cat['bin-interval'].split("-")[2]
                montypemonval = perf_cat['montype-monval']
                if isinstance(montypemonval, list):
                    for mtmv in montypemonval:
                        mt = mtmv['mon-type'].split(":")[1]
                        mv = mtmv['mon-val']
                        perf_dict[":".join([name, interval, mt])] = mv
                else:
                    mt=montypemonval['mon-type'].split(":")[1]
                    mv=montypemonval['mon-val']
                    perf_dict[":".join([name, interval, mt])] = mv
                #print(mt, mv)
        else:
            print('No BER reading available!')
        return perf_dict

    def get_otu_type(self, line_port):
        request = f'''
        <managed-element xmlns:acor-me="http://www.advaoptical.com/aos/netconf/aos-core-managed-element">
        <interface xmlns="http://www.advaoptical.com/aos/netconf/aos-core-facility">
        <name>{self._config[line_port]['line_port'] + '/' + self._config[line_port]['logical_interface']}</name>
        <logical-interface/>
        </interface>
        </managed-element>
        '''
        flt = ("subtree", request)
        return self.conn.get_config(source="running", filter=flt)   


    def read_pm_data(self,sleep_counter, line_port,DEBUG=False):
        offline = True
        stable = False
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        time.sleep(sleep_counter)
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        while offline:
            response = self.get_operational_state(line_port)
            response_details = xmltodict.parse(response.xml)
            status = response_details['rpc-reply']['data']['components']['component']['state']['oper-status']
            if DEBUG:
                print(status)
            offline = None if status == 'ACTIVE' else True
            time.sleep(5)
    
        while not stable:
            pm_data = self.get_params(line_port=line_port)
            if pm_data['QualityTF_indefinite_q-factor']:
                Q_factor = float(pm_data['QualityTF_indefinite_q-factor'])
                time.sleep(5)
                pm_data_verification = self.get_params(line_port=line_port)
                try:
                    stable = abs(Q_factor - float(pm_data_verification['QualityTF_indefinite_q-factor'])) < 0.05
                    if DEBUG:
                        print(Q_factor, float(pm_data_verification['QualityTF_indefinite_q-factor']))
                except:
                    stable = False
                    print("QualityTF_indefinite_q-factor exception")
            else:
                time.sleep(15)
        pm_data = self.get_params(line_port=line_port)
        if DEBUG:
            print(pm_data['QualityTF_indefinite_q-factor'])
        return pm_data
