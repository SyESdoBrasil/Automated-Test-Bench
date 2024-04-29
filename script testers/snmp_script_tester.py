from pysnmp.hlapi import *

def set_frequency(ip_address, community_string, frequency_value):
    """Sets the channel frequency of a device using SNMP.

    Args:
        ip_address (str): The IP address of the device.
        community_string (str): The SNMP community string.
        frequency_value (int): The new frequency value in Hertz (Hz).
    """

    oid_channel_offset = ObjectIdentity('.1.3.6.1.4.1.10066.2.100.1.5.2.0')  

    cmd_gen = setCmd(
        SnmpEngine(),
        CommunityData(community_string, mpModel=1),  
        UdpTransportTarget((ip_address, 161)), 
        ContextData(),
        ObjectType(oid_channel_offset, Integer32(frequency_value))  
    )

    # Process the response using next() function
    error_indication, error_status, error_index, var_binds = next(cmd_gen)

    if error_indication:
        print(f"SNMP error: {error_indication}")
        return False  # Indicates failure
    else:
        print("Frequency setting successful!")
        return True   # Indicate success

# Example Usage:
set_frequency('192.168.168.168', 'private', 591142857)
