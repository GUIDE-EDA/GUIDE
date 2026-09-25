`timescale 1ns/1ps

module tb_shift_register();
    reg clk;
    reg reset_n;
    reg data_in;
    reg shift_enable;
    wire [7:0] data_out;

    // Instantiate the shift_register
    shift_register dut (
        .clk(clk),
        .reset_n(reset_n),
        .data_in(data_in),
        .shift_enable(shift_enable),
        .data_out(data_out)
    );

    // Clock generation
    always begin
        #5 clk = ~clk;
    end

    // Test case data
    reg [7:0] test_case_reset_n = 8'b10111111;
    reg [7:0] test_case_data_in = 8'b11001011;
    reg [7:0] test_case_shift_enable = 8'b10111110;
    reg [63:0] test_case_data_out = 64'h80002850a0408000;

    integer i = 0;

    // Test runner
    initial begin
        clk = 0;
		reset_n = 0;
        data_in = 0;
        shift_enable = 0;

		@(posedge clk) // Wait for one clock cycle for synchronous reset
		@(negedge clk) // Starts inputs changing on negedge

        for (i = 0; i < 8; i = i + 1) begin
            reset_n <= test_case_reset_n[i];
            data_in <= test_case_data_in[i];
            shift_enable <= test_case_shift_enable[i];
			@(negedge clk)
			
            if (data_out !== test_case_data_out[8*i+:8]) begin
                $display("Error: Test case %0d failed. Expected: %b, Got: %b", i, test_case_data_out[8*i+:8], data_out);
                $finish;
            end
        end

        $display("All test cases passed!");
        $finish;
    end
endmodule

