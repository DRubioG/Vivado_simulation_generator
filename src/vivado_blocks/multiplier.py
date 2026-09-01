from vivado_blocks.common_functions import *


class Multiplier:
    """Class to generate the VIO file.
 
    """
    LIBRARIES = """
library ieee;         
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

"""
    def generate_multiplier(self, json_file):
      """This method generates the output file.

      Args:
          json_file (array): Array with the information.

      Returns:
          string: file data.
      """
      self.output_width = json_file["ip_inst"]["parameters"]["component_parameters"]["Use_Custom_Output_Width"][0]["value"] == "true"
      self.width_high = json_file["ip_inst"]["parameters"]["component_parameters"]["OutputWidthHigh"][0]["value"]
      self.width_low = json_file["ip_inst"]["parameters"]["component_parameters"]["OutputWidthLow"][0]["value"]
      self.ce_enable = json_file["ip_inst"]["parameters"]["component_parameters"]["ClockEnable"][0]["value"] == "true"
      self.sclr_enable = json_file["ip_inst"]["parameters"]["component_parameters"]["SyncClear"][0]["value"] == "true"
      self.ce_priority = json_file["ip_inst"]["parameters"]["component_parameters"]["SclrCePriority"][0]["value"] == "SCLR_Overrides_CE"

     
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
      # Architecture start
      data = "\n\narchitecture arch_" + json_file["ip_inst"]["xci_name"] + " of "+ json_file["ip_inst"]["xci_name"] +" is" 

      # Signals
      data += "\n\tsignal P_aux : std_logic_vector(A'length+B'length-1 downto 0);"

      
      # Constant assignation
      data += "\n\nbegin\n\n"

      # Safety report
      data += """\nassert false\nreport "Don't use this file in synthesis"\nseverity error;"""

      data += "\n\n\tP <= P_aux"
      # Slice data
      if self.output_width:
        data += "(" + self.width_high + " downto " + self.width_low + ")"
      data += ";"

      data += "\n\nprocess(clk)\nbegin\n\tif rising_edge(CLK) then"


      if self.ce_priority:
        # Synchronous Clear (SCLR)
        if self.sclr_enable:
          data += "\nif SCLR = '0' then"

        # Clock Enable (CE)
        if self.ce_enable:
          data += "\nif CE = '1' then"

      else:
        # Clock Enable (CE)
        if self.ce_enable:
          data += "\nif CE = '1' then"

        # Synchronous Clear (SCLR)
        if self.sclr_enable:
          data += "\nif SCLR = '0' then"

      # Multiplier
      data += "\nP_aux <= std_logic_vector(unsigned(A)*unsigned(B));"


      if self.ce_priority:
        # Clock Enable (CE)
        if self.ce_enable:
            data += "\nend if;"

        # Synchronous Clear (SCLR)
        if self.sclr_enable:
            data += "\n\t\t\t\telse\n\t\t\t\t\tP_aux <= (others => '0');\n\t\t\t\tend if;"

      else:
        # Synchronous Clear (SCLR)
        if self.sclr_enable:
            data += "\n\t\t\t\telse\n\t\t\t\t\tP_aux <= (others => '0');\n\t\t\t\tend if;"
        
        # Clock Enable (CE)
        if self.ce_enable:
            data += "\nend if;"
        
         
      data += "\n\t\nend if;end process;"
      
      data += "\n\nend architecture;"

      # Return data
      return data
    