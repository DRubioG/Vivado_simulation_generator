
library ieee;         
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity c_counter_binary_0 is
	port (
		Q : out std_logic_vector(10 downto 0);
		CLK : in std_logic;
		CE : in std_logic
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
if CE = '1' then
r_cont <= r_cont - x"6";
end if;
end if;
  end process;


end architecture;