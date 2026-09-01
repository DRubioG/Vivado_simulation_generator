from vivado_blocks.common_functions import *

class ila:
    """Class to generate the clock wizard.

    """
    LIBRARIES = """
library ieee;         
use ieee.std_logic_1164.all;
"""


    def generate_ila_file(self, json_file):
      """This method generates the output file.

      Args:
          json_file (array): Array with the information.

      Returns:
          string: clock wizard data.
      """
      
      # Add libraries
      data = self.LIBRARIES

      # Add entity
      data += generate_entity(json_file)

      # Add architecture
      data += self.generate_architecture(json_file)

      # Return data
      return data





    def generate_architecture(self, json_file):
      """Method with the architecture information.

      Args:
          json_file (array): Array with the JSON data.

      Returns:
          string: string with the architecture of the clocking wizard.
      """
      data = "\n\narchitecture arch_" + json_file["ip_inst"]["xci_name"] + " of "+ json_file["ip_inst"]["xci_name"] +" is\n\n" 
      
      # Constant assignation
      data += "\n\nbegin\n\n"

      data += """\nassert false\nreport "Don't use this file in synthesis"\nseverity error;"""
    

      data += "\n\n\nend architecture;"

      # Return data
      return data
    
