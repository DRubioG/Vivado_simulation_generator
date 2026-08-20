
library ieee;         
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity c_counter_binary_0 is
	port (
		THRESH0 : out std_logic;
		Q : out std_logic_vector(10 downto 0);
		CLK : in std_logic
	);
end entity;


architecture arch_c_counter_binary_0 of c_counter_binary_0 is
	signal r_cont : unsigned(Q'range) := (others=>'0');

begin


assert false
report "Don't use this file in synthesis"
severity error;

  Q <= std_logic_vector(r_cont);
  

process (clk)
  begin
    if rising_edge(clk) then
r_cont <= r_cont + x"2";
end if;
  end process;


	THRESH0 <= '1' when r_cont = x"50" else '0';


end architecture;