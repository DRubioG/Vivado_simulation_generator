from vivado_blocks.clk_wizard import *


class simulator_generator:
    """Class that selects the option to generate the file.
    """
    def __init__(self):
        """Constructor of the class.
        """
        self.clk_wiz = clk_wizard()
        pass


    def simulator_generator(self, json_file):
        """This method selects which IP block is used.

        Args:
            json_file (array): array with the JSON data.
        """
        if "clocking_wizard" in json_file:
            self.generate_clocking_wizard(json_file)



    def generate_clocking_wizard(self, json_file):
        """This method calls the clocking wizard class to generate the file.

        Args:
            json_file (array): array wuth the JSON data.
        """
        name = json_file["clocking_wizard"]["name"]
        file = open(name+".vhd", "w")
        clock_wizard_data = self.clk_wiz.generate_clock_file(json_file)
        file.write(clock_wizard_data) 
        file.close()


# Vio


# Ila



# block memory generator



# concat


# constant


# Binary counter


# Distributed Memory Generator



# oddr


# RAM-based shift register


# Slice

# Utility idelay Control


# Utility buffer

# Utility Reduced Logic

# Utitlity Vector Logic


# DDS Compiler


# xpm_cdc


# adder/substracter

# cordic



# Divider Generator


# Floating-Point

# Multiplier




# JESD204



