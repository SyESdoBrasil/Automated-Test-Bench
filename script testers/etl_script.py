import pyvisa

rm = pyvisa.ResourceManager()

try:
    etl = rm.open_resource("TCPIP::169.254.200.78::INSTR") 
    etl.timeout = 5000  # Adjust timeout if needed

    identification = etl.query("*IDN?") #Identificates the equipment
    print("ETL Identification:", identification) 
    etl.analyzer.write("SET:TV:STAN ISDBT") #Set ISDBT TV  digital standard

    etl.write("SET:TV:MODE DTV")  #Set equipment to Digital TV mode
    etl.write("INST CATV") # Set intrumental to TV/Radio Analyzer
    etl.write("DISP:ZOOM:OVER") # Connects to the digital TV measurement screen   

    etl.write("DISP:ZOOM:OVER MERRms") # Connects to the digital TV measurement screen   
    etl.write("DISP:MEAS:OVER:TMCC:STAT OFF") # Changes Overview stats to meas   
    etl.write("FREQ:CHAN 22") # set channel to 3

    etl.write("FREQ:CHAN 22")


    
except pyvisa.VisaIOError as error:
    print("Connection Error:", error)

# finally:
#     if etl:
#         etl.close()
