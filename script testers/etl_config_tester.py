class AnalyzerConfigurator:
    def __init__(self, analyzer_type, analyzer):
        self.analyzer_type = analyzer_type
        self.analyzer = analyzer

    def identify(self):
        identification = self.analyzer.query("*IDN?")
        print("Analyzer Identification:", identification)

    def set_common_configurations(self):
        self.analyzer.write("SENSe1:DETector1:FUNCtion POS")          
        self.analyzer.write("DISPlay:TRACe1:Y:SCALe:RLEVel -20") 

    def set_tv_radio_configurations(self):
        self.analyzer.write("SET:TV:STAN ISDBT")
        print("Set mode to ISDBT")
        self.analyzer.write("BAND:VID 300Hz")
        print("VBW set to 300Hz")
        self.analyzer.write("BAND 10kHz")
        print("RBW set to 10kHz")
        self.analyzer.write("FREQ:SPAN 20Mhz")
        print("Span set to 20MHz")
        self.analyzer.write("SET:TV:MODE DTV")
        print("Set mode to DTV")
        self.analyzer.write("SWE:POIN 501")
        print("Sweep points set to 501")

    def set_spectrum_configurations(self):
        self.analyzer.write("SENSe1:DETector1:FUNCtion POS")
        print("Detector positive autopeak")
        self.analyzer.write("DISPlay:TRACe1:Y:SCALe:RLEVel 0")
        print("Amplitude ref level set to 0")
        self.analyzer.write("SENSe1:FREQuency:CENTer 581.142857Mhz")
        print("Center frequency set to 581.142857Mhz")
        self.analyzer.write("SWE:TIME 10")
        print("Sweep time set to 10s")

    def set_spectrum_markers(self):
        self.analyzer.write("CALCulate1:DELTamarker1:FUNCtion:FIXed:STATe OFF")
        self.analyzer.write("CALCulate1:MARK1:X 581.142857Mhz") #This command sets the center Marker 
        self.analyzer.write("CALCulate1:DELTamarker1:X -2.79Mhz") #This command sets Marker 1
        self.analyzer.write("CALCulate1:DELTamarker2:X 2.79Mhz") #This command sets Marker 2
        self.analyzer.write("CALCulate1:DELTamarker4:X 2.86Mhz") #This command sets Marker 4 
        self.analyzer.write("CALCulate1:DELTamarker3:X -2.86Mhz") #This command sets Marker 3
