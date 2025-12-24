# The problem input consists of instructions on
# how to display the ideal lighting configuration.
# Lights in grid are numbered from 0 to 999 in
# each direction; the lights at each corner are at
# 0,0, 0,999, 999,999, and 999,0. The instructions
# include whether to turn on, turn off, or toggle
# various inclusive ranges given as coordinate
# pairs.
#
# After following the instructions, how many
# lights are lit?

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



# Convert the list of strings into a list of lists
# with each element of the inner list conveying an
# instruction for dealing with a series of lights.
# The first element in the inner list denotes
# whether the lights are toggled, turned on, or
# turned off. The second element provides the
# starting coordinates and the third element
# provides the ending coordinates for the series
# of lights for the given action.
def parseInput(values):
   instructions = list()
   for line in values:
      action = list()
      parts = line.split()

      # Determine toggle, on, or off.
      if parts[0] == 'toggle':
         action.append('toggle')
         parts = parts[1:]
      else:
         action.append(parts[1])
         parts = parts[2:]

      # Convert the starting and ending points.
      action.append([ int(i) for i in parts[0].split(',') ])
      action.append([ int(i) for i in parts[2].split(',') ])

      # Append the light series instructions.
      instructions.append(action)

   # Return the list of instructions
   return instructions

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   file_data = readFile("input6b.txt")
   instructions = parseInput(file_data)

   # Iterate through the lighting instructions.
   lights = set()
   for i in instructions:
      # For each instruction, iterate through the
      # specified lights.
      for y in range(i[1][1], i[2][1] + 1):
         for x in range(i[1][0], i[2][0] + 1):
            # If 'on', add the coordinates to the
            # light set.
            if i[0] == 'on':
               lights.add((x, y))

            # If 'off' and the light is on, then
            # turn it off (remove it from lights).
            if (i[0] == 'off') and ((x, y) in lights):
               lights.remove((x, y))

            # If 'toggle' then add it if off and
            # remove it if on.
            if (i[0] == 'toggle'):
               if (x, y) in lights:
                  lights.remove((x, y))
               else:
                  lights.add((x, y))

   # The number of lights on is the size of the
   # set.
   count = len(lights)

   # Display the results.
   print('Number of lights = ' + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
