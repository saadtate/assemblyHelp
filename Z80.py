# Get the path to the file from the user
file_path = input('Enter the path to the file containing the Z80 assembly code: ')

# Open the file for reading
with open(file_path, 'r') as f:
    # Read each line of the file
    for line in f:
        # Remove any leading or trailing white space from the line
        line = line.strip()

        # Split the line into individual words
        words = line.split()

        # If the line is empty or a comment, skip it
        if not line or line.startswith(';'):
            continue

        # Print the line of assembly code
        print(line)

        # Check the first word to determine the type of instruction
        if words[0] == 'LD':
            # LD instruction: load data into a register or memory location
            print('This instruction loads data into a register or memory location.')
        elif words[0] == 'ADD':
            # ADD instruction: add data to the accumulator
            print('This instruction adds data to the accumulator.')
        elif words[0] == 'SUB':
            # SUB instruction: subtract data from the accumulator
            print('This instruction subtracts data from the accumulator.')
        elif words[0] == 'AND':
            # AND instruction: perform a bitwise AND operation on the accumulator
            print('This instruction performs a bitwise AND operation on the accumulator.')
        elif words[0] == 'OR':
            # OR instruction: perform a bitwise OR operation on the accumulator
            print('This instruction performs a bitwise OR operation on the accumulator.')
        elif words[0] == 'XOR':
            # XOR instruction: perform a bitwise XOR operation on the accumulator
            print('This instruction performs a bitwise XOR operation on the accumulator.')
        elif words[0] == 'NOT':
            # NOT instruction: perform a bitwise NOT operation on the accumulator
            print('This instruction performs a bitwise NOT operation on the accumulator.')
        elif words[0] == 'INC':
            # INC instruction: increment a register or memory location
            print('This instruction increments a register or memory location.')
        elif words[0] == 'DEC':
            # DEC instruction: decrement a register or memory location
            print('This instruction decrements a register or memory location.')
        elif words[0] == 'ADDHL':
            # ADDHL instruction: add the value in HL to the accumulator
            print('This instruction adds the value in HL to the accumulator.')
        elif words[0] == 'ADCHL':
            # ADCHL instruction: add the value in HL and the carry flag to the accumulator
            print('This instruction adds the value in HL and the carry flag to the accumulator.')
        elif words[0] == 'SUBHL':
            # SUBHL instruction: subtract the value in HL from the accumulator
            print('This instruction subtracts the value in HL from the accumulator.')
        elif words[0] == 'SBCHL ':
            print('This instruction subtracts the value in HL and the carry flag from the accumulator.')

        elif words[0] == 'JP':
            # JP instruction: jump to a new location in the program
            print('This instruction jumps to a new location in the program.')
        elif words[0] == 'JR':
            # JR instruction: jump to a new location in the program, relative to the current location
            print('This instruction jumps to a new location in the program, relative to the current location.')
        elif words[0] == 'CALL':
            # CALL instruction: call a subroutine
            print('This instruction calls a subroutine.')
        elif words[0] == 'RET':
            # RET instruction: return from a subroutine
            print('This instruction returns from a subroutine.')
        elif words[0] == 'RST':
            # RST instruction: call a subroutine at a fixed address
            print('This instruction calls a subroutine at a fixed address.')
        elif words[0] == 'PUSH':
            # PUSH instruction: push a value onto the stack
            print('This instruction pushes a value onto the stack.')
        elif words[0] == 'POP':
            # POP instruction: pop a value off the stack
            print('This instruction pops a value off the stack.')
        elif words[0] == 'EX':
            # EX instruction: exchange the values of two registers or memory locations
            print('This instruction exchanges the values of two registers or memory locations.')
        elif words[0] == 'EXX':
            # EXX instruction: exchange the values of the BC, DE, and HL registers
            print('This instruction exchanges the values of the BC, DE, and HL registers.')
        elif words[0] == 'EXAF':
            # EXAF instruction: exchange the values of the AF and AF' registers
            print('This instruction exchanges the values of the AF and AF registers.')

        else :
            # Unrecognized instruction
            print('This is an unrecognized instruction.')

