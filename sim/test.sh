nvc -a mult_gen_0.vhd

nvc -a test_mul.vhd

nvc -e mult_gen_0_tb

nvc -r mult_gen_0_tb --stop-time=1us --wave=mult_gen_0_tb.vcd