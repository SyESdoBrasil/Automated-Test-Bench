import pyvisa

rm = pyvisa.ResourceManager()

try:
    etl = rm.open_resource("TCPIP::169.254.200.78::INSTR") 
    etl.timeout = 5000  # Adjust timeout if needed

    identification = etl.query("*IDN?") #Identificates the equipment
    print("ETL Identification:", identification) 
        
    # etl.write("SENSe1:DETector1:FUNCtion POS") #This command sets the Detector positive autopeak 
    # print("Detector positive autopeak")
    
    # etl.write("DISPlay:TRACe1:Y:SCALe:RLEVel -20 ") #This command sets the Detector positive autopeak 
    # print("Detector positive autopeak")

    # etl.write("FREQ:SPAN 20Mhz") #Set the span to 10Mhz 
    # print("Span setted to 10MHz")
    frequency = 597142857
    # etl.write(f"SENSe1:FREQuency:CENTer {frequency}") #This command sets the Detector positive autopeak 
    print("Detector positive autopeak")

    etl.write(f"FREQ:CHAN {frequency}") # set channel to 3


    # etl.write("SET:TV:MODE DTV")  #Set equipment to Digital TV moFF
    # etl.write("INST CATV") # Set intrumental to TV/Radio Analyzer


 
    # etl.write("DISP:ZOOM:OVER MERRms") # Connects to the digital TV measurement screen   
    # etl.write("DISP:MEAS:OVER:TMCC:STAT OFF") # Changes Overview stats to meas   
    # etl.write("SET:TV:MODE DTV")  #Set equipment to Digital TV mode
    # print("Setted mode to DTV")

    # etl.write("CONF:TV:CTAB:SEL 'TV-BRAZIL_ISDB-T'") #Set ISDBT TV  Channel Table
    # print("Set ISDBT TV  Channel Table")

    # etl.write("FREQ:CHAN 32") # set channel to 3

    # etl.write("CALCulate1:DELTamarker1:FUNCtion:FIXed:STATe OFF") #This command sets the Detector positive autopeak 

    # etl.write("CALCulate1:MARK1:X 581.142857Mhz") #This command sets thee center Marker 
    # etl.write("CALCulate1:DELTamarker1:X -2.79Mhz") #This command sets the Marker 1
    # etl.write("CALCulate1:DELTamarker2:X 2.79Mhz") #This command sets the Marker 2
    # etl.write("CALCulate1:DELTamarker3:X -2.86Mhz") #This command sets the Marker 3
    # etl.write("CALCulate1:DELTamarker4:X 2.86Mhz") #This command sets the Marker 4 


#trace 2 
    # etl.write("SENSe2:DETector1:FUNCtion POS") #This command sets the Detector positive autopeak 

    # etl.write("SENSe2:FREQuency:CENTer 581.142857Mhz") #This command sets the Detector positive autopeak 
    # print("Detector positive autopeak")

    # etl.write("CALCulate1:DELTamarker1:FUNCtion:FIXed:STATe OFF") #This command sets the Detector positive autopeak 

    # etl.write("CALCulate1:MARK1:X 581.142857Mhz:TRACe 2") #This command sets the Detector positive autopeak 

    # etl.write("CALCulate1:DELTamarker1:X 3Mhz:TRACe 2") #This command sets the Detector positive autopeak 

    # etl.write("CALCulate1:DELTamarker2:X -3Mhz:TRACe 2") #This command sets the Detector positive autopeak 

    # etl.write("CALCulate1:DELTamarker3:X 3.15Mhz:TRACe 2") #This command sets the Detector positive autopeak 

    # etl.write("CALCulate1:DELTamarker4:X -3.15Mhz:TRACe 2") #This command sets the Detector positive autopeak 


    # etl.write("SWE:TIME 1s") #Defines the sweep time to 1s
    # print("Sweep time setted to 20ms")

    # etl.write("SET:TV:MODE DTV")  #Set equipment to Digital TV mode
    # print("Setted mode to DTV")

   
    # etl.write("BAND:VID 10kHz") #Set VBW - Video Bandwith 
    # print("VBW set to 1kHz")

    # etl.write("BAND 300Hz") #Set RBW - Resolution Bandwith 
    # print("RBW set to 1MHz")
    

#     etl.write("FREQ:STAR 20Mhz") #Set the span to 10Mhz 
#     print("Start frequency set to 20MHz")

#     etl.write("FREQ:STOP 2000MHz") #Set the span to 10Mhz 
#     print("Stop frequency set to 2000MHz")

#     etl.write("FREQ:SPAN 20Mhz") #Set the span to 10Mhz 
#     print("Span setted to 20MHz")

# #     result = etl.query("SWE:COUN:CURR?") #Asks for current sweep
# #     print(result)

#     etl.write("SWE:POIN 501") #Defines the number of sweeps points to 501
#     print("Sweep points setted to 501")
    
except pyvisa.VisaIOError as error:
    print("Connection Error:", error)

finally:
    if etl:
        etl.close()
