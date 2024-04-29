from unittest import TestCase
from unittest.mock import patch, Mock  # Import for mocking
import automated_test_system.etl_controller.etl_commands.etl_config as etl_config  # Import your module
from transmitter_automator import oid_channel_frequency
from pysnmp.error import PySnmpError as SNMPError


class TestAnalyzerConfigurator(TestCase):
    @patch('etl_config.AnalyzerConfigurator.transmitter_controller')
    def test_get_current_channel(self, mock_transmitter_controller):
        # Set up mock return value for get_snmp_data
        mock_transmitter_controller.get_snmp_data.return_value = "591142857"  # Example return value
        
        # Call the method you want to test
        channel_frequency = self.get_current_channel()
        
        # Assertions or further processing based on the returned value
        self.assertEqual(channel_frequency, 591142857)  # Example assertion

    def get_current_channel(self):
        try:
            channel_frequency = etl_config.AnalyzerConfigurator.transmitter_controller.get_snmp_data(oid_channel_frequency)

            if channel_frequency is None:
                print("Error: No channel frequency retrieved")
                return None

            channel_frequency = float(channel_frequency)  # Attempt conversion
            
            if not self.is_valid_channel_frequency(channel_frequency):  # Assuming you have a function for this
                print("Error: Invalid channel frequency:", channel_frequency)
                return None

            print("Channel Frequency:", channel_frequency)
            return channel_frequency

        except ValueError as ve:
            print("Error converting channel frequency to float:", ve)
            return None

        except SNMPError as e:  # Or a more specific SNMP-related exception if applicable
            print("SNMP Error:", e)
            return None
