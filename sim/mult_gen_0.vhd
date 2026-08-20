
library ieee;         
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity mult_gen_0 is
	port (
		P : out std_logic_vector(35 downto 0);
		CLK : in std_logic;
		A : in std_logic_vector(17 downto 0);
		B : in std_logic_vector(17 downto 0)
	);
end entity;


architecture arch_mult_gen_0 of mult_gen_0 is

begin


assert false
report "Don't use this file in synthesis"
severity error;

process(clk)
begin
	if rising_edge(CLK) then
		P <= std_logic_vector(unsigned(A)*unsigned(B));
	end if;
end process;

end architecture;