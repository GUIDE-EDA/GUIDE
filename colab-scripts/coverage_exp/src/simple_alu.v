`timescale 1ps/1ps

// A small 4-bit calculator used to demonstrate basic code coverage.
module simple_alu (
    input  wire [3:0] a,
    input  wire [3:0] b,
    input  wire [1:0] op,
    output reg  [3:0] result
);

    // op selects one of four simple operations.
    always @* begin
        case (op)
            2'b00: result = a + b;  // ADD
            2'b01: result = a & b;  // AND
            2'b10: result = a | b;  // OR
            2'b11: result = a ^ b;  // XOR
        endcase
    end

endmodule
