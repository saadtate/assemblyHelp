# Define a dictionary of instructions and their corresponding opcodes
opcodes = {
    "ADD": "000000",
    "ADDU": "000001",
    "AND": "000010",
    "BEQ": "000011",
    "BNE": "000100",
    "J": "000101",
    "JAL": "000110",
    "JR": "000111",
    "LBU": "001000",
    "LHU": "001001",
    "LUI": "001010",
    "LW": "001011",
    "NOR": "001100",
    "OR": "001101",
    "SLT": "001110",
    "SLTU": "001111",
    "SLL": "010000",
    "SRL": "010001",
    "SUB": "010010",
    "SUBU": "010011",
    "SW": "010100",
    "XOR": "010101",
    "MFHI": "010110",
    "MFLO": "010111",
    "MTHI": "011000",
    "MTLO": "011001",
    "MULT": "011010",
    "MULTU": "011011",
    "DIV": "011100",
    "DIVU": "011101",
    "BLTZ": "011110",
    "BGEZ": "011111",
    "BLTZAL": "100000",
    "BGEZAL": "100001"
}

# Define a dictionary of instructions and their corresponding descriptions
descriptions = {
    "ADD": "Add two registers and store the result in a third register.",
    "ADDU": "Add two registers and store the result in a third register (unsigned).",

    "AND": "Bitwise AND two registers and store the result in a third register.",
    "BEQ": "Branch if two registers are equal.",
    "BNE": "Branch if two registers are not equal.",
    "J": "Jump to a specific address.",
    "JAL": "Jump to a specific address and save the return address in a register.",
    "JR": "Jump to the address stored in a register.",
    "LBU": "Load a byte from memory into a register (unsigned).",
    "LHU": "Load a halfword from memory into a register (unsigned).",
    "LUI": "Load an immediate value into a register and shift it left by 16 bits.",
    "LW": "Load a word from memory into a register.",
    "NOR": "Bitwise NOR two registers and store the result in a third register.",
    "OR": "Bitwise OR two registers and store the result in a third register.",
    "SLT": "Set a register to 1 if the value in another register is less than that in a third register, or 0 if it is not (signed).",
    "SLTU": "Set a register to 1 if the value in another register is less than that in a third register, or 0 if it is not (unsigned).",
    "SLL": "Shift the value in a register left by a specified number of bits.",
    "SRL": "Shift the value in a register right by a specified number of bits.",
    "SUB": "Subtract one register from another and store the result in a third register (signed).",
    "SUBU": "Subtract one register from another and store the result in a third register (unsigned).",
    "SW": "Store a word in memory from a register.",
    "XOR": "Bitwise XOR two registers and store the result in a third register.",
    "MFHI": "Move the value in the HI register to a general-purpose register.",
    "MFLO": "Move the value in the LO register to a general-purpose register.",
    "MTHI": "Move the value in a general-purpose register to the HI register.",
    "MTLO": "Move the value in a general-purpose register to the LO register.",
    "MULT": "Multiply two registers (signed) and store the result in the LO and HI registers.",
    "MULTU": "Multiply two registers (unsigned) and store the result in the LO and HI registers.",
     "DIV": "Divide one register by another (signed) and store the quotient in the LO register and the remainder in the HI register.",
    "DIVU": "Divide one register by another (unsigned) and store the quotient in the LO register and the remainder in the HI register.",
    "BLTZ": "Branch if the value in a register is less than zero (signed).",
    "BGEZ": "Branch if the value in a register is greater than or equal to zero (signed).",
    "BLTZAL": "Branch if the value in a register is less than zero (signed) and save the return address in the link register.",
    "BGEZAL": "Branch if the value in a register is greater than or equal to zero (signed) and save the return address in the link register."
}

# Define a function to print the description of an instruction
def print_description(opcode):
  if opcode in descriptions:
    print(descriptions[opcode])
  else:
    print("An unknown or invalid instruction.")

# Read in the file name
filename = input("Enter the name of the assembly file: ")

# Open the file and read in each line
with open(filename, "r") as file:
  for line in file:
    # Split the line into the opcode and operand
    parts = line.split(" ")
    opcode = parts[0]
    # Print the description of the instruction
    print_description(opcode)

