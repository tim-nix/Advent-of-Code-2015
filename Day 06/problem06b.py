# The problem input consists of instructions on
# how to display the ideal lighting configuration.
# Lights in grid are numbered from 0 to 999 in
# each direction; the lights at each corner are at
# 0,0, 0,999, 999,999, and 999,0. The light grid
# actually has individual brightness controls;
# each light can have a brightness of zero or
# more. The lights all start at zero.
# - The phrase turn on actually means that you
#   should increase the brightness of those lights
#   by 1.
# - The phrase turn off actually means that you
#   should decrease the brightness of those lights
#   by 1, to a minimum of zero.
# - The phrase toggle actually means that you
#   should increase the brightness of those lights
#   by 2.
#
# What is the total brightness of all lights
# combined after following Santa's instructions?

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
   lights = dict()
   for i in instructions:
      # For each instruction, iterate through the
      # specified lights.
      for y in range(i[1][1], i[2][1] + 1):
         for x in range(i[1][0], i[2][0] + 1):
            # If 'on' and already in dict, then
            # increment. Otherwise, add to dict.
            if i[0] == 'on':
               if (x, y) in lights:
                  lights[(x, y)] += 1
               else:
                  lights[(x, y)] = 1

            # If 'off' and the light is on, then
            # decrement brightness. If brightness
            # is below zero, then remove it.
            if i[0] == 'off':
               if (x, y) in lights:
                  lights[(x, y)] -= 1
                  if lights[(x, y)] < 0:
                     del lights[(x, y)]

            # If 'toggle' then add it if off and
            # remove it if on.
            if (i[0] == 'toggle'):
               if (x, y) in lights:
                  lights[(x, y)] += 2
               else:
                  lights[(x, y)] = 2

   # Iterate through the dict and total the
   # brightness.
   count = 0
   for key in lights:
      count += lights[key]

   # Display the results.
   print('Total brightness of lights = ' + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
