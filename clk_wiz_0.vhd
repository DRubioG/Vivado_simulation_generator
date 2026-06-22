
library ieee;         
use ieee.std_logic_1164.all;


entity clk_wiz_0 is
	port (
		clk_in1 : in std_logic;
		clk_in2 : in std_logic;
		clk_out1 : out std_logic;
		clk_out2 : out std_logic;
		clk_out3 : out std_logic;

		reset : out std_logic;
		locked : out std_logic
	);
end entity;


architecture arch_clk_wiz_0 of clk_wiz_0 is


	constant C_PERIOD_CLK_OUT1 : time := 5.0 ns;
	constant C_PERIOD_CLK_OUT2 : time := 2.0 ns;
	constant C_PERIOD_CLK_OUT3 : time := 4.0 ns;

begin



    
----------------------------------------------------------------
-- clk_out1
---------------------------------------------------------------- 
	process begin
		clk_out1 <= '1';
		wait for C_PERIOD_CLK_OUT1;

		clk_out1 <= '1';
		wait for C_PERIOD_CLK_OUT1;
	end process;



    
----------------------------------------------------------------
-- clk_out2
---------------------------------------------------------------- 
	process begin
		clk_out2 <= '1';
		wait for C_PERIOD_CLK_OUT2;

		clk_out2 <= '1';
		wait for C_PERIOD_CLK_OUT2;
	end process;



    
----------------------------------------------------------------
-- clk_out3
---------------------------------------------------------------- 
	process begin
		clk_out3 <= '1';
		wait for C_PERIOD_CLK_OUT3;

		clk_out3 <= '1';
		wait for C_PERIOD_CLK_OUT3;
	end process;



    
----------------------------------------------------------------
-- RESET
---------------------------------------------------------------- 
	process begin
		reset <= '0';
		wait for 50 ns;
		reset <= '1';
		wait;
	end process;



    
----------------------------------------------------------------
-- LOCKED
---------------------------------------------------------------- 
	process begin
		locked <= '0';
		wait for 120 ns;
		locked <= '1';
		wait;
	end process;


end architecture;