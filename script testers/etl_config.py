def config_etl(etl):
    identification = etl.query("*IDN?") #Identificates the equipment
    print("ETL Identification:", identification) 

    etl.write("SENSe1:DETector1:FUNCtion POS") #This command sets the Detector positive autopeak 
    print("Detector positive autopeak")

    etl.write("DISPlay:TRACe1:Y:SCALe:RLEVel 0") #This command sets amplitude ref level 
    print("Detector positive autopeak")

    etl.write("SENSe1:FREQuency:CENTer 581.142857Mhz") #This command sets the center frequency
    print("Detector positive autopeak")

    etl.write("SWE:TIME 10") #Defines the sweep time to 1s
    print("Sweep time setted to 20ms")

    etl.write("SET:TV:STAN ISDBT") #Set ISDBT TV  digital standard
    print("Setted mode to ISDBT")

    etl.write("BAND:VID 300Hz") #Set VBW - Video Bandwith 
    print("VBW set to 300Hz")

    etl.write("BAND 10kHz") #Set RBW - Resolution Bandwith 
    print("RBW set to 10kHz")
    
    # etl.write("FREQ:STAR 20Mhz") #Set the span to 10Mhz 
    # print("Start frequency set to 20MHz")

    # etl.write("FREQ:STOP 2000MHz") #Set the span to 10Mhz 
    # print("Stop frequency set to 2000MHz")

    etl.write("FREQ:SPAN 20Mhz") #Set the span to 10Mhz 
    print("Span setted to 10MHz")


    etl.write("SET:TV:MODE DTV")  #Set equipment to Digital TV mode
    print("Setted mode to DTV")
    
    etl.write("SWE:POIN 501") #Defines the number of sweeps points to 501
    print("Sweep points setted to 501")
