sh4_opcodes = {
    "ADD": "000000",
    "ADDC": "000001",
    "ADDV": "000010",
    "AND": "000011",
    "ANDI": "000100",
    "ANDM": "000101",
    "BF": "000110",
    "BFS": "000111",
    "BRA": "001000",
    "BRAF": "001001",
    "BSR": "001010",
    "BSRF": "001011",
    "BT": "001100",
    "BTS": "001101",
    "CLR1": "001110",
    "CLRMAC": "001111",
    "CLRT": "010000",
    "CMPEQ": "010001",
    "CMPEQI": "010010",
    "CMPHS": "010011",
    "CMPHSI": "010100",
    "CMPGE": "010101",
    "CMPGEI": "010110",
    "CMPGT": "010111",
    "CMPGTI": "011000",
    "CMPHI": "011001",
    "CMPHSU": "011010",
    "CMPHSUI": "011011",
    "CMPLT": "011100",
    "CMPLTI": "011101",
    "CMPPL": "011110",
    "CMPPZ": "011111",
    "DIV0S": "100000",
    "DIV0U": "100001",
    "DIV1": "100010",
    "DMULS": "100011",
    "DMULU": "100100",
    "DT": "100101",
    "EXTSB": "100110",
    "EXTSW": "100111",
    "EXTUB": "101000",
    "EXTUW": "101001",
    "JMP": "101010",
    "JSR": "101011",
    "LDC": "101100",
    "LDCL": "101101",
    "LDCG": "101110",
    "LDCGL": "101111",
    "LDS": "110000",
    "LDSL": "110001",
    "LDSP": "110010",
    "LDSLP": "110011",
    "LDSG": "110100",
    "LDSGL": "110101",
    "LDSM": "110110",
    "LDSML": "110111",
    "LDT": "111000",
    "LDTL": "111001",
    "LDTU": "111010",
    "LDTUL": "111011",
    "LDSF": "111100",
    "LDSFL": "111101",
    "MACL": "111110",
    "MOV": "111111",
    "MOVI": "1000000",
    "MOVBL": "1000001",
    "MOVBS": "1000010",
"MOVWI": "1000011",
"MOVWU": "1000100",
"MOVW": "1000101",
"MOVLM": "1000110",
"MOVLL": "1000111",
"MOVBP": "1001000",
"MOVLP": "1001001",
"MOVUA": "1001010",
"MOVLA": "1001011",
"MOVA": "1001100",
"MOVT": "1001101",
"MULL": "1001110",
"MULS": "1001111",
"MULU": "1010000",
"NEG": "1010001",
"NEGC": "1010010",
"NOP": "1010011",
"NOT": "1010100",
"OR": "1010101",
"ORI": "1010110",
"ORM": "1010111",
"POP": "1011000",
"PUSH": "1011001",
"ROTCL": "1011010",
"ROTCR": "1011011",
"ROTL": "1011100",
"ROTR": "1011101",
"RTS": "1011110",
"SET1": "1011111",
"SETT": "1100000",
"SHAL": "1100001",
"SHAR": "1100010",
"SHLL": "1100011",
"SHLR": "1100100",
"SLEEP": "1100101",
"STC": "1100110",
"STCL": "1100111",
"STCG": "1101000",
"STCGL": "1101001",
"STS": "1101010",
"STSL": "1101011",
"STSP": "1101100",
"STSLP": "1101101",
"STSG": "1101110",
"STSGL": "1101111",
"STSM": "1110000",
"STSML": "1110001",
"STT": "1110010",
"STTL": "1110011",
"STTU": "1110100",
"STTUL": "1110101",
"STSF": "1110110",
"STSFL": "1110111",
"SUB": "1111000",
"SUBC": "1111001",
"SUBV": "1111010",
"SWAPB": "1111011",
"SWAPW": "1111100",
"TASB": "1111101",
"TRAPA": "1111110",
"TST": "1111111",
"TSTI": "10000000",
"TSTM": "10000001",
"XOR": "10000010",
"XORI": "10000011",
"XORM": "10000100",
"MOVCAL": "10000101",
"MOVCBL": "10000110",
"MOVCB": "10000111",
"MOVCHI": "10001000",
"MOVCLO": "10001001",
"MOVCWI": "10001010",
"MOVCWU": "10001011",
"MOVC": "100",
"MOVCA": "10001100",
"MOVCALG": "10001101",
"MOVCL": "10001110",
"MOVCALGP": "10001111",
"MOVCALP": "10010001",
"MOVCBLG": "10010010",
"MOVCBGP": "10010011",
"MOVCBLS": "10010100",
"MOVCBLP": "10010101",
"MOVCHIS": "10010110",
"MOVCHIL": "10010111",
"MOVCHISP": "10011000",
"MOVCHILP": "10011001",
"MOVCLOS": "10011010",
"MOVCLOL": "10011011",
"MOVCLOSP": "10011100",
"MOVCLOLP": "10011101",
"MOVCWP": "10011110",
"MOVCWPL": "10011111",
"MOVCWW": "10100000",
"MOVCWL": "10100001",
"MOVCWWP": "10100010",
"MOVCWLP": "10100011",
"MOVC": "10100100",
"MOVCGP": "10100101",
"MOVCG": "10100110",
"MOVCGP": "10100111",
"MOVCHISW": "10101000",
"MOVCHISL": "10101001",
"MOVCLOSW": "10101010",
"MOVCLOSL": "10101011",
"MOVCWLS": "10101100",
"MOVCWLL": "10101101",
"MOVCWWS": "10101110",
"MOVCWWL": "10101111",
"MOVCGLS": "10110000",
"MOVCGL": "10110001",
"MOVCGPW": "10110010",
"MOVCGPFL": "10110011",
"MOVCGPF": "10110100",
"MOVCGPFW": "10110101",
"MOVCGPFLP": "10110110",
"MOVCGPFP": "10110111",
"MOVCGPS": "10111000",
"MOVCGLP": "10111001",
"MOVCGPWP": "10111010",
"MOVCGPFLP": "10111011",
"MOVCGPFPP": "10111100",
"MOVCGLW": "10111101",
"MOVCGLPW": "10111110",
"MOVCGPFLW": "10111111",
"MOVCGPFPW": "11000000",
"MOVCGPFLPW": "11000001",
"MOVCGPFPPW": "11000010",
"MOVCGPFWP": "11000011",
"MOVCGPFLWP": "11000100",
"MOVCGPFPWP": "11000101",
"MOVCGLWP": "11000110",
"MOVCGLPWP": "11000111",
"MOVCGPFLWP": "11001000",
"MOVCGPFPWP": "11001001",
"MOVCGPFWPL": "11001010",
"MOVCGPFLWPL": "11001011",
"MOVCGPFPWPL": "11001100",
"MOVCGLWPL": "11001101",
"MOVCGLPWPL": "11001110",
"MOVCGPFLWPL": "11001111",
"MOVCGPFPWPL": "11010000",
"MOVCGPFWPFL": "11010001",
"MOVCGPFLWPFL": "11010010",
"MOVCGPFPWPFL": "11010011",
"MOVCGLWPFL": "11010100",
"MOVCGLPWPFL": "11010101",
"MOVCGPFLWPFL": "11010110",
"MOVCGPFPWPFL": "11010111",
"MOVCGPFWPFLP": "11011000",
"MOVCGPFLWPFLP": "11011001",
"MOVCGPFPWPFLP": "11011010",
"MOVCGLWPFLP": "11011011",
"MOVCGLPWPFLP": "11011100",
"MOVCGPFLWPFLP": "11011101",
"MOVCGPFPWPFLP": "11011110",
"MOVCAW": "11011111",
"MOVCAWP": "11100000",
"MOVCAWPL": "11100001",
"MOVCAWPFL": "11100010",
"MOVCAWPFLP": "11100011",
"MOVCAWPLP": "11100100",
"MOVCAP": "11100101",
"MOVCAPW": "11100110",
"MOVCAPWP": "11100111",
"MOVCAPWPL": "11101000",
"MOVCAPWPFLP": "11101001",
"MOVCAPWPLP": "11101010",
"MOVCAPL": "11101011",
"MOVCAPLP": "11101100",
"MOVCAPLW": "11101101",
"MOVCAPLWP": "11101110",
"MOVCAPLWPL": "11101111",
"MOVCAPLPFL": "11110000",
"MOVCAPLWPFL": "11110001",
"MOVCAPLPFLP": "11110010",
"MOVCAPLWPLP": "11110011",
"MOVCAFP": "11110100",
"MOVCAFPW": "11110101",
"MOVCAFPWP": "11110110",
"MOVCAFPWPL": "11110111",
"MOVCAFPWPFL": "11111000",
"MOVCAFPWPFLP": "11111001",
"MOVCAFPWPLP": "11111010",
"MOVCAFPL": "11111011",
"MOVCAFPLP": "11111100",
"MOVCAFPLW": "11111101",
"MOVCAFPLWP": "11111110",
"MOVCAFPLWPL": "11111111"
}





