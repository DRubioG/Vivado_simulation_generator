nvc -a c_counter_binary_0.vhd

nvc -a test_binary_counter.vhd

nvc -e test_binary_counter

nvc -r test_binary_counter --stop-time=1us --wave=test_binary_counter.vcd