
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity blk_mem_gen_0 is
  port (
    douta : out std_logic_vector(15 downto 0);
    clka  : in std_logic;
    ena   : in std_logic;
    wea   : in std_logic;
    addra : in std_logic_vector(3 downto 0);
    dina  : in std_logic_vector(15 downto 0)
  );
end entity;
architecture arch_blk_mem_gen_0 of blk_mem_gen_0 is
  type ram_type is array (0 to 16 - 1)
  of std_logic_vector(15 downto 0);
  signal RAM : ram_type := (others => (others => '0'));

begin
  assert false
  report "Don't use this file in synthesis"
    severity error;
  douta <= ram(to_integer(unsigned(addra)));
  process (clka)
  begin
    if rising_edge(clka) then
      if ena = '1' then
        if wea = '1' then
          RAM(to_integer(unsigned(addra))) <= dina;
        end if;
      end if;
    end if;
  end process;
end architecture;