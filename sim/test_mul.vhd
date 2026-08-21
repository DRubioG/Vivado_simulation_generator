
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity mult_gen_0_tb is
end;

architecture bench of mult_gen_0_tb is
COMPONENT mult_gen_0
  PORT (
    CLK : IN STD_LOGIC;
    A : IN STD_LOGIC_VECTOR(17 DOWNTO 0);
    B : IN STD_LOGIC_VECTOR(17 DOWNTO 0);
    CE : IN STD_LOGIC;
    SCLR : IN STD_LOGIC;
    P : OUT STD_LOGIC_VECTOR(12 DOWNTO 0) 
  );
END COMPONENT;
  -- Clock period
  constant clk_period : time := 5 ns;
  -- Generics
  -- Ports
  signal P : std_logic_vector(12 downto 0);
  signal CLK : std_logic:='0';
  signal A : std_logic_vector(17 downto 0);
  signal B : std_logic_vector(17 downto 0);
  signal CE : std_logic;
  signal SCLR : std_logic;
begin

  mult_gen_0_inst : mult_gen_0
  port map (
    P => P,
    CLK => CLK,
    A => A,
    CE => CE,
    SCLR => SCLR,
    B => B
  );

  CE <= '1';

  SCLR <= '0', '1' after 100 ns;
clk <= not clk after clk_period/2;
A <= (0=>'1', others => '0');
B <= ((others => '1') );

end;