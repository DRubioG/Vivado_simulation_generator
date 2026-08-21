
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity mult_gen_0 is
  port (
    P    : out std_logic_vector(12 downto 0);
    CLK  : in std_logic;
    A    : in std_logic_vector(17 downto 0);
    B    : in std_logic_vector(17 downto 0);
    CE   : in std_logic;
    SCLR : in std_logic
  );
end entity;
architecture arch_mult_gen_0 of mult_gen_0 is
  signal P_aux : std_logic_vector(A'length + B'length - 1 downto 0);

begin
  assert false
  report "Don't use this file in synthesis"
    severity error;

  P <= P_aux(12 downto 0);

  process (clk)
  begin
    if rising_edge(CLK) then
      if SCLR = '0' then
        if CE = '1' then
          P_aux <= std_logic_vector(unsigned(A) * unsigned(B));
        end if;
      else
        P_aux <= (others => '0');
      end if;
    end if;
  end process;

end architecture;