`timescale 1ns/1ps

// 8-bit multi-function ALU for the coverage-guided testbench generation assignment.
//
// Operations:
//   4'h0: ADD  - y = a + b
//   4'h1: SUB  - y = a - b
//   4'h2: AND  - y = a & b
//   4'h3: OR   - y = a | b
//   4'h4: XOR  - y = a ^ b
//   4'h5: NOT  - y = ~a
//   4'h6: SLL  - y = a << b[2:0]
//   4'h7: SRL  - y = a >> b[2:0]
//   4'h8: SRA  - y = signed(a) >>> b[2:0]
//   4'h9: SLT  - signed comparison; y = 8'h01 when a < b, otherwise 8'h00
//   other: y = 8'h00
//
// Flags:
//   zero     = 1 when y == 0
//   negative = y[7]
//   carry    = carry-out for ADD; for SUB, 1 means no unsigned borrow
//   overflow = signed overflow for ADD/SUB; 0 for all other operations

module coverage_guided_alu (
    input  wire [7:0] a,
    input  wire [7:0] b,
    input  wire [3:0] op,
    output reg  [7:0] y,
    output reg        zero,
    output reg        negative,
    output reg        carry,
    output reg        overflow
);

    always @* begin
        // Safe defaults. These also define behavior for unsupported opcodes.
        y        = 8'h00;
        carry    = 1'b0;
        overflow = 1'b0;

        case (op)
            4'h0: begin // ADD
                {carry, y} = {1'b0, a} + {1'b0, b};
                overflow = (~(a[7] ^ b[7])) & (y[7] ^ a[7]);
            end

            4'h1: begin // SUB
                y = a - b;
                carry = (a >= b); // carry=1 means no unsigned borrow
                overflow = (a[7] ^ b[7]) & (y[7] ^ a[7]);
            end

            4'h2: begin // AND
                y = a & b;
            end

            4'h3: begin // OR
                y = a | b;
            end

            4'h4: begin // XOR
                y = a ^ b;
            end

            4'h5: begin // NOT
                y = ~a;
            end

            4'h6: begin // SLL
                y = a << b[2:0];
            end

            4'h7: begin // SRL
                y = a >> b[2:0];
            end

            4'h8: begin // SRA
                y = $signed(a) >>> b[2:0];
            end

            4'h9: begin // SLT (signed)
                y = ($signed(a) < $signed(b)) ? 8'h01 : 8'h00;
            end

            default: begin
                y = 8'h00;
            end
        endcase

        zero     = (y == 8'h00);
        negative = y[7];
    end

endmodule
