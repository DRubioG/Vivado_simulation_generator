
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

      self.in_ports = self.get_ports(json_file)
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
      """ This method returns an array with the name of the port and the size of the port.

      Structure:
      [<name>, <MSB bit>]
      In string format.

      Returns:
        array: array with the port and MSB bit.
      
      """
      boundary =  data["ip_inst"]["boundary"]["ports"]
      
      in_ports = []

      for i in boundary:
        # Check if the port is the clock of the ILA. That because the 
        # clock doesn't have the all the fields.
        if i == "clk":
            in_ports.append([i, '0'])
        else:
            in_ports.append([i, boundary[i][0]["size_left"]])

        # Return input ports
      return in_ports



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
    
