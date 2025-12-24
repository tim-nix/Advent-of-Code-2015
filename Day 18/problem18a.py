# The problem input depicts the initial configur-
# ation of a 100x100 grid of lights. A "#" means
# 'on', and a "." means 'off'. Then, each step
# decides the next configuration based on the
# current one. Each light's next state (either on
# or off) depends on its current state and the
# current states of the eight lights adjacent to
# it (including diagonals). The state a light
# should have next is based on its current state
# (on or off) plus the number of neighbors that
# are on:
# - A light which is on stays on when 2 or 3
#   neighbors are on, and turns off otherwise.
# - A light which is off turns on if exactly 3
#   neighbors are on, and stays off otherwise.
# - All of the lights update simultaneously; they
#   all consider the same current state before
#   moving to the next.
#
# Given the initial configuration, how many lights
# are on after 100 steps?

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



# Convert the light grid into a set of light
# coordinates that are 'on'.
def parseInput(values):
   lights_on = set()

   # Iterate through each row and add to the set
   # if the location x, y is marked by '#'.
   for y in range(len(values)):
      for x in range(len(values[y])):
         if values[y][x] == '#':
            lights_on.add((x, y))

   # Return the set of lights that are 'on'.
   return lights_on



# Given a location (x, y), determine if the value
# is a legal location on the grid; that is, within
# 0 <= x < max_x and 0 <= y < max_y.
def isInBounds(x, y, max_coords):
   max_x, max_y = max_coords
   if (x >= 0) and (y >= 0):
      if (x < max_x) and (y < max_y):
         return True

   return False


# For the given x,y location, count the number of
# neighbors that are 'on' to determine whether the
# light at x,y turns 'on', stays 'on', or turns
# 'off'.
def updateLight(x, y, max_coords, lights_on):
   # Count the number of neighbors that are 'on'.
   count = 0
   if isInBounds(x - 1, y - 1, max_coords) and ((x - 1, y - 1) in lights_on):
      count += 1
   if isInBounds(x, y - 1, max_coords) and ((x, y - 1) in lights_on):
      count += 1
   if isInBounds(x + 1, y - 1, max_coords) and ((x + 1, y - 1) in lights_on):
      count += 1
   if isInBounds(x - 1, y, max_coords) and ((x - 1, y) in lights_on):
      count += 1
   if isInBounds(x + 1, y, max_coords) and ((x + 1, y) in lights_on):
      count += 1
   if isInBounds(x - 1, y + 1, max_coords) and ((x - 1, y + 1) in lights_on):
      count += 1
   if isInBounds(x, y + 1, max_coords) and ((x, y + 1) in lights_on):
      count += 1
   if isInBounds(x + 1, y + 1, max_coords) and ((x + 1, y + 1) in lights_on):
      count += 1

   # A light which is 'on' stays on when 2 or 3
   # neighbors are 'on', and turns 'off'
   # otherwise.
   if (x, y) in lights_on:
      if (count == 2) or (count == 3):
         return True
      else:
         return False
   # A light which is 'off' turns 'on' if exactly
   # 3 neighbors are on, and stays off otherwise.
   elif ((x, y) not in lights_on) and (count == 3):
      return True
   else:
      return False



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read in the file input, determine the size of
   # the light grid, and construct the set of 'on'
   # lights.
   file_input = readFile("input18b.txt")
   max_x = len(file_input[0])
   max_y = len(file_input)
   lights_on = parseInput(file_input)

   # Define the number of steps that will be
   # taken and the max x and max y as a tuple.
   num_steps = 100
   max_coords = (max_x, max_y)

   # Iterate through the given number of steps.
   for t in range(num_steps):
      # Iterate through each light location and
      # generate a new set of 'on' lights.
      next_on = set()
      for y in range(max_y):
         for x in range(max_x):
            if updateLight(x, y, max_coords, lights_on):
               next_on.add((x, y))

      # Reassign the set of 'on' lights for the
      # next round.
      lights_on = next_on
      
   # Display the resulting number of 'on' lights.
   print('After ' + str(num_steps) + ' rounds, lights on = ' + str(len(lights_on)))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
