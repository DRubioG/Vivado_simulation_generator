
library ieee;         
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity blk_mem_gen_0 is
	port (
		douta : out std_logic_vector(31 downto 0);
		clka : in std_logic;
		rsta : in std_logic;
		regcea : in std_logic;
		wea : in std_logic_vector(3 downto 0);
		addra : in std_logic_vector(31 downto 0);
		dina : in std_logic_vector(31 downto 0)
	);
end entity;


architecture arch_blk_mem_gen_0 of blk_mem_gen_0 is


	type ram_type is array (0 to 32-1)
		of std_logic_vector(31 downto 0);
	signal RAM : ram_type := (others => (others => '0'));
	signal ram_d : std_logic_vector(31 downto 0);

begin


assert false
report "Don't use this file in synthesis"
severity error;


	process begin
		rsta_busy <= '0';
		wait until rising_edge(clka);
		rsta_busy <= '1';
		wait for 40 ns;
		for i in 0 to 2 loop
		wait until rising_edge(clka);
		end loop;
		rsta_busy <= '0';
		wait;
	end process;


	process (clka)
		variable addr : integer;
	begin
		if rising_edge(clka) then
			if rsta = '1' then
				addr := 0;
			else
				addr := to_integer(unsigned(addra));
					if wea /= "0000" then
						RAM(addr) <= dina;
						ram_d <= dina;
					else
						ram_d <= RAM(addr);
					end if;
			end if;
		end if;
	end process;


	process (clka)
	begin
		if rising_edge(clka) then
			douta <= ram_d;
		end if;
	end process;
end architecture;