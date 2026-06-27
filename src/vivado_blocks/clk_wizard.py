
class clk_wizard:
    """Class to generate the clock wizard.

    """
    LIBRARIES = """
library ieee;         
use ieee.std_logic_1164.all;
"""


    def generate_clock_file(self, json_file):
      """This method generates the output file.

      Args:
          json_file (array): Array with the information.

      Returns:
          string: clock wizard data.
      """
      
      # Add libraries
      data = self.LIBRARIES

      
      self.num_freqs = int(json_file["ip_inst"]["parameters"]["component_parameters"]["NUM_OUT_CLKS"][0]["value"])

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
        cont += 1
        data += "\n\t\t" + i + " : out std_logic;"     

      #input ports
      for i in self.in_ports:
        cont += 1
        data += "\n\t\t" + i + " : in std_logic"
        if cont != len(self.in_ports)+len(self.out_ports):
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

      for i in boundary:
        if boundary[i][0]["direction"] == "in":
          # Add to the input array
          in_ports.append(i)
        else:
          # Add to the output array
          out_ports.append(i)

      # Return the arrays
      return in_ports, out_ports
    


    def generate_architecture(self, json_file):
      """Method with the architecture information.

      Args:
          json_file (array): Array with the JSON data.

      Returns:
          string: string with the architecture of the clocking wizard.
      """
      data = "\n\narchitecture arch_" + json_file["ip_inst"]["xci_name"] + " of "+ json_file["ip_inst"]["xci_name"] +" is\n\n" 
      
      # Constant assignation
      data += self.constant_time_clock(json_file) + "\n\nbegin\n\n"

      data += """\nassert false\nreport "Don't use this file in synthesis"\nseverity error;"""
      

      self.generate_reset(json_file)

      # Clock generation
      for i in self.out_ports:
        if i.find("clk") != -1:
          data += self.generate_clock(json_file, i)

      # Lock generation
      for i in self.out_ports:
        if i == "locked":
          data += self.generate_lock(json_file)

      data += "\nend architecture;"

      # Return data
      return data
    



    def constant_time_clock(self, json_file):
      """Method to generate the time constant.

      Return:
      constant C_PERIOD_<port name> : time := 5.0 ns;

      Args:
          json_file (array): Array with the JSON data.

      Returns:
          string: string with the time constant.
      """
      # constants string
      data = ""

      freqs = self.get_freqs(json_file)

      cont = 0
      for i in freqs:
        data += "\n\tconstant " + self.get_constant_name(self.out_ports[cont]) + " : time := " + str(int(((1/i)*1000/2) * 100) / 100) + " ns;"
        cont += 1
      # Return data
      return data



    def get_freqs(self, json_file):
      """This method gets the frequencies of the clocking wizard.

      Args:
          json_file (array): array with the JSON data.

      Returns:
          array: array with the frequencies.
      """
      freqs = []

      for i in range(self.num_freqs):
        freq_name = "CLKOUT" + str(i+1) + "_REQUESTED_OUT_FREQ"
        freqs.append(float(json_file["ip_inst"]["parameters"]["component_parameters"][freq_name][0]["value"]))

      # Return de frequencies.
      return freqs


    def get_constant_name(self, num):
      """Method to generate the name of the time constant.

      Return:
      C_PERIOD_<port name>
      
      Args:
          json_file (array): Array with the JSON data.
          num (int): position of the constant.

      Returns:
          string: string with the constant name.
      """
      # period string
      data = "C_PERIOD_" + num.upper()

      # Return data
      return data




    def generate_clock(self, json_file, num):
      """Method to generate the clocks of the clocking wizard.
      
      Example clock:

      	process begin
          clk_out3 <= '1';
          wait for C_PERIOD_CLK_OUT3;

          clk_out3 <= '1';
          wait for C_PERIOD_CLK_OUT3;
        end process;


      Args:
          json_file (array): Array with the JSON data.
          num (int): clock position.

      Returns:
          string: string with the clock.
      """
      port = num

      data = """\n    
----------------------------------------------------------------
-- """ + port + """
---------------------------------------------------------------- """
      data += "\n\tprocess begin"

      if self.reset:
        data += "\n\t\twhile true loop"
        data += "\n\t\t\tif reset = " + self.reset_value + " then"
        data += "\n\t\t\t\t" + port + " <= \'0\';"
        data += "\n\t\t\t\twait for 825 ns;"
        data += "\n\t\t\telse"

      data += "\n\t\t\t" + port + " <= '1';"
      data += "\n\t\t\twait for " + self.get_constant_name(num) + ";"
      data += "\n\t\t\t" + port + " <= '0';"
      data += "\n\t\t\twait for " + self.get_constant_name(num) + ";"

      if self.reset:
        data += "\n\t\t\tend if;"
        data += "\n\t\tend loop;"
      data += "\n\tend process;\n\n"

      # Return data
      return data
    



    def generate_reset(self, json_file):
      """Method to analyze the reset and modifies the properties.
      
      Args:
          json_file (array): Array with the JSON data.
          
      """

      self.reset = False
      # Reset generation
      for i in self.in_ports:
        if i == "reset":
          self.reset = True
          if json_file["ip_inst"]["boundary"]["interfaces"]["reset"]["parameters"]["POLARITY"][0]["value"] == "ACTIVE_LOW":
            self.reset_value = "\'0\'"
          else:
            self.reset_value = "\'1\'"
          break

    


    def generate_lock(self, json_file):
      """Method to generate the lock of the clocking wizard.
      
      Lock example:

      	process begin
          locked <= '0';
          wait for 120 ns;
          locked <= '1';
          wait;
        end process;

      Args:
          json_file (array): Array with the JSON data.

      Returns:
          string: string with the lock.
      """
      data = """\n    
----------------------------------------------------------------
-- LOCKED
---------------------------------------------------------------- """
      # lock string
      data += "\n\tprocess begin"
      data += "\n\t\tlocked <= '0';"
      if self.reset:
        data += "\n\t\twait until reset=" + self.reset_value + ";"
        data += "\n\t\twait for 912.5 ns;"

      data += "\n\t\tlocked <= '1';\n\t\twait;\n\tend process;\n\n"
      
      # Return data
      return data
    
