import pyvisa
import datetime

def connect_and_identify_ena(address="TCPIP::10.50.0.81::INSTR"):
  """Connects to the ENA, retrieves identification, and returns the resource.

  Args:
      address: The instrument address (default: "TCPIP::10.50.0.81::INSTR").

  Returns:
      pyvisa.ResourceManager: The connected ENA resource object, or None on failure.
  """
  rm = pyvisa.ResourceManager()
  try:
    ena = rm.open_resource(address)
    ena.timeout = 5000  # Adjust timeout if needed

    identification = ena.query("*IDN?")
    print("ENA Identification:", identification)

    return ena
  except pyvisa.VisaIOError as error:
    print("Connection Error:", error)
    return None

def configure_sweep(ena):
  """Configures sweep parameters for the ENA.

  Args:
      ena: The connected ENA resource object.
  """
  ena.write(":SENS1:SWE:TIME:AUTO ON") #Set sweep time to AUTO"
  print("Set sweep time to AUTO")

  ena.write(":SENS1:SWE:GEN STEP") #Set sweep mode to stepped
  print("Set sweep mode to stepped")

  ena.write(":SENSe:SWEep:POINts 204") #Sweep points set to 204
  print("Sweep points set to 204")

  ena.write(":SENSe:SWEep:DELay 0") #Sweep delay set to 0s"
  print("Sweep delay set to 0s")

  ena.write(":SENS1:SWE:TYPE LIN") #Sweep type set to Linear"
  print("Sweep type set to Linear")

def configure_scale(ena):
  """Configures scale parameters for the ENA.

  Args:
      ena: The connected ENA resource object.
  """
  ena.write(":DISP:WIND1:Y:DIV 12") #Set the Y-axis divions to 10
  print("Set y axis divions to 12")

  ena.write(":DISP:WIND1:TRAC1:Y:PDIV 10") #Set scale/div to 10/db
  print("Set scale/div to 10db")

  ena.write(":DISP:WIND1:TRAC1:Y:RPOS 6") #Set reference value to 6
  print("Set reference value to 6")

  ena.write(":CALC1:CORR:EDEL:TIME 0") #Set eletrical delay to 6
  print("Set eletrical delay to 0")
  
  ena.write(":CALC1:CORR:EDEL:WGC 9E6") #Set cutoff frequency
  print("Set cutoff frequency to 9Khz")

def configure_span(ena):
  """Configures scale parameters for the ENA.
  Args:
      ena: The connected ENA resource object.
  """
  ena.write("SENS1:FREQ:SPAN 10E6") #Set span
  print("Set span")

  ena.write(":SENS1:FREQ:CENT 3E6") #Set center frequency
  print("Set center frequency")

  ena.write(":CALC1:MARK1:ACT") #Create mark 1 
  print("Set marker 1")
  
  ena.write(":CALC1:MARK2:ACT") #Create mark 2 
  print("Set marker 2")
  
  ena.write(":CALC1:MARK1:X 1E6") #Set mark 1 spot
  print("Set marker spot 1")

  ena.write(":CALC1:MARK2:X 1E9") #Set mark 2 spot 
  print("Set marker spot 2")

  # ena.write(":CALC1:MARK1 OFF") #Set marker 1 to off  
  # print("Set marker 1 to off")

def save_ena_screenshot(ena, filename):
    
    """Assumes a valid ENA connection object is passed as 'ena'."""
    try:
        # Generate a dynamic filename with a timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = filename + "_" + timestamp + ".png"
        save_directory = "C:\\Documents and Settings\\TEMP\\Desktop" # Customize save folder
        ena.write(f"MMEM:STOR:IMAG '{save_directory}{filename}'") 
        filepath = save_directory + filename
        print(f"Screenshot saved to: {filepath}")

    except pyvisa.VisaIOError as error:
        print("Communication Error:", error) 

if __name__ == "__main__":
  ena = connect_and_identify_ena()
if ena:
    configure_sweep(ena)
    configure_scale(ena)
    configure_span(ena)
    # *** Take a screenshot after configuration ***
    base_filename = "my_screenshot" 
    save_ena_screenshot(ena, base_filename)
    
    ena.close()
    print("ENA disconnected.")
else:
  print("Failed to connect to ENA.")
