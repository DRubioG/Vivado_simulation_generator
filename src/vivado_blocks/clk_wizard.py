



code = " \
library ieee; \
use ieee.std_logic_1164.all; \
\
library std; \
use std.textio.all; \
\
entity clk_wiz_0 is \
    port (\
        clk_out1 : out std_logic; \
        clk_out2 : out std_logic; \
        reset    : in  std_logic; \
        locked   : out std_logic; \
        clk_in1  : in  std_logic \
    ); \
end entity; \
 \
architecture sim of clk_wiz_0 is \
 \
    constant clk1_period : time := 10 ns; \
    constant clk2_period : time := 20 ns; \
    constant lock_delay  : time := 100 ns; \
 \
begin \
 \
    ---------------------------------------------------------------- \
    -- CONFIG LOADER \
    ---------------------------------------------------------------- \
 \
    ---------------------------------------------------------------- \
    -- CLOCK 1 \
    ---------------------------------------------------------------- \
 \
    process \
    begin \
 \
        wait for 1 ns; \
 \
        while true loop \
 \
            clk_out1 <= '1'; \
            wait for clk1_period/2; \
 \
            clk_out1 <= '0'; \
            wait for clk1_period/2; \
 \
        end loop; \
 \
    end process; \
 \
    ---------------------------------------------------------------- \
    -- CLOCK 2 \
    ---------------------------------------------------------------- \
 \
    process \
    begin \
 \
        wait for 1 ns; \
 \
        while true loop \
 \
            clk_out2 <= '1'; \
            wait for clk2_period/2; \
 \
            clk_out2 <= '0'; \
            wait for clk2_period/2; \
 \
        end loop; \
 \
    end process; \
 \
    ---------------------------------------------------------------- \
    -- LOCKED \
    ---------------------------------------------------------------- \
 \
    process \
    begin \
 \
        locked <= '0'; \
 \
        wait for lock_delay; \
 \
        locked <= '1'; \
 \
        wait; \
 \
    end process; \
 \
end architecture;"

locked = "process \
    begin \
        locked <= '0'; \
        wait for lock_delay; \
        locked <= '1'; \
        wait; \
    end process; \
end architecture;"
