`timescale 1ns/1ps

module simple_alu_tb;
    reg  [3:0] a;
    reg  [3:0] b;
    reg  [1:0] op;
    wire [3:0] result;

    integer failures;

    simple_alu dut (
        .a(a),
        .b(b),
        .op(op),
        .result(result)
    );

    initial begin
        $dumpfile("build/simple_alu_raw.vcd");
        $dumpvars(0, simple_alu_tb);

        failures = 0;
        a = 4'h0;
        b = 4'h0;
        op = 2'b00;

        // Test 1: ADD.  3 + 2 should be 5.
        #1;
        a = 4'h3;
        b = 4'h2;
        op = 2'b00;
        #1;
        if (result !== 4'h5) begin
            $display("ERROR: ADD result=%h expected=5", result);
            failures = failures + 1;
        end

        // Test 2: AND.  6 & 3 should be 2.
        #1;
        a = 4'h6;
        b = 4'h3;
        op = 2'b01;
        #1;
        if (result !== 4'h2) begin
            $display("ERROR: AND result=%h expected=2", result);
            failures = failures + 1;
        end

        // OR (op=10) and XOR (op=11) are intentionally not tested.
        if (failures == 0)
            $display("PASS: ADD and AND tests passed");
        else
            $display("FAIL: %0d self-check(s) failed", failures);

        #1;
        $finish;
    end

endmodule
