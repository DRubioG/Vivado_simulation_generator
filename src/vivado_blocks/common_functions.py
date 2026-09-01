

def generate_entity( json_file):
      """This method generates the entity information.

      Args:
          json_file (array): Array with the JSON data.

      Returns:
          string: string with the entity of the clocking wizard.
      """

      data = "\n\nentity " + json_file["ip_inst"]["xci_name"] + " is\n\tport ("

      # Gets the ports
      in_ports, out_ports = get_ports(json_file)
      cont = 0

      # outputs
      for i in out_ports:
        data += "\n\t\t" + i[0] + " : out std_logic"
        # add the final of the vector
        if int(i[1]) != 0:
           data += "_vector(" + i[1] + " downto 0)"
        data += ";"

        
      cont = 0
      #input ports
      for i in in_ports:
        cont += 1
        data += "\n\t\t" + i[0] + " : in std_logic"
        # add the final of the vector
        if int(i[1]) != 0:
           data += "_vector(" + i[1] + " downto 0)"
        # add the ';' at the end when it is necessary.
        if cont != len(in_ports):
          data += ";"    

      data += "\n\t);\nend entity;\n"
          
      # Return data
      return data

    
def get_ports( data):
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
          
          if "size_left" in ports[i][0]:
                in_ports.append([i, ports[i][0]["size_left"]])
          else:
               in_ports.append([i, '0'])
                   
        else:
          # Add to the output array

            if "size_left" in ports[i][0]:
                out_ports.append([i, ports[i][0]["size_left"]])
            else:
                out_ports.append([i, '0'])

        cont += 1
      # Return the arrays
      return in_ports, out_ports
