import os
from vivado_blocks.clk_wizard import *
from vivado_blocks.ila import *
from vivado_blocks.vio import *
from vivado_blocks.block_memory_generator import *


class simulator_generator:
    """Class that selects the option to generate the file.
    """
    def __init__(self):
        """Constructor of the class.
        """
        self.clk_wiz = clk_wizard()
        self.ila = ila()
        self.vio = vio()
        self.block_memory_generator = block_memory_generator()
        self.sim_folder = True
        pass


    def simulator_generator(self, json_file, sim_folder = True):
        """This method selects which IP block is used.

        Args:
            json_file (array): array with the JSON data.
        """
        self.sim_folder = sim_folder
        if json_file["ip_inst"]["component_reference"].find("clk_wiz") != -1:
            self.generate_clocking_wizard(json_file)
        elif json_file["ip_inst"]["component_reference"].find("ila") != -1:
            self.generate_ila(json_file)
        elif json_file["ip_inst"]["component_reference"].find("vio") != -1:
            self.generate_vio(json_file)
        elif json_file["ip_inst"]["component_reference"].find("blk_mem_gen") != -1:
            self.generate_block_memory_generator(json_file)



    def generate_clocking_wizard(self, json_file):
        """This method calls the clocking wizard class to generate the file.

        Args:
            json_file (array): array with the JSON data.
        """
        name = json_file["ip_inst"]["xci_name"]
        if self.sim_folder:
            os.makedirs("sim", exist_ok=True)
            file = open("sim/"+name+".vhd", "w")
        else:
            file = open(name+".vhd", "w")

        clock_wizard_data = self.clk_wiz.generate_clock_file(json_file)
        file.write(clock_wizard_data) 
        file.close()


# Vio

    def generate_vio(self, json_file):
        """This method calls the vio class to generate the file.

        Args:
            json_file (array): array with the JSON data.
        """
        name = json_file["ip_inst"]["xci_name"]
        if self.sim_folder:
            os.makedirs("sim", exist_ok=True)
            file = open("sim/"+name+".vhd", "w")
        else:
            file = open(name+".vhd", "w")

        vio_data = self.vio.generate_vio_file(json_file)
        file.write(vio_data) 
        file.close()


# Ila

    def generate_ila(self, json_file):
        """This method generates the ila simulation file

        Args:
            json_file (array): array with the jSON data.
        """
        name = json_file["ip_inst"]["xci_name"]
        if self.sim_folder:
            os.makedirs("sim", exist_ok=True)
            file = open("sim/"+name+".vhd", "w")
        else:
            file = open(name+".vhd", "w")

        ila_data = self.ila.generate_ila_file(json_file)
        file.write(ila_data) 
        file.close()



# block memory generator

    def generate_block_memory_generator(self, json_file):
        """This method generates the block memory generator simulation file

        Args:
            json_file (array): array with the jSON data.
        """
        name = json_file["ip_inst"]["xci_name"]
        if self.sim_folder:
            os.makedirs("sim", exist_ok=True)
            file = open("sim/"+name+".vhd", "w")
        else:
            file = open(name+".vhd", "w")

        block_memory_generator_data = self.block_memory_generator.generate_block_memory_generator_file(json_file)
        file.write(block_memory_generator_data) 
        file.close()



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


