# Simple Icarus Verilog + Covered Example

This example uses a very small 4-bit calculator. There is no clock, reset,
state machine, or memory. The goal is to make the simulation and coverage flow
easy to understand.

## The RTL

The RTL is in `src/simple_alu.v` and has only four signals:

| Signal | Direction | Meaning |
|---|---|---|
| `a` | input | first 4-bit number |
| `b` | input | second 4-bit number |
| `op` | input | chooses the operation |
| `result` | output | 4-bit answer |

`op` is a 2-bit value:

| `op` | Operation |
|---|---|
| `00` | `a + b` (ADD) |
| `01` | `a & b` (AND) |
| `10` | `a | b` (OR) |
| `11` | `a ^ b` (XOR) |

For example, when `a=3`, `b=2`, and `op=00`, the result is 5.

## The testbench

The testbench is in `tb/simple_alu_tb.v`. It performs two tests:

1. ADD: `3 + 2 = 5`
2. AND: `6 & 3 = 2`

OR and XOR are deliberately not tested. This gives the coverage report two
clear missing RTL lines to show.

## Run it

Install `iverilog`, `vvp`, and `covered`, then run:

```sh
cd coverage_exp
make report
```

If Covered is not in `PATH`:

```sh
make report COVERED=/path/to/covered
```

Generated files:

```text
build/simple_alu.vvp         compiled simulation
build/simple_alu_raw.vcd     original simulation waveform
build/simple_alu.vcd         waveform read by Covered
build/simple_alu.cdd         coverage data
build/coverage_summary.rpt   short coverage report
build/coverage_detail.rpt    missed lines and signal details
```

To run only the simulation:

```sh
make sim
```

The ready-to-present English slides are included here:

```text
slides/coverage_flow_slides.pdf
```

The classroom ZIP intentionally omits the LaTeX source and temporary files.

The complete Covered user manual is also included as a PDF:

```text
covered/doc/covered_user_guide.pdf
```

To present the slides together with a live, executable demonstration:

```sh
jupyter lab student_coverage_demo.ipynb
```

The notebook sections are labeled with the matching slide numbers. Run its
cells from top to bottom. The first code cell installs the command-line tools
before the lesson starts:

- Google Colab and Debian/Ubuntu install Icarus Verilog and Covered with
  `apt-get`.
- macOS installs Icarus Verilog and the build tools with Homebrew, then builds
  a private Covered 0.7.10 in a per-user directory under `/tmp`. This avoids a
  limitation in Covered's old build scripts when the course folder name has
  spaces. Homebrew itself must already be present because its installer may
  request an administrator password.
- On Windows, use Google Colab or WSL/Ubuntu; native Windows is not supported.

Distribute the complete `coverage_exp` folder so the notebook can read the RTL
and testbench files beside it.

An instructor with Covered installed in a non-standard location can start
Jupyter with:

```sh
COVERED=/path/to/covered jupyter lab student_coverage_demo.ipynb
```

The notebook checks the `COVERED` environment variable, `PATH`, and its private
Covered copy. On macOS, rerunning the install cell rebuilds the copy if `/tmp`
has been cleaned.

## Three coverage types used here

### Line coverage

Question: did the test run each RTL line?

The ADD and AND lines run. The OR and XOR lines do not. The measured result is
3 of 5 lines, or 60%.

### Toggle coverage

Question: did every bit change from 0 to 1 and from 1 to 0?

The test uses only a few values, so many bits do not change both ways. Covered
reports 64% for 0-to-1 changes and 21% for 1-to-0 changes.

### Logic coverage

Question: did the test try different input combinations for each expression?

For example, `a & b` can see zeros and ones in different positions. One AND
test cannot try every combination. The measured result is 6 of 17, or 35%.

Covered can also measure state-machine, memory, and OVL assertion coverage, but
this beginner example does not contain those structures.

## Flow

```text
simple_alu.v + simple_alu_tb.v
              |
              | Icarus Verilog: compile and simulate
              v
       simple_alu.vcd
              |
              | Covered: read RTL and waveform
              v
       coverage reports
```

The Makefile removes one VCD comment produced by Icarus Verilog 13 because the
older Covered 0.7.10 VCD reader cannot parse that comment.
