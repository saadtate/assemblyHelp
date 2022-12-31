opcodes = {
"ADD": "000000",
"ADDU": "000000",
"AND": "000000",
"BREAK": "000000",
"DIV": "000000",
"DIVU": "000000",
"J": "000010",
"JAL": "000011",
"JR": "000000",
"LB": "100000",
"LBU": "100100",
"LH": "100001",
"LHU": "100101",
"LUI": "001111",
"LW": "100011",
"LWL": "100010",
"LWR": "100110",
"MFHI": "000000",
"MFLO": "000000",
"MTHI": "000000",
"MTLO": "000000",
"MULT": "000000",
"MULTU": "000000",
"NOR": "000000",
"OR": "000000",
"SB": "101000",
"SH": "101001",
"SLL": "000000",
"SLT": "000000",
"SLTI": "001010",
"SLTIU": "001011",
"SLTU": "000000",
"SRA": "000000",
"SRL": "000000",
"SUB": "000000",
"SUBU": "000000",
"SW": "101011",
"SWL": "101010",
"SWR": "101110",
"XOR": "000000",
"ADDI": "001000",
"ADDIU": "001001",
"ANDI": "001100",
"BEQ": "000100",
"BGEZ": "000001",
"BGEZAL": "000001",
"BGTZ": "000111",
"BLEZ": "000110",
"BLTZ": "000001",
"BLTZAL": "000001",
"BNE": "000101",
"CACHE": "101111",
"CLO": "010010",
"CLZ": "010011",
"COP0": "010000",
"COP1": "010001",
"COP2": "010010",
"COP3": "010011",
"DADD": "000000",
"DADDU": "000000",
"DDIV": "000000",
"DDIVU": "000000",
"DIV": "000000",
"DIVU": "000000",
"DMULT": "000000",
"DMULTU": "000000",
"DSLL": "000000",
"DSLL32": "000000",
"DSRA": "000000",
"DSRA32": "000000",
"DSRL": "000000",
"DSRL32": "000000",
"DSUB": "000000",
"DSUBU": "000000",
"ERET": "010000",
"FLOOR.L.D": "010010",
"FLOOR.L.S": "010010",
"FLOOR.W.D": "010010",
"FLOOR.W.S": "010010",
"INS": "010011",
"JALR": "000000",
"JALR.HB": "000000",
"JR.HB": "000000",
"L.D": "110111",
"L.S": "110001",
"LA": "110111",
"LBU": "100100",
"LDC1": "110101",
"LDC2": "110010",
"LDC3": "110011",
"LDXC1": "110101",
"LHU": "100101",
"LL": "110000",
"LWL": "100010",
"LWR": "100110",
"LWU": "100111",
"MADD": "000000",
"MADDU": "000000",
"MFC0": "010000",
"MFC1": "010001",
"MFC2": "010010",
"MFC3": "010011",
"MFHC1": "010001",
"MFHC2": "010010",
"MFHC3": "010011",
"MFHI": "000000",
"MFLO": "000000",
"MOV.D": "010010",
"MOV.S": "010010",
"MOVF": "000000",
"MOVF.D": "010010",
"MOVF.S": "010010",
"MOVN": "000000",
"MOVN.D": "010010",
"MOVN.S": "010010",
"MOVT": "000000",
"MOVT.D": "010010",
"MOVT.S": "010010",
"MOVZ": "000000",
"MOVZ.D": "010010",
"MOVZ.S": "010010",
"MSUB": "000000",
"MSUBU": "000000",
"MTC0": "010000",
"MTC1": "010001",
"MTC2": "010010",
"MTC3": "010011",
"MTHC1": "010001",
"MTHC2": "010010",
"MTHC3": "010011",
"MTHI": "000000",
"MTLO": "000000",
"MUL": "000000",
"MULT": "000000",
"MULTU": "000000",
"NOP": "000000",
"NOR": "000000",
"OR": "000000",
"ORI": "001101",
"PREF": "110011",
}
# Define a dictionary of instructions and their corresponding descriptions
descriptions = {
    "ADD": "Add two registers and store the result in a third register.",
    "ADDU": "Add two registers and store the result in a third register (unsigned).",
    "AND": "Bitwise AND two registers and store the result in a third register.",
    "BREAK": "Cause an exception to occur, usually to halt program execution.",
    "DIV": "Divide one register by another (signed) and store the quotient in the LO register and the remainder in the HI register.",
    "DIVU": "Divide one register by another (unsigned) and store the quotient in the LO register and the remainder in the HI register.",
    "J": "Jump to a specific address.",
    "JAL": "Jump to a specific address and save the return address in a register.",
    "JR": "Jump to the address stored in a register.",
    "LB": "Load a byte from memory into a register (signed).",
    "LBU": "Load a byte from memory into a register (unsigned).",
    "LH": "Load a halfword from memory into a register (signed).",
    "LHU": "Load a halfword from memory into a register (unsigned).",
    "LUI": "Load an immediate value into a register and shift it left by 16 bits.",
    "LW": "Load a word from memory into a register.",
    "LWL": "Load a word from memory into a register, with the least significant byte being stored in the register first.",
    "LWR": "Load a word from memory into a register, with the most significant byte being stored in the register first.",
    "MFHI": "Move the value in the HI register to a general-purpose register.",
    "MFLO": "Move the value in the LO register to a general-purpose register.",
    "MTHI": "Move the value in a general-purpose register to the HI register.",
    "MTLO": "Move the value in a general-purpose register to the LO register.",
    "MULT": "Multiply two registers (signed) and store the result in the LO and HI registers.",
    "MULTU": "Multiply two registers (unsigned) and store the result in the LO and HI registers.",
    "NOR": "Bitwise NOR two registers and store the result in a third register.",
    "OR": "Bitwise OR two registers and store the result in a third register.",
    "ORI": "Bitwise OR an immediate value with a register and store the result in a third register.",
    "SB": "Store a byte in memory from a register.",
"SH": "Store a halfword in memory from a register.",
"SLL": "Shift the value in a register left by a specified number of bits.",
"SLT": "Set a register to 1 if the value in another register is less than that in a third register, or 0 if it is not (signed).",
"SLTI": "Set a register to 1 if the value in another register is less than an immediate value, or 0 if it is not (signed).",
"SLTIU": "Set a register to 1 if the value in another register is less than an immediate value, or 0 if it is not (unsigned).",
"SLTU": "Set a register to 1 if the value in another register is less than that in a third register, or 0 if it is not (unsigned).",
"SRA": "Shift the value in a register right by a specified number of bits, preserving the sign bit.",
"SRL": "Shift the value in a register right by a specified number of bits, filling the leftmost bits with 0.",
"SUB": "Subtract one register from another and store the result in a third register (signed).",
"SUBU": "Subtract one register from another and store the result in a third register (unsigned).",
"SW": "Store a word in memory from a register.",
"SWL": "Store a word in memory from a register, with the least significant byte being stored first.",
"SWR": "Store a word in memory from a register, with the most significant byte being stored first.",
"XOR": "Bitwise XOR two registers and store the result in a third register.",
"ADDI": "Add an immediate value to a register and store the result in a.",
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




