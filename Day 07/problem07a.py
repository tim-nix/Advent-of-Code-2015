# The problem input consists of instructions for
# building a digital circuit. Each wire has an
# identifier (some lowercase letters) and can
# carry a 16-bit signal (0 to 65535). A signal is
# provided to each wire by a gate, another wire,
# or some specific value. Each wire can only get a
# signal from one source, but can provide its
# signal to multiple destinations. A gate provides
# no signal until all of its inputs have a signal.
# The instructions describe how to connect the
# parts together:
# - 123 -> x means that the signal 123 is provided
#   to wire x;
# - x AND y -> z means that the bitwise AND of
#   wire x and wire y is provided to wire z;
# - p LSHIFT 2 -> q means that the value from wire
#   p is left-shifted by 2 and then provided to
#   wire q.
# - NOT e -> f means that the bitwise complement
#   of the value from wire e is provided to wire f.
# - Other possible gates include OR (bitwise OR)
#   and RSHIFT (right-shift).
#
# Determine what signal is ultimately provided to
# wire a.

import time     # For timing the execution

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
   
   return lines



# Convert the string representation of each
# instruction to a list split on the spaces.
def parseInput(values):
   booklet = list()
   for line in values:
      booklet.append(line.split())

   # Return the booklet of instructions.
   return booklet

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   file_data = readFile("input7b.txt")
   booklet = parseInput(file_data)

   # Continue to execute instructions as long as
   # there are instructions to execute.
   wires = dict()
   while len(booklet) > 0:
      next_round = list()
      # Iterate through each instruction.
      for ops in booklet:
         try:
            # Assignment
            if len(ops) == 3:
               if ops[0].isnumeric():
                  wires[ops[2]] = int(ops[0])
               else:
                  wires[ops[2]] = wires[ops[0]]

            # NOT operation
            if len(ops) == 4:
               if ops[1].isnumeric():
                  wires[ops[3]] = ~int(ops[0]) & 0xFFFF
               else:
                  wires[ops[3]] = ~wires[ops[1]] & 0xFFFF

            # Binary operators
            if len(ops) == 5:
               if ops[1] == 'AND':
                  if ops[0].isnumeric() and ops[2].isnumeric():
                     wires[ops[4]] = (int(ops[0]) & int(ops[2])) & 0xFFFF
                  elif ops[0].isnumeric():
                     wires[ops[4]] = (int(ops[0]) & wires[ops[2]]) & 0xFFFF
                  elif ops[2].isnumeric():
                     wires[ops[4]] = (wires[ops[0]] & int(ops[2])) & 0xFFFF
                  else:
                     wires[ops[4]] = (wires[ops[0]] & wires[ops[2]]) & 0xFFFF

               if ops[1] == 'OR':
                  if ops[0].isnumeric() and ops[2].isnumeric():
                     wires[ops[4]] = (int(ops[0]) | int(ops[2])) & 0xFFFF
                  elif ops[0].isnumeric():
                     wires[ops[4]] = (int(ops[0]) | wires[ops[2]]) & 0xFFFF
                  elif ops[2].isnumeric():
                     wires[ops[4]] = (wires[ops[0]] | int(ops[2])) & 0xFFFF
                  else:
                     wires[ops[4]] = (wires[ops[0]] | wires[ops[2]]) & 0xFFFF

               if ops[1] == 'LSHIFT':
                  if ops[0].isnumeric() and ops[2].isnumeric():
                     wires[ops[4]] = (int(ops[0]) << int(ops[2])) & 0xFFFF
                  elif ops[0].isnumeric():
                     wires[ops[4]] = (int(ops[0]) << wires[ops[2]]) & 0xFFFF
                  elif ops[2].isnumeric():
                     wires[ops[4]] = (wires[ops[0]] << int(ops[2])) & 0xFFFF
                  else:
                     wires[ops[4]] = (wires[ops[0]] << wires[ops[2]]) & 0xFFFF

               if ops[1] == 'RSHIFT':
                  if ops[0].isnumeric() and ops[2].isnumeric():
                     wires[ops[4]] = (int(ops[0]) >> int(ops[2])) & 0xFFFF
                  elif ops[0].isnumeric():
                     wires[ops[4]] = (int(ops[0]) >> wires[ops[2]]) & 0xFFFF
                  elif ops[2].isnumeric():
                     wires[ops[4]] = (wires[ops[0]] >> int(ops[2])) & 0xFFFF
                  else:
                     wires[ops[4]] = (wires[ops[0]] >> wires[ops[2]]) & 0xFFFF

         # A KeyError exception will be thrown if
         # the operand(s) of the instruction are
         # not known. Add this instruction to the
         # next_round list for attempting it at
         # the next round.
         except KeyError:
            next_round.append(ops)
            continue

      # Reassign booklet to those instructions
      # that were not executed.
      booklet = next_round

   # Display the results on wire a.
   print('Value on wire a = ' + str(wires['a']))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
