# Open the file for reading
with open('6502l', 'r') as f:
  # Read the contents of the file
  text = f.read()
opcode_dict = {
    # ADC - Add with carry
    'ADC': {'mode': 'Immediate', 'operation': 'Add with carry', 'bytes': 2, 'cycles': 2},
    'ADC': {'mode': 'Zero Page', 'operation': 'Add with carry', 'bytes': 2, 'cycles': 3},
    'ADC': {'mode': 'Zero Page,X', 'operation': 'Add with carry', 'bytes': 2, 'cycles': 4},
    'ADC': {'mode': 'Absolute', 'operation': 'Add with carry', 'bytes': 3, 'cycles': 4},
    'ADC': {'mode': 'Absolute,X', 'operation': 'Add with carry', 'bytes': 3, 'cycles': 4},
    'ADC': {'mode': 'Absolute,Y', 'operation': 'Add with carry', 'bytes': 3, 'cycles': 4},
    'ADC': {'mode': 'Indirect,X', 'operation': 'Add with carry', 'bytes': 2, 'cycles': 6},
    'ADC': {'mode': 'Indirect,Y', 'operation': 'Add with carry', 'bytes': 2, 'cycles': 5},

    # AND - Bitwise AND
    'AND': {'mode': 'Immediate', 'operation': 'Bitwise AND', 'bytes': 2, 'cycles': 2},
    'AND': {'mode': 'Zero Page', 'operation': 'Bitwise AND', 'bytes': 2, 'cycles': 3},
    'AND': {'mode': 'Zero Page,X', 'operation': 'Bitwise AND', 'bytes': 2, 'cycles': 4},
    'AND': {'mode': 'Absolute', 'operation': 'Bitwise AND', 'bytes': 3, 'cycles': 4},
    'AND': {'mode': 'Absolute,X', 'operation': 'Bitwise AND', 'bytes': 3, 'cycles': 4},
    'AND': {'mode': 'Absolute,Y', 'operation': 'Bitwise AND', 'bytes': 3, 'cycles': 4},
    'AND': {'mode': 'Indirect,X', 'operation': 'Bitwise AND', 'bytes': 2, 'cycles': 6},
    'AND': {'mode': 'Indirect,Y', 'operation': 'Bitwise AND', 'bytes': 2, 'cycles': 5},

    # ASL - Arithmetic shift left
    'ASL': {'mode': 'Accumulator', 'operation': 'Arithmetic shift left', 'bytes': 1, 'cycles': 2},
    'ASL': {'mode': 'Zero Page', 'operation': 'Arithmetic shift left', 'bytes': 2, 'cycles': 5},
    'ASL': {'mode': 'Zero Page,X', 'operation': 'Arithmetic shift left', 'bytes': 2, 'cycles': 6},
    'ASL': {'mode': 'Absolute', 'operation': 'Arithmetic shift left', 'bytes': 3, 'cycles': 6},
    'ASL': {'mode': 'Absolute,X', 'operation': 'Arithmetic shift left', 'bytes': 3, 'cycles': 7},

    # BCS - Branch on carry set
    'BCS': {'mode': 'Relative', 'operation': 'Branch on carry set', 'bytes': 2, 'cycles': 2},

    # BEQ - Branch on equal
    'BEQ': {'mode': 'Relative', 'operation': 'Branch on equal', 'bytes': 2, 'cycles': 2},

    # BIT - Bit test
    'BIT': {'mode': 'Zero Page', 'operation': 'Bit test', 'bytes': 2, 'cycles': 3},
    'BIT': {'mode': 'Absolute', 'operation': 'Bit test', 'bytes': 3, 'cycles': 4},

    # BMI - Branch on minus
    'BMI': {'mode': 'Relative', 'operation': 'Branch on minus', 'bytes': 2, 'cycles': 2},

    # BNE - Branch on not equal
    'BNE': {'mode': 'Relative', 'operation': 'Branch on not equal', 'bytes': 2, 'cycles': 2},

    # BPL - Branch on plus
    'BPL': {'mode': 'Relative', 'operation': 'Branch on plus', 'bytes': 2, 'cycles': 2},

    # BRK - Force interrupt
    'BRK': {'mode': 'Implied', 'operation': 'Force interrupt', 'bytes': 1, 'cycles': 7},

    # BVC - Branch on overflow clear
    'BVC': {'mode': 'Relative', 'operation': 'Branch on overflow clear', 'bytes': 2, 'cycles': 2},

    # BVS - Branch on overflow set
    'BVS': {'mode': 'Relative', 'operation': 'Branch on overflow set', 'bytes': 2, 'cycles': 2},

    # CLC - Clear carry flag
    'CLC': {'mode': 'Implied', 'operation': 'Clear carry flag', 'bytes': 1, 'cycles': 2},

    # CLD - Clear decimal mode
    'CLD': {'mode': 'Implied', 'operation': 'Clear decimal mode', 'bytes': 1, 'cycles': 2},

    # CLI - Clear interrupt disable
    'CLI': {'mode': 'Implied', 'operation': 'Clear interrupt disable', 'bytes': 1, 'cycles': 2},

    # CLV - Clear overflow flag
    'CLV': {'mode': 'Implied', 'operation': 'Clear overflow flag', 'bytes': 1, 'cycles': 2},

    # CPX - Compare X register
    'CPX': {'mode': 'Immediate', 'operation': 'Compare X register', 'bytes': 2, 'cycles': 2},
    'CPX': {'mode': 'Zero Page', 'operation': 'Compare X register', 'bytes': 2, 'cycles': 3},
    'CPX': {'mode': 'Absolute', 'operation': 'Compare X register', 'bytes': 3, 'cycles': 4},

    # CPY - Compare Y register
    'CPY': {'mode': 'Immediate', 'operation': 'Compare Y register', 'bytes': 2, 'cycles': 2},
    'CPY': {'mode': 'Zero Page', 'operation': 'Compare Y register', 'bytes': 2, 'cycles': 3},
    'CPY': {'mode': 'Absolute', 'operation': 'Compare Y register', 'bytes': 3, 'cycles': 4},

    # DEC - Decrement memory
    'DEC': {'mode': 'Zero Page', 'operation': 'Decrement memory', 'bytes': 2, 'cycles': 5},
    'DEC': {'mode': 'Zero Page,X', 'operation': 'Decrement memory', 'bytes': 2, 'cycles': 6},
    'DEC': {'mode': 'Absolute', 'operation': 'Decrement memory', 'bytes': 3, 'cycles': 6},
    'DEC': {'mode': 'Absolute,X', 'operation': 'Decrement memory', 'bytes': 3, 'cycles': 7},

    # DEX - Decrement X register
    'DEX': {'mode': 'Implied', 'operation': 'Decrement X register', 'bytes': 1, 'cycles': 2},

    # DEY - Decrement Y register
    'DEY': {'mode': 'Implied', 'operation': 'Decrement Y register', 'bytes': 1, 'cycles': 2},

    # EOR - Exclusive OR
    'EOR': {'mode': 'Immediate', 'operation': 'Exclusive OR', 'bytes': 2, 'cycles': 2},
    'EOR': {'mode': 'Zero Page', 'operation': 'Exclusive OR', 'bytes': 2, 'cycles': 3},
    'EOR': {'mode': 'Zero Page,X', 'operation': 'Exclusive OR', 'bytes': 2, 'cycles': 4},
    'EOR': {'mode': 'Absolute', 'operation': 'Exclusive OR', 'bytes': 3, 'cycles': 4},
    'EOR': {'mode': 'Absolute,X', 'operation': 'Exclusive OR', 'bytes': 3, 'cycles': 4},
    'EOR': {'mode': 'Absolute,Y', 'operation': 'Exclusive OR', 'bytes': 3, 'cycles': 4},
    'EOR': {'mode': 'Indirect,X', 'operation': 'Exclusive OR', 'bytes': 2, 'cycles': 6},
    'EOR': {'mode': 'Indirect,Y', 'operation': 'Exclusive OR', 'bytes': 2, 'cycles': 5},

    # INX - Increment X register
    'INX': {'mode': 'Implied', 'operation': 'Increment X register', 'bytes': 1, 'cycles': 2},

    # INY - Increment Y register
    'INY': {'mode': 'Implied', 'operation': 'Increment Y register', 'bytes': 1, 'cycles': 2},

    # JMP - Jump
    'JMP': {'mode': 'Absolute', 'operation': 'Jump', 'bytes': 3, 'cycles': 3},
    'JMP': {'mode': 'Indirect', 'operation': 'Jump', 'bytes': 3, 'cycles': 5},

    # JSR - Jump to subroutine
    'JSR': {'mode': 'Absolute', 'operation': 'Jump to subroutine', 'bytes': 3, 'cycles': 6},

    # LDA - Load accumulator
    'LDA': {'mode': 'Immediate', 'operation': 'Load accumulator', 'bytes': 2, 'cycles': 2},
    'LDA': {'mode': 'Zero Page', 'operation': 'Load accumulator', 'bytes': 2, 'cycles': 3},
    'LDA': {'mode': 'Zero Page,X', 'operation': 'Load accumulator', 'bytes': 2, 'cycles': 4},

    # LDX - Load X register
    'LDX': {'mode': 'Immediate', 'operation': 'Load X register', 'bytes': 2, 'cycles': 2},
    'LDX': {'mode': 'Zero Page', 'operation': 'Load X register', 'bytes': 2, 'cycles': 3},
    'LDX': {'mode': 'Zero Page,Y', 'operation': 'Load X register', 'bytes': 2, 'cycles': 4},
    'LDX': {'mode': 'Absolute', 'operation': 'Load X register', 'bytes': 3, 'cycles': 4},
    'LDX': {'mode': 'Absolute,Y', 'operation': 'Load X register', 'bytes': 3, 'cycles': 4},

    # LDY - Load Y register
    'LDY': {'mode': 'Immediate', 'operation': 'Load Y register', 'bytes': 2, 'cycles': 2},
    'LDY': {'mode': 'Zero Page', 'operation': 'Load Y register', 'bytes': 2, 'cycles': 3},
    'LDY': {'mode': 'Zero Page,X', 'operation': 'Load Y register', 'bytes': 2, 'cycles': 4},
    'LDY': {'mode': 'Absolute', 'operation': 'Load Y register', 'bytes': 3, 'cycles': 4},
    'LDY': {'mode': 'Absolute,X', 'operation': 'Load Y register', 'bytes': 3, 'cycles': 4},

    # LSR - Logical shift right
    'LSR': {'mode': 'Accumulator', 'operation': 'Logical shift right', 'bytes': 1, 'cycles': 2},
    'LSR': {'mode': 'Zero Page', 'operation': 'Logical shift right', 'bytes': 2, 'cycles': 5},
    'LSR': {'mode': 'Zero Page,X', 'operation': 'Logical shift right', 'bytes': 2, 'cycles': 6},
    'LSR': {'mode': 'Absolute', 'operation': 'Logical shift right', 'bytes': 3, 'cycles': 6},
    'LSR': {'mode': 'Absolute,X', 'operation': 'Logical shift right', 'bytes': 3, 'cycles': 7},

    # NOP - No operation
    'NOP': {'mode': 'Implied', 'operation': 'No operation', 'bytes': 1, 'cycles': 2},

    # ORA - Logical inclusive OR
    'ORA': {'mode': 'Immediate', 'operation': 'Logical inclusive OR', 'bytes': 2, 'cycles': 2},
    'ORA': {'mode': 'Zero Page', 'operation': 'Logical inclusive OR', 'bytes': 2, 'cycles': 3},
    # PHA - Push accumulator
    'PHA': {'mode': 'Implied', 'operation': 'Push accumulator', 'bytes': 1, 'cycles': 3},

    # PHP - Push processor status
    'PHP': {'mode': 'Implied', 'operation': 'Push processor status', 'bytes': 1, 'cycles': 3},

    # PLA - Pull accumulator
    'PLA': {'mode': 'Implied', 'operation': 'Pull accumulator', 'bytes': 1, 'cycles': 4},

    # PLP - Pull processor status
    'PLP': {'mode': 'Implied', 'operation': 'Pull processor status', 'bytes': 1, 'cycles': 4},

    # ROL - Rotate left
    'ROL': {'mode': 'Accumulator', 'operation': 'Rotate left', 'bytes': 1, 'cycles': 2},
    'ROL': {'mode': 'Zero Page', 'operation': 'Rotate left', 'bytes': 2, 'cycles': 5},
    'ROL': {'mode': 'Zero Page,X', 'operation': 'Rotate left', 'bytes': 2, 'cycles': 6},
    'ROL': {'mode': 'Absolute', 'operation': 'Rotate left', 'bytes': 3, 'cycles': 6},
    'ROL': {'mode': 'Absolute,X', 'operation': 'Rotate left', 'bytes': 3, 'cycles': 7},

    # ROR - Rotate right
    'ROR': {'mode': 'Accumulator', 'operation': 'Rotate right', 'bytes': 1, 'cycles': 2},
    'ROR': {'mode': 'Zero Page', 'operation': 'Rotate right', 'bytes': 2, 'cycles': 5},
    'ROR': {'mode': 'Zero Page,X', 'operation': 'Rotate right', 'bytes': 2, 'cycles': 6},
    'ROR': {'mode': 'Absolute', 'operation': 'Rotate right', 'bytes': 3, 'cycles': 6},
    'ROR': {'mode': 'Absolute,X', 'operation': 'Rotate right', 'bytes': 3, 'cycles': 7},

    # RTS - Return from subroutine
    'RTS': {'mode': 'Implied', 'operation': 'Return from subroutine', 'bytes': 1, 'cycles': 6},

    # SBC - Subtract with carry
    'SBC': {'mode': 'Immediate', 'operation': 'Subtract with carry', 'bytes': 2, 'cycles': 2},
    'SBC': {'mode': 'Zero Page', 'operation': 'Subtract with carry', 'bytes': 2, 'cycles': 3},
    'SBC': {'mode': 'Zero Page,X', 'operation': 'Subtract with carry', 'bytes': 2, 'cycles': 4},
    'SBC': {'mode': 'Absolute', 'operation': 'Subtract with carry', 'bytes': 3, 'cycles': 4},
    'SBC': {'mode': 'Absolute,X', 'operation': 'Subtract with carry', 'bytes': 3, 'cycles': 4},
    'SBC': {'mode': 'Absolute,Y', 'operation': 'Subtract with carry', 'bytes': 3, 'cycles': 4},
    'SBC': {'mode': 'Indirect,X', 'operation': 'Subtract with carry', 'bytes': 2, 'cycles': 6},
    'SBC': {'mode': 'Indirect,Y', 'operation': 'Subtract with carry', 'bytes': 2, 'cycles': 5},

    # SEC - Set carry flag
    'SEC': {'mode': 'Implied', 'operation': 'Set carry flag', 'bytes': 1, 'cycles': 2},

    # SED - Set decimal mode
    'SED': {'mode': 'Implied', 'operation': 'Set decimal mode', 'bytes': 1, 'cycles': 2},

    # SEI - Set interrupt disable
    'SEI': {'mode': 'Implied', 'operation': 'Set interrupt disable', 'bytes': 1, 'cycles': 2},

    # STA - Store accumulator
    'STA': {'mode': 'Zero Page', 'operation': 'Store accumulator', 'bytes': 2, 'cycles': 3},
    'STA': {'mode': 'Zero Page,X', 'operation': 'Store accumulator', 'bytes': 2, 'cycles': 4},
    'STA': {'mode': 'Absolute', 'operation': 'Store accumulator', 'bytes': 3, 'cycles': 4},
    'STA': {'mode': 'Absolute,X', 'operation': 'Store accumulator', 'bytes': 3, 'cycles': 5},
    'STA': {'mode': 'Absolute,Y', 'operation': 'Store accumulator', 'bytes': 3, 'cycles': 5},
    'STA': {'mode': 'Indirect,X', 'operation': 'Store accumulator', 'bytes': 2, 'cycles': 6},
    'STA': {'mode': 'Indirect,Y', 'operation': 'Store accumulator', 'bytes': 2, 'cycles': 6},

    # STY - Store Y register
    'STY': {'mode': 'Zero Page', 'operation': 'Store Y register', 'bytes': 2, 'cycles': 3},
    'STY': {'mode': 'Zero Page,X', 'operation': 'Store Y register', 'bytes': 2, 'cycles': 4},
    'STY': {'mode': 'Absolute', 'operation': 'Store Y register', 'bytes': 3, 'cycles': 4},

    # TAX - Transfer accumulator to X
    'TAX': {'mode': 'Implied', 'operation': 'Transfer accumulator to X', 'bytes': 1, 'cycles': 2},

    # TAY - Transfer accumulator to Y
    'TAY': {'mode': 'Implied', 'operation': 'Transfer accumulator to Y', 'bytes': 1, 'cycles': 2},

    # TSX - Transfer stack pointer to X
    'TSX': {'mode': 'Implied', 'operation': 'Transfer stack pointer to X', 'bytes': 1, 'cycles': 2},

    # TXA - Transfer X to accumulator
    'TXA': {'mode': 'Implied', 'operation': 'Transfer X to accumulator', 'bytes': 1, 'cycles': 2},

    # TXS - Transfer X to stack pointer
    'TXS': {'mode': 'Implied', 'operation': 'Transfer X to stack pointer', 'bytes': 1, 'cycles': 2},

    # TYA - Transfer Y to accumulator
    'TYA': {'mode': 'Implied', 'operation': 'Transfer Y to accumulator', 'bytes': 1, 'cycles': 2},

    # UNOFFICIAL OPCODES
    # (not all 6502 implementations support these opcodes)

    # AHX - Store A and X index registers into memory
    'AHX': {'mode': 'Absolute,Y', 'operation': 'Store A and X index registers into memory', 'bytes': 3, 'cycles': 5},
    'AHX': {'mode': 'Indirect,Y', 'operation': 'Store A and X index registers into memory', 'bytes': 2, 'cycles': 6},

    # ALR - AND accumulator with memory, then shift right
    'ALR': {'mode': 'Immediate', 'operation': 'AND accumulator with memory, then shift right', 'bytes': 2, 'cycles': 2},

    # ANC - AND accumulator with memory, then set carry flag
    'ANC': {'mode': 'Immediate', 'operation': 'AND accumulator with memory, then set carry flag', 'bytes': 2,
            'cycles': 2},

    # ARR - AND accumulator with memory, then rotate right
    'ARR': {'mode': 'Immediate', 'operation': 'AND accumulator with memory, then rotate right', 'bytes': 2,
            'cycles': 2},
    # DCP - Decrement memory, then compare with accumulator
    'DCP': {'mode': 'Zero Page', 'operation': 'Decrement memory, then compare with accumulator', 'bytes': 2,
            'cycles': 5},
    'DCP': {'mode': 'Zero Page,X', 'operation': 'Decrement memory, then compare with accumulator', 'bytes': 2,
            'cycles': 6},
    'DCP': {'mode': 'Absolute', 'operation': 'Decrement memory, then compare with accumulator', 'bytes': 3,
            'cycles': 6},
    'DCP': {'mode': 'Absolute,X', 'operation': 'Decrement memory, then compare with accumulator', 'bytes': 3,
            'cycles': 7},
    'DCP': {'mode': 'Absolute,Y', 'operation': 'Decrement memory, then compare with accumulator', 'bytes': 3,
            'cycles': 7},
    'DCP': {'mode': 'Indirect,X', 'operation': 'Decrement memory, then compare with accumulator', 'bytes': 2,
            'cycles': 8},
    'DCP': {'mode': 'Indirect,Y', 'operation': 'Decrement memory, then compare with accumulator', 'bytes': 2,
            'cycles': 8},

    # ISB - Increment memory, then subtract with carry
    'ISB': {'mode': 'Zero Page', 'operation': 'Increment memory, then subtract with carry', 'bytes': 2, 'cycles': 5},
    'ISB': {'mode': 'Zero Page,X', 'operation': 'Increment memory, then subtract with carry', 'bytes': 2, 'cycles': 6},
    'ISB': {'mode': 'Absolute', 'operation': 'Increment memory, then subtract with carry', 'bytes': 3, 'cycles': 6},
    'ISB': {'mode': 'Absolute,X', 'operation': 'Increment memory, then subtract with carry', 'bytes': 3, 'cycles': 7},
    'ISB': {'mode': 'Absolute,Y', 'operation': 'Increment memory, then subtract with carry', 'bytes': 3, 'cycles': 7},
    'ISB': {'mode': 'Indirect,X', 'operation': 'Increment memory, then subtract with carry', 'bytes': 2, 'cycles': 8},
    'ISB': {'mode': 'Indirect,Y', 'operation': 'Increment memory, then subtract with carry', 'bytes': 2, 'cycles': 8},

    # LAS - Load accumulator and X with stack memory
    'LAS': {'mode': 'Absolute,Y', 'operation': 'Load accumulator and X with stack memory', 'bytes': 3, 'cycles': 4},

    # LAX - Load accumulator and X with memory
    'LAX': {'mode': 'Zero Page', 'operation': 'Load accumulator and X with memory', 'bytes': 2, 'cycles': 3},
    'LAX': {'mode': 'Zero Page,Y', 'operation': 'Load accumulator and X with memory', 'bytes': 2, 'cycles': 4},

# RLA - Rotate left, then AND accumulator with memory
  'RLA': {'mode': 'Zero Page', 'operation': 'Rotate left, then AND accumulator with memory', 'bytes': 2, 'cycles': 5},
  'RLA': {'mode': 'Zero Page,X', 'operation': 'Rotate left, then AND accumulator with memory', 'bytes': 2, 'cycles': 6},
  'RLA': {'mode': 'Absolute', 'operation': 'Rotate left, then AND accumulator with memory', 'bytes': 3, 'cycles': 6},
  'RLA': {'mode': 'Absolute,X', 'operation': 'Rotate left, then AND accumulator with memory', 'bytes': 3, 'cycles': 7},
  'RLA': {'mode': 'Absolute,Y', 'operation': 'Rotate left, then AND accumulator with memory', 'bytes': 3, 'cycles': 7},
  'RLA': {'mode': 'Indirect,X', 'operation': 'Rotate left, then AND accumulator with memory', 'bytes': 2, 'cycles': 8},
  'RLA': {'mode': 'Indirect,Y', 'operation': 'Rotate left, then AND accumulator with memory', 'bytes': 2, 'cycles': 8},

    # RRA - Rotate right, then add with carry
    'RRA': {'mode': 'Zero Page', 'operation': 'Rotate right, then add with carry', 'bytes': 2, 'cycles': 5},
    'RRA': {'mode': 'Zero Page,X', 'operation': 'Rotate right, then add with carry', 'bytes': 2, 'cycles': 6},
    'RRA': {'mode': 'Absolute', 'operation': 'Rotate right, then add with carry', 'bytes': 3, 'cycles': 6},
    'RRA': {'mode': 'Absolute,X', 'operation': 'Rotate right, then add with carry', 'bytes': 3, 'cycles': 7},
    'RRA': {'mode': 'Absolute,Y', 'operation': 'Rotate right, then add with carry', 'bytes': 3, 'cycles': 7},
    'RRA': {'mode': 'Indirect,X', 'operation': 'Rotate right, then add with carry', 'bytes': 2, 'cycles': 8},
    'RRA': {'mode': 'Indirect,Y', 'operation': 'Rotate right, then add with carry', 'bytes': 2, 'cycles': 8},

    # SAX - Store AND of accumulator and X in memory
    'SAX': {'mode': 'Zero Page', 'operation': 'Store AND of accumulator and X in memory', 'bytes': 2, 'cycles': 3},
    'SAX': {'mode': 'Zero Page,Y', 'operation': 'Store AND of accumulator and X in memory', 'bytes': 2, 'cycles': 4},
    'SAX': {'mode': 'Absolute', 'operation': 'Store AND of accumulator and X in memory', 'bytes': 3, 'cycles': 4},

    # SKB - Skip next instruction if bit in memory is clear
    'SKB': {'mode': 'Immediate', 'operation': 'Skip next instruction if bit in memory is clear', 'bytes': 2,
            'cycles': 2},

    # SKW - Skip next instruction if bit in memory is set
    'SKW': {'mode': 'Immediate', 'operation': 'Skip next instruction if bit in memory is set', 'bytes': 2, 'cycles': 2},

    # SLO - Shift left, then OR accumulator with memory
    'SLO': {'mode': 'Zero Page', 'operation': 'Shift left, then OR accumulator with memory', 'bytes': 2, 'cycles': 5},
    'SLO': {'mode': 'Zero Page,X', 'operation': 'Shift left, then OR accumulator with memory', 'bytes': 2, 'cycles': 6},
    'SLO': {'mode': 'Absolute', 'operation': 'Shift left, then OR accumulator with memory', 'bytes': 3, 'cycles': 6},

    # SRE - Shift right, then EOR accumulator with memory
    'SRE': {'mode': 'Zero Page', 'operation': 'Shift right, then EOR accumulator with memory', 'bytes': 2, 'cycles': 5},
    'SRE': {'mode': 'Zero Page,X', 'operation': 'Shift right, then EOR accumulator with memory', 'bytes': 2,
            'cycles': 6},
    'SRE': {'mode': 'Absolute', 'operation': 'Shift right, then EOR accumulator with memory', 'bytes': 3, 'cycles': 6},
    'SRE': {'mode': 'Absolute,X', 'operation': 'Shift right, then EOR accumulator with memory', 'bytes': 3,
            'cycles': 7},
    'SRE': {'mode': 'Absolute,Y', 'operation': 'Shift right, then EOR accumulator with memory', 'bytes': 3,
            'cycles': 7},
    'SRE': {'mode': 'Indirect,X', 'operation': 'Shift right, then EOR accumulator with memory', 'bytes': 2,
            'cycles': 8},
    'SRE': {'mode': 'Indirect,Y', 'operation': 'Shift right, then EOR accumulator with memory', 'bytes': 2,
            'cycles': 8},

    # SYA - Store Y and accumulator in memory
    'SYA': {'mode': 'Absolute,X', 'operation': 'Store Y and accumulator in memory', 'bytes': 3, 'cycles': 5},

    # XAA - Transfer X to accumulator and AND with memory
    'XAA': {'mode': 'Immediate', 'operation': 'Transfer X to accumulator and AND with memory', 'bytes': 2, 'cycles': 2},

    # XAS - Transfer X to stack pointer and AND with accumulator
    'XAS': {'mode': 'Absolute,Y', 'operation': 'Transfer X to stack pointer and AND with accumulator', 'bytes': 3,
            'cycles': 5}






}

# Prompt the user for the file path
file_path = input("Enter the path of the assembly code file: ")

# Open the assembly code file in read-only mode
with open(file_path, 'r') as f:
    # Read each line of the file
    for line in f:
        # Strip leading and trailing whitespace from the line
        line = line.strip()

        # If the line is empty or a comment, skip it
        if not line or line.startswith(';'):
            continue

        # Split the line into fields delimited by whitespace
        fields = line.split()

        # The first field is the opcode
        opcode = fields[0]

        # The remaining fields are the operands
        operands = fields[1:]

        # Look up the full information for the opcode
        opcode_info = opcode_dict.get(opcode, {'mode': 'Unknown', 'operation': 'Unknown', 'bytes': 0, 'cycles': 0})

        # Print out the interpretation of the line
        print(
            f'{opcode}: {operands} ({opcode_info["mode"]} mode, {opcode_info["operation"]}, {opcode_info["bytes"]} bytes, {opcode_info["cycles"]} cycles)')