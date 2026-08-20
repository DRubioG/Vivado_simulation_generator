

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
      data = "\n\narchitecture arch_" + json_file["ip_inst"]["xci_name"] + " of "+ json_file["ip_inst"]["xci_name"] +" is" 

      data += "\n\tsignal r_cont : unsigned(Q'range) := (others=>'0');"

      
      # Constant assignation
      data += "\n\nbegin\n\n"

      data += """\nassert false\nreport "Don't use this file in synthesis"\nseverity error;"""

      data += """

  Q <= std_logic_vector(r_cont);
  \n\n\tprocess (clk)
  begin
    if rising_edge(clk) then"""
      if self.sclr_enable:
        data += "\nif SCLR = '0' then"
      
      if self.ce_enable:
         data += "\nif CE = '1' then"

      data += """\nr_cont <= r_cont """
      if self.direction == "UP":
         data += "+"
      else:
         data += "-"

      data += """ x\"""" + self.increment + """\";"""


      if self.ce_enable:
         data += "\nend if;"

      if self.sclr_enable:
         data += """
      else
        r_cont <= (others => '0');
      end if;"""

      data += """\nend if;
  end process;"""

      if self.sync_threshold:
         data += 	"\n\n\tTHRESH0 <= '1' when r_cont = x\"" + self.threshold_value + "\" else '0';"
      
      data += "\n\nend architecture;"

      # Return data
      return data
    