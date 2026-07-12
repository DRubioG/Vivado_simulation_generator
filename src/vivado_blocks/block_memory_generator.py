

class block_memory_generator:
    LIBRARIES = """
library ieee;         
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
"""

    def generate_block_memory_generator_file(self, json_file):
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
          
          if len(ports[i][0]) <= 2:
                in_ports.append([i, '0'])
          else:
                in_ports.append([i, ports[i][0]["size_left"]])
                   
        else:
          # Add to the output array
          out_ports.append([i, ports[i][0]["size_left"]])

        cont += 1
      # Return the arrays
      return in_ports, out_ports
    



    def generate_architecture(self, json_file):
      """Method with the architecture information.

      Args:
          json_file (array): Array with the JSON data.

      Returns:
          string: string with the architecture.
      """
      data = "\n\narchitecture arch_" + json_file["ip_inst"]["xci_name"] + " of "+ json_file["ip_inst"]["xci_name"] +" is\n\n" 
      
      data += self.generate_signals(json_file=json_file)
      
      data += "\n\nbegin\n\n"

      data += """\nassert false\nreport "Don't use this file in synthesis"\nseverity error;"""
      
      data += self.generate_process(json_file)
      
      data += "\nend architecture;"

      # Return data
      return data
    

    def generate_signals(self, json_file):
        """Method to generate the signals.

        Args:
            json_file (array): Array with the JSON data.

        Returns:
            string: string with the signals.
        """
       
        for i in self.in_ports:
            if i[0] == "dina":
                addr_width = i[1]
                break
        
        depth = json_file["ip_inst"]["parameters"]["component_parameters"]["Write_Width_A"][0]["value"]

        data = "\n\ttype ram_type is array (0 to " + depth + "-1)"
        data += "\n\t\tof std_logic_vector(" + addr_width + " downto 0);"

        if json_file["ip_inst"]["parameters"]["component_parameters"]["Memory_Type"][0]["value"].find("RAM") != -1:
            data += "\n\tsignal RAM : ram_type := (others => (others => '0'));"
        else:
            data += "\n\tsignal ROM : ram_type := (others => (others => '0'));"

        return data
    
    def generate_process(self, json_file):
        """Method to generate the process.

        Args:
            json_file (array): Array with the JSON data.

        Returns:
            string: string with the process.
        """
        data = ""
        # Single_Port_RAM
        if json_file["ip_inst"]["parameters"]["component_parameters"]["Memory_Type"][0]["value"] == "Single_Port_RAM":
            data += "\n\n\n\tdouta <= ram(to_integer(unsigned(addra)));"
            data += "\n\tprocess(clka)"
            data += "\n\tbegin"
            data += "\n\t\tif rising_edge(clka) then"
            data += "\n\t\t\tif ena = '1' then"
            data += "\n\t\t\t\tif wea = '1' then"
            data += "\n\t\t\t\t\tRAM(to_integer(unsigned(addra))) <= dina;"
            data += "\n\t\t\t\tend if;"
            data += "\n\t\t\tend if;"
            data += "\n\t\tend if;"
            data += "\n\tend process;"
            data += "\n\n"
        
        # Simple_Dual_Port_RAM
        elif json_file["ip_inst"]["parameters"]["component_parameters"]["Memory_Type"][0]["value"] == "Simple_Dual_Port_RAM":
            data += "\n\n\n\tprocess(clka)"
            data += "\n\tbegin"
            data += "\n\t\tif rising_edge(clka) then"
            data += "\n\t\tif wea = '1' then"
            data += "\n\t\t\tRAM(to_integer(unsigned(addra))) <= dina;"
            data += "\n\t\tend if;"
            data += "\n\n\t\tdoutb <= RAM(to_integer(unsigned(addrb)));"
            data += "\n\tend if;"
            data += "\n\tend process;"
            data += "\n\n"


        # True_Dual_Port_RAM
        elif json_file["ip_inst"]["parameters"]["component_parameters"]["Memory_Type"][0]["value"] == "True_Dual_Port_RAM":
            data += "\n\n\n\tprocess(clka)"
            data += "\n\tbegin"
            data += "\n\t\tif rising_edge(clka) then"
            data += "\n\t\t-- A"
            data += "\n\t\t\tif wea = '1' then"
            data += "\n\t\t\t\tRAM(to_integer(unsigned(addra))) <= dina;"
            data += "\n\t\t\tend if;"
            data += "\n\t\t\tdouta <= RAM(to_integer(unsigned(addra)));"
            data += "\n\t\t\t-- B"
            data += "\n\t\t\tif web = '1' then"
            data += "\n\t\t\t\tRAM(to_integer(unsigned(addrb))) <= dinb;"
            data += "\n\t\t\tend if;"
            data += "\n\t\t\tdoutb <= RAM(to_integer(unsigned(addrb)));"
            data += "\n\t\tend if;"
            data += "\n\tend process;"
            data += "\n\n"
            

        # Single_Port_ROM
        elif json_file["ip_inst"]["parameters"]["component_parameters"]["Memory_Type"][0]["value"] == "Single_Port_ROM":
            data += "\n\n\n\tprocess(clka)"
            data += "\n\t\tbegin"
            data += "\n\t\t\tif rising_edge(clka) then"
            data += "\n\t\t\t\tdouta <= ROM(to_integer(unsigned(addra)));"
            data += "\n\t\t\tend if;"
            data += "\n\tend process;"
            data += "\n\n"
    
        # Dual_Port_ROM
        elif json_file["ip_inst"]["parameters"]["component_parameters"]["Memory_Type"][0]["value"] == "Dual_Port_ROM":
            data += "\n\n\n\tprocess(clka)"
            data += "\n\tbegin"
            data += "\n\t\tif rising_edge(clka) then"
            data += "\n\t\t\tdouta <= ROM(to_integer(unsigned(addra)));"
            data += "\n\t\t\tdoutb <= ROM(to_integer(unsigned(addrb)));"
            data += "\n\t\tend if;"
            data += "\n\tend process;"
            data += "\n\n"

        return data
        
    

    