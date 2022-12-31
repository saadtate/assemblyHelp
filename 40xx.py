# Open the file for reading
with open('40xxl', 'r') as f:
  # Read the contents of the file
  text = f.read()


# Define a dictionary of opcodes and their corresponding instructions
opcodes = {
    "0000": "Halt",
    "0001": "Load A",
    "0010": "Load B",
    "0011": "Load C",
    "0100": "Load D",
    "0101": "Store A",
    "0110": "Store B",
    "0111": "Store C",
    "1000": "Store D",
    "1001": "Add",
    "1010": "Subtract",
    "1011": "Shift right",
    "1100": "Shift left",
    "1101": "And",
    "1110": "Or",
    "1111": "Exclusive or",
    "11100": "Branch if A = 0",
    "11101": "Branch if A ≠ 0",
    "11110": "Branch if C = 0",
    "11111": "Branch if C ≠ 0"
}

# Define a dictionary of instructions and their corresponding descriptions
descriptions = {
    "Halt": "Stop execution of the program.",
    "Load A": "Load the value at the memory address specified in the next 12 bits into register A.",
    "Load B": "Load the value at the memory address specified in the next 12 bits into register B.",
    "Load C": "Load the value at the memory address specified in the next 12 bits into register C.",
    "Load D": "Load the value at the memory address specified in the next 12 bits into register D.",
    "Store A": "Store the value in register A at the memory address specified in the next 12 bits.",
    "Store B": "Store the value in register B at the memory address specified in the next 12 bits.",
    "Store C": "Store the value in register C at the memory address specified in the next 12 bits.",
    "Store D": "Store the value in register D at the memory address specified in the next 12 bits.",
    "Add": "Add the values in registers A and B and store the result in register A.",
    "Subtract": "Subtract the value in register B from the value in register A and store the result in register A.",
    "Shift right": "Shift the value in register A right by one bit.",
    "Shift left": "Shift the value in register A left by one bit.",
    "And": "Perform a bitwise AND operation on the values in registers A and B and store the result in register A.",
    "Or": "Perform a bitwise OR operation on the values in registers A and B and store the result in register A.",
    "Exclusive or": "Perform a bitwise XOR operation on the values in registers A and B and store the result in register A.",
    "Branch if A = 0": "If the value in register A is 0, jump to the memory address specified in the next 12 bits.",
    "Branch if A ≠ 0": "If the value in register A is not 0, jump to the memory address specified in the next 12 bits.",
    "Branch if C = 0": "If the value in register C is 0, jump to the memory address specified in the next 12 bits.",
    "Branch if C ≠ 0": "If the value in register C is not 0, jump to the memory address specified in the next 12 bits.",
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

