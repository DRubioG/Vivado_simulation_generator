library ieee;
use ieee.std_logic_1164.all;

library std;
use std.textio.all;

entity clk_wiz_0 is
    port (
        clk_out1 : out std_logic;
        clk_out2 : out std_logic;
        reset    : in  std_logic;
        locked   : out std_logic;
        clk_in1  : in  std_logic
    );
end entity;

architecture sim of clk_wiz_0 is

    shared variable clk1_period : time := 10 ns;
    shared variable clk2_period : time := 20 ns;
    shared variable lock_delay  : time := 100 ns;

begin

    ----------------------------------------------------------------
    -- CONFIG LOADER
    ----------------------------------------------------------------

    process

        file cfg_file : text open read_mode is "clk_wiz_0.cfg";

        variable line_buf : line;

    begin

        readline(cfg_file, line_buf);
        read(line_buf, clk1_period);

        readline(cfg_file, line_buf);
        read(line_buf, clk2_period);

        readline(cfg_file, line_buf);
        read(line_buf, lock_delay);

        report "CLK1 period = " & time'image(clk1_period);
        report "CLK2 period = " & time'image(clk2_period);
        report "LOCK delay  = " & time'image(lock_delay);

        wait;

    end process;

    ----------------------------------------------------------------
    -- CLOCK 1
    ----------------------------------------------------------------

    process
    begin

        wait for 1 ns;

        while true loop

            clk_out1 <= '1';
            wait for clk1_period/2;

            clk_out1 <= '0';
            wait for clk1_period/2;

        end loop;

    end process;

    ----------------------------------------------------------------
    -- CLOCK 2
    ----------------------------------------------------------------

    process
    begin

        wait for 1 ns;

        while true loop

            clk_out2 <= '1';
            wait for clk2_period/2;

            clk_out2 <= '0';
            wait for clk2_period/2;

        end loop;

    end process;

    ----------------------------------------------------------------
    -- LOCKED
    ----------------------------------------------------------------

    process
    begin

        locked <= '0';

        wait for lock_delay;

        locked <= '1';

        wait;

    end process;

end architecture;