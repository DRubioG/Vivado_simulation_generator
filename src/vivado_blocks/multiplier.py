
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
      data += self.generate_entity(json_file)

      # Add architecture
      data += self.generate_architecture(json_file)

      # Return data
      return data


    def generate_entity(self, json_file):
      """This method generates the entity information.

      Args:
          json_file (array): Array with the JSON data.

      Returns:
          string: string with the entity of the clocking wizard.
      """

      data = "\n\nentity " + json_file["ip_inst"]["xci_name"] + " is\n\tport ("

      # Gets the ports
      self.in_ports, self.out_ports = self.get_ports(json_file)
      cont = 0

      # outputs
      for i in self.out_ports:
        data += "\n\t\t" + i[0] + " : out std_logic"
        # add the final of the vector
        if int(i[1]) != 0:
           data += "_vector(" + i[1] + " downto 0)"
        data += ";"

        
      cont = 0
      #input ports
      for i in self.in_ports:
        cont += 1
        data += "\n\t\t" + i[0] + " : in std_logic"
        # add the final of the vector
        if int(i[1]) != 0:
           data += "_vector(" + i[1] + " downto 0)"
        # add the ';' at the end when it is necessary.
        if cont != len(self.in_ports):
          data += ";"    

      data += "\n\t);\nend entity;\n"
          
      # Return data
      return data

    
    def get_ports(self, data):
      """This method returns the input and output ports.

      Args:
          data (array): array with the JSON data.

      Returns:
          array: array with two arrays. One for the input and the other for the output.
      """
      ports =  data["ip_inst"]["boundary"]["ports"]
      
      in_ports = []
      out_ports = []
      cont = 0

    # This generates the ports
      for i in ports:
        if ports[i][0]["direction"] == "in":
          # Add to the input array
          
          if i.lower() == "clk" or i.lower() == "ce" or i.lower() == "sclr":
                in_ports.append([i, '0'])
          else:
                in_ports.append([i, ports[i][0]["size_left"]])
                   
        else:
          # Add to the output array
          if i.lower() == "thresh0":
                out_ports.append([i, '0'])
          else:
            out_ports.append([i, ports[i][0]["size_left"]])

        cont += 1
      # Return the arrays
      return in_ports, out_ports



    
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
    