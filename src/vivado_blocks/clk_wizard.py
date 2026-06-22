
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

      data = "\n\nentity " + json_file["clocking_wizard"]["name"] + " is\n\tport (\n"

      # inputs
      for i in json_file["clocking_wizard"]["inputs"]:
        data += "\t\t" + i["name"] + " : in std_logic;\n"

      # outputs
      for i in json_file["clocking_wizard"]["outputs"]:
        data += "\t\t" + i["name"] + " : out std_logic;\n"

      # reset
      if json_file["clocking_wizard"]["reset"]["enable"] == True:
        data += "\n\t\treset : out std_logic;"

      # lock
      if json_file["clocking_wizard"]["lock"]["enable"] == True:
        data += "\n\t\tlocked : out std_logic"

      data += "\n\t);\nend entity;\n"
          
      # Return data
      return data
    



    def generate_architecture(self, json_file):
      """Method with the architecture information.

      Args:
          json_file (array): Array with the JSON data.

      Returns:
          string: string with the architecture of the clocking wizard.
      """
      data = "\n\narchitecture arch_" + json_file["clocking_wizard"]["name"] + " of "+ json_file["clocking_wizard"]["name"] +" is\n\n" 
      
      # Constant assignation
      data += self.constant_time_clock(json_file) + "\n\nbegin\n\n"
      
      # Clock generation
      for i in range(len(json_file["clocking_wizard"]["outputs"])):
        data += self.genarate_clock(json_file, i)

      # Reset generation
      if json_file["clocking_wizard"]["reset"]["enable"] == True:
        data += self.generate_reset(json_file)

      # Lock generation
      if json_file["clocking_wizard"]["lock"]["enable"] == True:
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
      for i in range(len(json_file["clocking_wizard"]["outputs"])):
        data += "\n\tconstant " + self.get_constant_name(json_file, i) + " : time := " + str((1/json_file["clocking_wizard"]["outputs"][i]["frequency_mhz"])*1000/2) + " ns;"

      # Return data
      return data




    def get_constant_name(self, json_file, num):
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
      data = "C_PERIOD_" + json_file["clocking_wizard"]["outputs"][num]["name"].upper()

      # Return data
      return data




    def genarate_clock(self, json_file, num):
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
      port = json_file["clocking_wizard"]["outputs"][num]["name"]

      data = """\n    
----------------------------------------------------------------
-- """ + port + """
---------------------------------------------------------------- """
      data += "\n\tprocess begin\n\t\t"
      
      # clock string
      data += port + " <= '1';\n\t\twait for " + self.get_constant_name(json_file, num) + ";\n\t\t" + port + " <= '1';\n\t\twait for " + self.get_constant_name(json_file, num) + ";"

      data += "\n\tend process;\n\n"

      # Return data
      return data
    



    def generate_reset(self, json_file):
      """Method to generate the reset of the clocking wizard.

      Reset example:
      
      	process begin
          reset <= '0';
          wait for 50 ns;
          reset <= '1';
          wait;
        end process;

      Args:
          json_file (array): Array with the JSON data.

      Returns:
          string: string with the reset.
      """
      data = """\n    
----------------------------------------------------------------
-- RESET
---------------------------------------------------------------- """
      # reset string
      data += "\n\tprocess begin\n\t\treset <= '0';\n\t\twait for " + str(json_file["clocking_wizard"]["reset"]["reset_time_ns"]) + " ns;\n\t\treset <= '1';\n\t\twait;\n\tend process;\n\n"
      
      # Return data
      return data

    


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
      data += "\n\tprocess begin\n\t\tlocked <= '0';\n\t\twait for " + str(json_file["clocking_wizard"]["lock"]["lock_time_ns"]) + " ns;\n\t\tlocked <= '1';\n\t\twait;\n\tend process;\n\n"
      
      # Return data
      return data
    
