import pyvisa
from pysnmp.hlapi import *

def get_snmp_data(oid, ip_address, community_string):
    try:
        result = getCmd(
            SnmpEngine(),
            CommunityData(community_string, mpModel=1),
            UdpTransportTarget((ip_address, 161)),
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

def main():
    rm = pyvisa.ResourceManager()

    try:
        etl = rm.open_resource("TCPIP::169.254.200.78::INSTR") 
        etl.timeout = 5000  # Adjust timeout if needed

        identification = etl.query("*IDN?")
        print("ETL Identification:", identification) 

        # Example usage of get_snmp_data function
        oid = '1.3.6.1.4.1.10066.2.100.1.5.2.0'  # Example OID
        snmp_data = get_snmp_data(oid, '192.168.168.168', 'private')  # Adjust IP and community string
        if snmp_data is not None:
            print(f"SNMP data for OID {oid}: {snmp_data}")
            print(type(snmp_data))

        etl.write(f"SENSe1:FREQuency:CENTer {snmp_data}") #This command sets the Detector positive autopeak 
        print("Detector positive autopeak")

    except pyvisa.VisaIOError as error:
        print("Connection Error:", error)

    finally:
        if etl:
            etl.close()

if __name__ == "__main__":
    main()
