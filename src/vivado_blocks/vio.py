
class vio:
    """Class to generate the clock wizard.

    """
    LIBRARIES = """
library ieee;         
use ieee.std_logic_1164.all;
"""

    def generate_vio_file(self, json_file):
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
      boundary =  data["ip_inst"]["boundary"]["ports"]
      
      in_ports = []
      out_ports = []
      cont = 0

      for i in boundary:
        if boundary[i][0]["direction"] == "in":
          # Add to the input array
          
          if i == "clk":
                in_ports.append([i, '0'])
          else:
                in_ports.append([i, boundary[i][0]["size_left"]])
                   
        else:
          # Add to the output array
          out_ports.append([i, boundary[i][0]["size_left"]])

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
      
      # Constant assignation
      data += "\n\nbegin\n\n"

      data += """\nassert false\nreport "Don't use this file in synthesis"\nseverity error;"""
    
      num = int(json_file["ip_inst"]["parameters"]["component_parameters"]["C_NUM_PROBE_OUT"][0]["value"])


      data += "\n\n\n"

      for i in range(num):
        probe = "C_PROBE_OUT" + str(i) + "_INIT_VAL"
        value = json_file["ip_inst"]["parameters"]["model_parameters"][probe][0]["value"]




        val = int(value, 16)

        data += "\n\t" + self.out_ports[i][0] + " <= "

        if val == 0:
           if self.out_ports[i][1] == '0':
              data += "\'0\';"
           else:
              data += "(others=>'0');"
            

        else:
            data += "\"" + bin(val)[2:].zfill(int(self.out_ports[i][1])+1) + "\";"



      data += "\n\n\nend architecture;"

      # Return data
      return data
    