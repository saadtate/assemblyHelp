# Define a dictionary of opcodes and their corresponding instructions
opcodes = {
    "0000": "ORI to CCR",
    "0001": "ORI",
    "0010": "ANDI to CCR",
    "0011": "ANDI",
    "0100": "SUBI",
    "0101": "ADDI",
    "0110": "BTST",
    "0111": "BCHG",
    "1000": "BCLR",
    "1001": "BSET",
    "1010": "MOVEP",
    "1011": "MOVEA",
    "1100": "MOVE",
    "1101": "LEA",
    "1110": "CMP",
    "1111": "JSR"
}

# Define a dictionary of instructions and their corresponding descriptions
descriptions = {
    "ORI to CCR": "Logically OR an immediate value with the condition code register (CCR).",
    "ORI": "Logically OR an immediate value with a destination operand.",
    "ANDI to CCR": "Logically AND an immediate value with the condition code register (CCR).",
    "ANDI": "Logically AND an immediate value with a destination operand.",
    "SUBI": "Subtract an immediate value from a destination operand.",
    "ADDI": "Add an immediate value to a destination operand.",
    "BTST": "Test a bit in a destination operand.",
    "BCHG": "Toggle a bit in a destination operand.",
    "BCLR": "Clear a bit in a destination operand.",
    "BSET": "Set a bit in a destination operand.",
    "MOVEP": "Move data between memory and register pairs.",
    "MOVEA": "Move address from source to destination.",
    "MOVE": "Move data from source to destination.",
    "LEA": "Load effective address into destination operand.",
    "CMP": "Compare destination and source operands.",
    "JSR": "Jump to subroutine.",
    "Unknown": "An unknown or invalid instruction."
}

# Prompt the user for the name of the assembly text file
filename = input("Enter the name of the assembly text file: ")

# Open the file and read each line
with open(filename, "r") as f:
    for line in f:
        # Split the line into opcode and operand (if any)
        parts = line.strip().split(" ")
        opcode = parts[0]
        operand = "" if len(parts) < 2 else parts[1]

        # Look up the instruction based on the opcode
        instruction = opcodes.get(opcode, "Unknown")

        # Look up the description of the instruction
        description = descriptions[instruction]

        # Print the instruction, operand (if any), and description
        print(f"{instruction}: {operand}\n{description}\n")
