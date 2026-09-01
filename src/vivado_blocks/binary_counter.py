from vivado_blocks.common_functions import *


class Binary_counter:
    """Class to generate the VIO file.
 
    """
    LIBRARIES = """
library ieee;         
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
"""
    def generate_binary_counter_file(self, json_file):
      """This method generates the output file.

      Args:
          json_file (array): Array with the information.

      Returns:
          string: file data.
      """

      self.increment = json_file["ip_inst"]["parameters"]["component_parameters"]["Increment_Value"][0]["value"]
      self.direction = json_file["ip_inst"]["parameters"]["component_parameters"]["Count_Mode"][0]["value"]
      self.ce_enable = json_file["ip_inst"]["parameters"]["component_parameters"]["CE"][0]["value"] == "true"
      self.sclr_enable = json_file["ip_inst"]["parameters"]["component_parameters"]["SCLR"][0]["value"] == "true"
      self.sync_threshold = json_file["ip_inst"]["parameters"]["component_parameters"]["Sync_Threshold_Output"][0]["value"] == "true"
      self.threshold_value = json_file["ip_inst"]["parameters"]["component_parameters"]["Threshold_Value"][0]["value"]

      
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
      data = "\n\narchitecture arch_" + json_file["ip_inst"]["xci_name"] + " of "+ json_file["ip_inst"]["xci_name"] +" is" 

      # Signals
      data += "\n\tsignal r_cont : unsigned(Q'range) := (others=>'0');"

      
      # Constant assignation
      data += "\n\nbegin\n\n"

      # Safety report
      data += """\nassert false\nreport "Don't use this file in synthesis"\nseverity error;"""

      data += """

  Q <= std_logic_vector(r_cont);
  \n\n\tprocess (clk)
  begin
    if rising_edge(clk) then"""
      
      # Synchronous Clear (SCLR)
      if self.sclr_enable:
        data += "\nif SCLR = '0' then"

      # Clock Enable (CE)
      if self.ce_enable:
         data += "\nif CE = '1' then"

      data += """\nr_cont <= r_cont """
      # Count mode
      if self.direction == "UP":
         data += "+"
      else:
         data += "-"

      data += """ x\"""" + self.increment + """\";"""

      # Clock Enable (CE)
      if self.ce_enable:
         data += "\nend if;"

      # Synchronous Clear (SCLR)
      if self.sclr_enable:
         data += """
      else
        r_cont <= (others => '0');
      end if;"""

      data += """\nend if;
  end process;"""

      # Sync Threshold Output
      if self.sync_threshold:
         data += 	"\n\n\tTHRESH0 <= '1' when r_cont = x\"" + self.threshold_value + "\" else '0';"
      
      data += "\n\nend architecture;"

      # Return data
      return data
    