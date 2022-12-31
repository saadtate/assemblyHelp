# Open the file for reading
with open('logo start', 'r') as f:
  # Read the contents of the file
  text = f.read()

# Print the text
print(text)
print('')
print('')
print('                                     WELCOM TO ASSEMBLY HELPER V 0.2 ')
print('')
print('')
import subprocess

# Create a list of microprocessors
microprocessors = ['6502', 'Z80', 'M68000', 'Ricoh 5A22', '40xx', '80-xxx', 'MIPS R3000A', 'MIPS R4300i', 'Hitachi SH-X', 'Hitachi SH-2', 'Sharp z80']

# Sort the list alphabetically
microprocessors.sort()

# Print the list of microprocessors
print('Select a number from the following list:')
for i, processor in enumerate(microprocessors):
  print(f'{i+1}: {processor}')

# Create a dict that maps microprocessors to scripts
scripts = {
  '6502': '6502.py',
  'Z80': 'Z80.py',
  'M68000': 'moto68.py',
  'Ricoh 5A22': 'Ricoh5A22.py',
  '40xx': '40xx.py',
  '80-xxx': '80-xxx.py',
  'MIPS R3000A': 'MIPSR3000A.py',
  'MIPS R4300i': 'MIPSR4300i.py',
  'Hitachi SH-X': 'Hitachi SH-4.py'
  # ...and so on for each microprocessor
}

# Get the user's selection
selection = input('Enter a number: ')

# Determine which script to run based on the user's selection
selected_processor = microprocessors[int(selection)-1]
script = scripts[selected_processor]

# Run the script using the Python interpreter
subprocess.call(['python', script])
