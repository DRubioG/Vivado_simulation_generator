library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.math_real.all;

entity test_binary_counter is
end entity test_binary_counter;

architecture rtl of test_binary_counter is

  component c_counter_binary_0
    port (
      CLK     : in std_logic;
      Q       : out std_logic_vector(10 downto 0);
      THRESH0 : out std_logic
    );
  end component;

  signal CLK     : std_logic := '0';
  signal THRESH0 : std_logic;
  signal Q       : std_logic_vector(10 downto 0);
  signal SCLR    : std_logic;

begin

  CLK <= not CLK after 5 ns;
  -- CE   <= '1';
  SCLR <= '0', '1' after 100 ns;

  your_instance_name : c_counter_binary_0
  port map
  (
    CLK     => CLK,
    Q       => Q,
    THRESH0 => THRESH0
  );
end architecture;