import os

# Define a dictionary of SH-4 instructions and their corresponding descriptions
descriptions = {
    "ADD": "Add two registers and store the result in a third register.",
    "ADDU": "Add two registers and store the result in a third register (unsigned).",
    "AND": "Bitwise AND two registers and store the result in a third register.",
    "BRAF": "Branch to an address specified by the sum of a register and an immediate value.",
    "BRSET": "Branch if a specified bit in a register is set to 1.",
    "CLRMAC": "Clear the MACL and MACH registers.",
    "CLRT": "Clear the T bit in the status register.",
    "CMPEQ": "Compare two registers and set the T bit in the status register if they are equal.",
    "CMPEQI": "Compare a register and an immediate value and set the T bit in the status register if they are equal.",
    "CMPGE": "Compare two registers and set the T bit in the status register if the first is greater than or equal to the second (signed).",
    "CMPGEI": "Compare a register and an immediate value and set the T bit in the status register if the first is greater than or equal to the second (signed).",
    "CMPGT": "Compare two registers and set the T bit in the status register if the first is greater than the second (signed).",
    "CMPGTI": "Compare a register and an immediate value and set the T bit in the status register if the first is greater than the second (signed).",
"CMPHI": "Compare two registers and set the T bit in the status register if the first is greater than the second (unsigned).",
"CMPHII": "Compare a register and an immediate value and set the T bit in the status register if the first is greater than the second (unsigned).",
"CMPPL": "Compare two registers and set the T bit in the status register if the first is less than the second (signed).",
"CMPPLI": "Compare a register and an immediate value and set the T bit in the status register if the first is less than the second (signed).",
"CMPU": "Compare two registers and set the T bit in the status register if they are not equal (unsigned).",
"CMPUI": "Compare a register and an immediate value and set the T bit in the status register if they are not equal (unsigned).",
"DIV0S": "Divide two registers and set the Q and M registers based on the result (signed).",
"DIV0U": "Divide two registers and set the Q and M registers based on the result (unsigned).",
"DIV1": "Divide two registers and store the result in a third register.",
"DMULS": "Multiply two registers and store the result in the MACL and MACH registers (signed).",
"CMPHI": "Compare two registers and set the T bit in the status register if the first is greater than the second (unsigned).",
"CMPHII": "Compare a register and an immediate value and set the T bit in the status register if the first is greater than the second (unsigned).",
"CMPPL": "Compare two registers and set the T bit in the status register if the first is less than the second (signed).",
"CMPPLI": "Compare a register and an immediate value and set the T bit in the status register if the first is less than the second (signed).",
"CMPU": "Compare two registers and set the T bit in the status register if they are not equal (unsigned).",
"CMPUI": "Compare a register and an immediate value and set the T bit in the status register if they are not equal (unsigned).",
"DIV0S": "Divide two registers and set the Q and M registers based on the result (signed).",
"DIV0U": "Divide two registers and set the Q and M registers based on the result (unsigned).",
"DIV1": "Divide two registers and store the result in a third register.",
"DMULS": "Multiply two registers and store the result in the MACL and MACH registers (signed).",
"DMULU": "Multiply two registers and store the result in the MACL and MACH registers (unsigned).",
"DT": "Decrement the value in a register and set the T bit in the status register if the result is 0.",
"EXTSB": "Sign-extend a byte in a register to a word and store the result in another register.",
"EXTSH": "Sign-extend a halfword in a register to a word and store the result in another register.",
"EXTUB": "Zero-extend a byte in a register to a word and store the result in another register.",
"EXTUH": "Zero-extend a halfword in a register to a word and store the result in another register.",
"FADD": "Add two single-precision floating-point values and store the result in a third register.",
"FADDS": "Add two single-precision floating-point values and store the result in a third register.",
"FADDD": "Add two double-precision floating-point values and store the result in a third register.",
"FADDDR": "Add two double-precision floating-point values and store the result in a third register.",
"FADD4S": "Add four single-precision floating-point values and store the result in a fourth register.",
"FSUB": "Subtract one single-precision floating-point value from another and store the result in a third register.",
"FSUBS": "Subtract one single-precision floating-point value from another and store the result in a third register.",
"FSUBD": "Subtract one double-precision floating-point value from another and store the result in a third register.",
"FSUBDR": "Subtract one double-precision floating-point value from another and store the result in a third register.",
"FMUL": "Multiply two single-precision floating-point values and store the result in a third register.",
"FMULS": "Multiply two single-precision floating-point values and store the result in a third register.",
"FMULD": "Multiply two double-precision floating-point values and store the result in a third register.",
"FMULDR": "Multiply two double-precision floating-point values and store the result.",
"FDIV": "Divide one single-precision floating-point value by another and store the result in a third register.",
"FDIVS": "Divide one single-precision floating-point value by another and store the result in a third register.",
"FDIVD": "Divide one double-precision floating-point value by another and store the result in a third register.",
"FDIVDR": "Divide one double-precision floating-point value by another and store the result in a third register.",
"FMOVS": "Move a single-precision floating-point value from one register to another.",
"FMOVD": "Move a double-precision floating-point value from one register to another.",
"FMOVSX": "Move a single-precision floating-point value from a register to a double-precision floating-point register.",
"FMOVSXD": "Move a single-precision floating-point value from a register to a double-precision floating-point register.",
"FMOVDX": "Move a double-precision floating-point value from a register to a single-precision floating-point register.",
"FMOVDXS": "Move a double-precision floating-point value from a register to a single-precision floating-point register.",
"FMOVSZ": "Move a single-precision floating-point value from a register to a double-precision floating-point register and clear the low-order 32 bits.",
"FMOVDZ": "Move a double-precision floating-point value from a register to a single-precision floating-point register and clear the high-order 32 bits.",
"FMOVSQ": "Move a single-precision floating-point value from a register to a double-precision floating-point register and set the low-order 32 bits to 1.",
"FMOVDQ": "Move a double-precision floating-point value from a register to a single-precision floating-point register and set the high-order 32 bits to 1.",
"FMOVS4": "Move four single-precision floating-point values from four registers to four other registers.",
"FMOVD4": "Move four double-precision floating-point values from four registers to four other registers.",
"FMOVSX4": "Move four single-precision floating-point values from four registers to four double-precision floating-point registers.",
"FMOVDX4": "Move four double-precision floating-point values from four registers to four single-precision floating-point registers.",
"FMOVSZ4": "Move four single-precision floating-point values from four registers to four double-precision floating-point registers and clear the low-order 32 bits.",
"FMOVDZ4": "Move four double-precision floating-point values from four registers to four single-precision floating-point registers and clear the high-order 32 bits.",
"FMOVSQ4": "Move four single-precision floating-point values from four registers to four double-precision floating-point registers and set the low-order 32 bits to 1.",
"FMOVDQ4": "Move four double-precision floating-point values from four",
"FMOVS4R": "Move four single-precision floating-point values from four registers to four other registers.",
"FMOVD4R": "Move four double-precision floating-point values from four registers to four other registers.",
"FMOVSX4R": "Move four single-precision floating-point values from four registers to four double-precision floating-point registers.",
"FMOVDX4R": "Move four double-precision floating-point values from four registers to four single-precision floating-point registers.",
"FMOVSZ4R": "Move four single-precision floating-point values from four registers to four double-precision floating-point registers and clear the low-order 32 bits.",
"FMOVDZ4R": "Move four double-precision floating-point values from four registers to four single-precision floating-point registers and clear the high-order 32 bits.",
"FMOVSQ4R": "Move four single-precision floating-point values from four registers to four double-precision floating-point registers and set the low-order 32 bits to 1.",
"FMOVDQ4R": "Move four double-precision floating-point values from four registers to four single-precision floating-point registers and set the high-order 32 bits to 1.",
"FMOVSXR": "Move a single-precision floating-point value from a register to a double-precision floating-point register.",
"FMOVDXR": "Move a double-precision floating-point value from a register to a single-precision floating-point register.",
"FMOVSZR": "Move a single-precision floating-point value from a register to a double-precision floating-point register and clear the low-order 32 bits.",
"FMOVDZR": "Move a double-precision floating-point value from a register to a single-precision floating-point register and clear the high-order 32 bits.",
"FMOVSQR": "Move a single-precision floating-point value from a register to a double-precision floating-point register and set the low-order 32 bits to 1.",
"FMOVDQR": "Move a double-precision floating-point value from a register to a single-precision floating-point register and set the high-order 32 bits to 1.",
"FMOVSZR4": "Move four single-precision floating-point values from four registers to four double-precision floating-point registers and clear the low-order 32 bits.",
"FMOVDZR4": "Move four double-precision floating-point values from four registers to four single-precision floating-point registers and clear the high-order 32 bits.",
"FMOVSQR4": "Move four single-precision floating-point values from four registers to four double-precision floating-point registers and set the low-order 32 bits to 1.",
"FMOVDQR4": "Move four double-precision floating-point values from four registers to four single-precision floating-point registers and set the high-order 32 bits to 1.",
"FCNVDS": "Convert a double-precision floating-point value to a single-precision floating",
"FCNVSD": "Convert a single-precision floating-point value to a double-precision floating-point value.",
"FCNVDSB": "Convert a double-precision floating-point value to a single-precision floating-point value and store the result in a register.",
"FCNVSDW": "Convert a single-precision floating-point value to a double-precision floating-point value and store the result in a register.",
"FCNVDSL": "Convert a double-precision floating-point value to a single-precision floating-point value and store the result in a register.",
"FCNVSDM": "Convert a single-precision floating-point value to a double-precision floating-point value and store the result in a register.",
"FCNVDSN": "Convert a double-precision floating-point value to a single-precision floating-point value and store the result in a register.",
"FCNVDSB4": "Convert four double-precision floating-point values to four single-precision floating-point values and store the results in four registers.",
"FCNVSDW4": "Convert four single-precision floating-point values to four double-precision floating-point values and store the results in four registers.",
"FCNVDSL4": "Convert four double-precision floating-point values to four single-precision floating-point values and store the results in four registers.",
"FCNVDSM4": "Convert four single-precision floating-point values to four double-precision floating-point values and store the results in four registers.",
"FCNVDSN4": "Convert four double-precision floating-point values to four single-precision floating-point values and store the results in four registers.",
"FCNVDSB4R": "Convert four double",
"FCNVSDW4R": "Convert four single-precision floating-point values to four double-precision floating-point values and store the results in four registers.",
"FCNVDSL4R": "Convert four double-precision floating-point values to four single-precision floating-point values and store the results in four registers.",
"FCNVDSM4R": "Convert four single-precision floating-point values to four double-precision floating-point values and store the results in four registers.",
"FCNVDSN4R": "Convert four double-precision floating-point values to four single-precision floating-point values and store the results in four registers.",
"FCNVDSB8": "Convert eight double-precision floating-point values to eight single-precision floating-point values and store the results in eight registers.",
"FCNVDSW8": "Convert eight single-precision floating-point values to eight double-precision floating-point values and store the results in eight registers.",
"FCNVDSL8": "Convert eight double-precision floating-point values to eight single-precision floating-point values and store the results in eight registers.",
"FCNVDSM8": "Convert eight single-precision floating-point values to eight double-precision floating-point values and store the results in eight registers.",
"FCNVDSN8": "Convert eight double-precision floating-point values to eight single-precision floating-point values and store the results in eight registers.",
"FCNVDSB8R": "Convert eight double-precision floating-point values to eight single-precision floating-point values and store the results in eight registers.",
"FCNVDSW8R": "Convert eight single-precision floating-point values to eight double-precision floating-point values and store the results in eight registers.",
"FCNVDSL8R": "Convert eight double-precision floating-point values to eight single-precision floating-point values and store the results in eight registers.",
"FCNVDSM8R": "Convert eight single-precision floating-point values to eight double-precision floating-point values and store the results in eight registers.",
"FCNVDSN8R": "Convert eight double-precision floating-point values to eight single-precision floating-point values and store the results in eight registers.",
"FCNVDSB12": "Convert twelve double-precision floating-point values to twelve single-precision floating-point values and store the results in twelve registers.",
"FCNVDSW12": "Convert twelve single-precision floating-point values to twelve double-precision floating-point values and store the results in twelve registers.",
"FCNVDSL12": "Convert twelve double-precision floating-point values to twelve single-precision floating-point values and store the results in twelve registers.",
"FCNVDSM12": "Convert twelve single-precision floating-point values to twelve double-precision floating-point values and store the results in twelve registers.",
"FCNVDSN12": "Convert twelve double-precision floating-point values to twelve single-precision floating-point values and store the results in twelve registers.",
"FCNVDSB12R": "Convert twelve double-pre",
"FCNVDSW12R": "Convert twelve single-precision floating-point values to twelve double-precision floating-point values and store the results in twelve registers.",
"FCNVDSL12R": "Convert twelve double-precision floating-point values to twelve single-precision floating-point values and store the results in twelve registers.",
"FCNVDSM12R": "Convert twelve single-precision floating-point values to twelve double-precision floating-point values and store the results in twelve registers.",
"FCNVDSN12R": "Convert twelve double-precision floating-point values to twelve single-precision floating-point values and store the results in twelve registers.",
"FCNVDSB16": "Convert sixteen double-precision floating-point values to sixteen single-precision floating-point values and store the results in sixteen registers.",
"FCNVDSW16": "Convert sixteen single-precision floating-point values to sixteen double-precision floating-point values and store the results in sixteen registers.",
"FCNVDSL16": "Convert sixteen double-precision floating-point values to sixteen single-precision floating-point values and store the results in sixteen registers.",
"FCNVDSM16": "Convert sixteen single-precision floating-point values to sixteen double-precision floating-point values and store the results in sixteen registers.",
"FCNVDSN16": "Convert sixteen double-precision floating-point values to sixteen single-precision floating-point values and store the results in sixteen registers.",
"FCNVDSB16R": "Convert sixteen double-precision floating-point values to sixteen single-precision floating-point values and store the results in sixteen registers.",
"FCNVDSW16R": "Convert sixteen single-precision floating-point values to sixteen double-precision floating-point values and store the results in sixteen registers.",
"FCNVDSL16R": "Convert sixteen double-precision floating-point values to sixteen single-precision floating-point values and store the results in sixteen registers.",
"FCNVDSM16R": "Convert sixteen single-precision floating-point values to sixteen double-precision floating-point values and store the results in sixteen registers.",
"FCNVDSN16R": "Convert sixteen double-precision floating-point values to sixteen single-precision floating-point values and store the results in sixteen registers.",
"FCMPEQS": "Compare two single-precision floating-point values for equality.",
"FCMPEQD": "Compare two double-precision floating-point values for equality.",
"FCMPGTS": "Compare two single-precision floating-point values for greater than.",
"FCMPGTD": "Compare two double-precision floating-point values for greater than.",
"FCMPGES": "Compare two single-precision floating-point values for greater than or equal.",
"FCMPGED": "Compare two double-precision floating-point values for greater than or equal.",
"FCMPLTS": "Compare two single-precision floating-point values for less than.",
"FCMPLTD": "Compare two double-precision floating-point values for less than.",
"FCMPLES": "Compare two single-precision floating-point values for less than or equal.",
"FCMPLED": "Compare two double-precision floating-point values for less than or equal.",
"FCNVDSD": "Convert a double-precision floating-point value to a single-precision floating-point value.",
"FCNVDSW": "Convert a single-precision floating-point value to a double-precision floating-point value and store the result in a register.",
"FCNVDSL": "Convert a double-precision floating-point value to a single-precision floating-point value and store the result in a register.",
"FCNVDSM": "Convert a single-precision floating-point value to a double-precision floating-point value and store the result in a register.",
"FCNVDSN": "Convert a double-precision floating-point value to a single-precision floating-point value and store the result in a register.",
"FADD": "Add two double-precision floating-point values and store the result in a register.",
"FADDS": "Add two single-precision floating-point values and store the result in a register.",
"FADDDR": "Add two double-precision floating-point values and store the result in a register.",
"FADDSR": "Add two single-precision floating-point values and store the result in a register.",
"FADDI": "Add an integer to a double-precision floating-point value and store the result in a register.",
"FADDIS": "Add an integer to a single-precision floating-point value and store the result in a register.",
"FADDID": "Add an integer to a double-precision floating-point value and store the result in a register.",
"FADDIDR": "Add an integer to a double-precision floating-point value and store the result in a register.",
"FADDIU": "Add an unsigned integer to a double-precision floating-point value and store the result in a register.",
"FADDIS": "Add an unsigned integer to a single-precision floating-point value and store the result in a register.",
"FADDIU": "Add an unsigned integer to a double-precision floating-point value and store the result in a register.",
"FADDIUR": "Add an unsigned integer to a double-precision floating-point value and store the result in a register.",
"FDIV": "Divide one double-precision floating-point value by another and store the result in a register.",
"FDIVS": "Divide one single-precision floating-point value by another and store the result in a register.",
"FDIVDR": "Divide one double-precision floating-point value by another and store the result in a register.",
"FDIVSR": "Divide one single-precision floating-point value by another and store the result in a register.",
"FDIVI": "Divide a double-precision floating-point value by an integer and store the result in a register.",
"FDIVIS": "Divide a single-precision floating-point value by an integer and store the result in a register.",
"FDIVID": "Divide a double-precision floating-point value by an integer and store the result in a register.",
"FDIVIDR": "Div",
"FDIVIU": "Divide a double-precision floating-point value by an unsigned integer and store the result in a register.",
"FDIVIS": "Divide a single-precision floating-point value by an unsigned integer and store the result in a register.",
"FDIVIU": "Divide a double-precision floating-point value by an unsigned integer and store the result in a register.",
"FDIVIUR": "Divide a double-precision floating-point value by an unsigned integer and store the result in a register.",
"FMAC": "Multiply two double-precision floating-point values and add the result to a third double-precision floating-point value.",
"FMACS": "Multiply two single-precision floating-point values and add the result to a third single-precision floating-point value.",
"FMACDR": "Multiply two double-precision floating-point values and add the result to a third double-precision floating-point value.",
"FMACSR": "Multiply two single-precision floating-point values and add the result to a third single-precision floating-point value.",
"FMUL": "Multiply two double-precision floating-point values and store the result in a register.",
"FMULS": "Multiply two single-precision floating-point values and store the result in a register.",
"FMULDR": "Multiply two double-precision floating-point values and store the result in a register.",
"FMULSR": "Multiply two single-precision floating-point values and store the result in a register.",
"FSUB": "Subtract one double-precision floating-point value from another and store the result in a register.",
"FSUBS": "Subtract one",
"FSUBDR": "Subtract one double-precision floating-point value from another and store the result in a register.",
"FSUBSR": "Subtract one single-precision floating-point value from another and store the result in a register.",
"FTRC": "Truncate a double-precision floating-point value and store the result in a register.",
"FTRCS": "Truncate a single-precision floating-point value and store the result in a register.",
"FTRCDR": "Truncate a double-precision floating-point value and store the result in a register.",
"FTRCSR": "Truncate a single-precision floating-point value and store the result in a register.",
"FIPR": "Interpolate two single-precision floating-point values and store the result in a register.",
"FSCA": "Perform a fast cosine approximation and store the result in a register.",
"FTRV": "Perform a matrix-vector multiplication and store the result in a register.",
"FADDX": "Add two double-precision floating-point values and store the result in a register.",
"FADDXS": "Add two single-precision floating-point values and store the result in a register.",
"FADDXDR": "Add two double-precision floating-point values and store the result in a register.",
"FADDXSR": "Add two single-precision floating-point values and store the result in a register.",
"FADDXI": "Add an integer to a double-precision floating-point value and store the result in a register.",
"FADDXIS": "Add an integer to a single-precision floating-point value and store the result in a register.",
"FADDXID": "Add an integer to a double-precision floating-point value and store the result in a register.",
"FADDXIDR": "Add an integer to a double-precision floating-point value and store the result in a register.",
"FADDXIU": "Add an unsigned integer to a double-precision floating-point value and store the result in a register.",
"FADDXIS": "Add an unsigned integer to a single-precision floating-point value and store the result in a register.",
"FADDXIU": "Add an unsigned integer to a double-precision floating-point value and store the result in a register.",
"FADDXIUR": "Add an unsigned integer to a double-precision floating-point value and store the result in a register.",
"FDIVX": "Divide one double-precision floating-point value by another and store the result in a register.",
"FDIVXS": "Divide one single-precision floating-point value by another and store the result in a register.",
"FDIVXDR": "Divide one double-precision floating-point value by another and store the result in a register.",
"FDIVXSR": "Divide one single-precision floating-point value by another and store the result in a register.",
"FDIVXI": "Divide a double-precision floating-point value by an integer and store the result in a register.",
"FDIVXIS": "Div.",
"FDIVXID": "Divide a double-precision floating-point value by an integer and store the result in a register.",
"FDIVXIDR": "Divide a double-precision floating-point value by an integer and store the result in a register.",
"FDIVXIU": "Divide a double-precision floating-point value by an unsigned integer and store the result in a register.",
"FDIVXIS": "Divide a single-precision floating-point value by an unsigned integer and store the result in a register.",
"FDIVXIU": "Divide a double-precision floating-point value by an unsigned integer and store the result in a register.",
"FDIVXIUR": "Divide a double-precision floating-point value by an unsigned integer and store the result in a register.",
"FMACX": "Multiply two double-precision floating-point values and add the result to a third double-precision floating-point value.",
"FMACXS": "Multiply two single-precision floating-point values and add the result to a third single-precision floating-point value.",
"FMACXDR": "Multiply two double-precision floating-point values and add the result to a third double-precision floating-point value.",
"FMACXSR": "Multiply two single-precision floating-point values and add the result to a third single-precision floating-point value.",
"FMULX": "Multiply two double-precision floating-point values and store the result in a register.",
"FMULXS": "Multiply two single-precision floating-point values and store the result in a register.",
"FMULXDR": "Multiply two double-precision floating-point values and store the result in a register.",
"FMULXSR": "Multiply two single-precision floating-point values and store the result in a register.",
"FSUBX": "Subtract one double-precision floating-point value from another and store the result in a register.",
"FSUBXS": "Subtract one single-precision floating-point value from another and store the result in a register.",
"FSUBXDR": "Subtract one double-precision floating-point value from another and store the result in a register.",
"FSUBXSR": "Subtract one single-precision floating-point value from another and store the result in a register.",
"FTRCX": "Truncate a double-precision floating-point value and store the result in a register.",
"FTRCXS": "Truncate a single-precision floating-point value and store the result in a register.",
"FTRCXDR": "Truncate a double-precision floating-point value and store the result in a register.",
"FTRCXSR": "Truncate a single-precision floating-point value and store the result in a register.",
"FIPRX": "Interpolate two single-precision floating-point values and store the result in a register.",
"FSCAX": "Perform a fast cosine approximation and store the result in a register.",
"FTRVX": "Perform a",
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










