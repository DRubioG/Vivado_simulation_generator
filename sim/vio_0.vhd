
library ieee;         
use ieee.std_logic_1164.all;


entity vio_0 is
	port (
		probe_out0 : out std_logic;
		probe_out1 : out std_logic;
		probe_out2 : out std_logic_vector(13 downto 0);
		probe_out3 : out std_logic;
		probe_out4 : out std_logic_vector(13 downto 0);
		probe_out5 : out std_logic;
		probe_out6 : out std_logic;
		clk : in std_logic;
		probe_in0 : in std_logic;
		probe_in1 : in std_logic;
		probe_in2 : in std_logic_vector(64 downto 0);
		probe_in3 : in std_logic_vector(13 downto 0);
		probe_in4 : in std_logic_vector(13 downto 0);
		probe_in5 : in std_logic;
		probe_in6 : in std_logic
	);
end entity;


architecture arch_vio_0 of vio_0 is

begin


assert false
report "Don't use this file in synthesis"
severity error;



	probe_out0 <= '0';
	probe_out1 <= '0';
	probe_out2 <= "00000000001111";
	probe_out3 <= '0';
	probe_out4 <= (others=>'0');
	probe_out5 <= '0';
	probe_out6 <= '0';


end architecture;