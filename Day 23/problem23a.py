# This program emulates a very simple computer.
# The problem input is the computer program to be
# executed. The computer supports two registers
# and six instructions. The registers are named a
# and b, can hold any non-negative integer, and
# begin with a value of 0. The instructions are as
# follows:
# - hlf r sets register r to half its current
#   value, then continues with the next
#   instruction.
# - tpl r sets register r to triple its current
#   value, then continues with the next
#   instruction.
# - inc r increments register r, adding 1 to it,
#   then continues with the next instruction.
# - jmp offset is a jump; it continues with the
#   instruction offset away relative to itself.
# - jie r, offset is like jmp, but only jumps if
#   register r is even ("jump if even").
# - jio r, offset is like jmp, but only jumps if
#   register r is 1 ("jump if one", not odd).
# All three jump instructions work with an offset
# relative to that instruction.
#
# What is the value in register b when the program
# in your puzzle input is finished executing?

import time          # For timing the execution



# Read in the data file and convert it to a list
# of strings.
def readFile(filename):
   lines = []
   try:
      with open(filename, "r") as file:
         line = file.readline()
         while line:
            lines.append(line.replace('\n', ''))
            line = file.readline()

         file.close()
            
   except FileNotFoundError:
      print("Error: File not found!")
   except:
      print("Error: Can't read from file!")

   # Only need the first number (as a string).
   return lines



# Parse the file input into a list of instructions
# with each instruction as a tuple. The first
# element in the tuple is the mnemonic. There may
# be one or two operands which are either named
# registers (a or b) or an integer value.
def parseInput(values):
   program = list()
   for line in values:
      # Eliminate commas and split the instruction
      # into parts.
      line = line.replace(',', '')
      parts = line.split()
      this_line = list()
      
      # Iterate through the parts of the
      # instruction.
      for i in range(len(parts)):
         # If the instruction is a number, then
         # convert it to integer. Any number is
         # written with a prefix + or -.
         if (parts[i][0] == '+'):
            this_line.append(int(parts[i][1:]))         
         elif (parts[i][0] == '-'):
            this_line.append(int(parts[i]))
         # Otherwise, leave it as a string.
         else:
            this_line.append(parts[i])

      # Append the instruction as a tuple.
      program.append(tuple(this_line))

   # Return the program as a list of tuples.
   return program
         



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it to a list
   # of tuples which make up the input program.
   file_input = readFile("input23b.txt")
   program = parseInput(file_input)

   # Set up the registers.
   registers = dict()
   registers['a'] = 0
   registers['b'] = 0

   # Execute the program.
   index = 0
   while index < len(program):
      # hlf r sets register r to half its current
      # value, then continues with the next
      # instruction.
      if program[index][0] == 'hlf':
         registers[program[index][1]] //= 2
         index += 1
         
      # tpl r sets register r to triple its
      # current value, then continues with the
      # next instruction.
      elif program[index][0] == 'tpl':
         registers[program[index][1]] *= 3
         index += 1
         
      # inc r increments register r, adding 1 to
      # it, then continues with the next
      # instruction.
      elif program[index][0] == 'inc':
         registers[program[index][1]] += 1
         index += 1

      # jmp offset is a jump; it continues with
      # the instruction offset away relative to
      # itself.
      elif program[index][0] == 'jmp':
         index += program[index][1]

      # jie r, offset is like jmp, but only jumps
      # if register r is even ("jump if even").
      elif program[index][0] == 'jie':
         if registers[program[index][1]] % 2 == 0:
            index += program[index][2]
         else:
            index += 1

      # jio r, offset is like jmp, but only jumps
      # if register r is 1 ("jump if one", not
      # odd).
      elif program[index][0] == 'jio':
         if registers[program[index][1]] == 1:
            index += program[index][2]
         else:
            index += 1

      # The program exits when it tries to run an
      # instruction beyond the ones defined.
      else:
         print('Error: unknown instruction!')
         break
      
   # Display the value stored in register 'b'
   print('Value in register b = ' + str(registers['b']))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
