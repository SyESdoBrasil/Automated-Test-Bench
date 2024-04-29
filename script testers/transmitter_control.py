from pysnmp.hlapi import *

class TransmitterController:
    def __init__(self, ip_address, community_string):
        self.ip_address = ip_address
        self.community_string = community_string

    def get_snmp_data(self, oid):
        try:
            result = getCmd(
                SnmpEngine(),
                CommunityData(self.community_string, mpModel=1),
                UdpTransportTarget((self.ip_address, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
            )

            error_indication, error_status, error_index, var_binds = next(result)
            if error_indication:
                print(f"Error getting SNMP data for OID {oid}: {error_indication}")
                return None
            else:
                return var_binds[0][1].prettyPrint()
                
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def set_snmp_data(self, oid, value):
        try:
            result = setCmd(
                SnmpEngine(),
                CommunityData(self.community_string, mpModel=1),
                UdpTransportTarget((self.ip_address, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid), Integer32(value))
            )

            error_indication, error_status, error_index, var_binds = next(result)
            if error_indication:
                print(f"Error setting SNMP data for OID {oid}: {error_indication}")
                return False
            else:
                return True
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

# Define the OIDs
oid_transmitter_rf_on = '1.3.6.1.4.1.10066.2.100.1.8.1.0'
oid_transmitter_rf_stndby = '1.3.6.1.4.1.10066.2.100.1.8.3.0'

oid_transmitter_power = '1.3.6.1.4.1.10066.2.100.1.7.1.0'
oid_channel_frequency = '1.3.6.1.4.1.10066.2.100.1.5.2.0'

oid_software_version = '1.3.6.1.4.1.10066.3.1.1.1.10.0'
# Example Usage:
ip_address = '192.168.168.168'
community_string = 'private'

controller = TransmitterController(ip_address, community_string)

# Get transmitter RF status
transmitter_rf_on = controller.get_snmp_data(oid_software_version)
print(transmitter_rf_on)

# transmitter_rf_stndby = controller.get_snmp_data(oid_transmitter_rf_stndby)
# print("Transmitter RF Status: STNDBY")

# # Get transmitter power
# transmitter_power = controller.get_snmp_data(oid_transmitter_power)
# print("Transmitter Power:", transmitter_power)

# # Get channel frequency
# channel_frequency = controller.get_snmp_data(oid_channel_frequency)
# print("Channel Frequency:", channel_frequency)

# Set transmitter RF status (Assuming '1' to turn on and '0' to turn off)
# controller.set_snmp_data(oid_transmitter_rf_on, 1)

# controller.set_snmp_data(oid_transmitter_rf_stndby, 1)
