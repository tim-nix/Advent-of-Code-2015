# The problem input consists of information about
# the movement capabilities of the reindeer.
# Reindeer can only either be flying (always at
# their top speed) or resting (not moving at all),
# and always spend whole seconds in either state.
# For example, suppose you have the following
# Reindeer:
# - Comet can fly 14 km/s for 10 seconds, but then
#   must rest for 127 seconds.
# - Dancer can fly 16 km/s for 11 seconds, but
#   then must rest for 162 seconds.
#
# Given the descriptions of each reindeer (in the
# puzzle input), after exactly 2503 seconds, what
# distance has the winning reindeer traveled?

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



# Convert the string input for each reindeer into
# a tuple of the reindeer's name, speed, stamina
# (how long they can travel at their speed), and
# how long they then need to rest. Tuples are
# stored in a list and returned.
def parseInput(values):
   reindeer = list()

   # Iterate through each string of text, break it
   # into separate words and extract needed data.
   for line in values:
      parts   = line.split()
      # Speed, stamina, and rest are all converted
      # to integers.
      speed   = int(parts[3])
      stamina = int(parts[6])
      rest    = int(parts[13])

      # Create tuple and store it in the list.
      reindeer.append((parts[0], speed, stamina, rest))

   # Return the resulting list.
   return reindeer



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it into a
   # list reindeer and their associated 
   # properties.   
   file_input = readFile("input14b.txt")
   reindeer = parseInput(file_input)

   # The duration of the race is specified.
   duration = 2503

   # Iterate through each reindeer data and
   # determine how far the reindeer travels.
   max_distance = 0
   for _, speed, stamina, rest in reindeer:
      r_time = duration
      # Calculate the distance traveled in each
      # burst of speed and the time remaining
      # after each burst and each rest.
      distance = 0
      while r_time > 0:
         # If enough time is available, then run
         # for the full stamina duration.
         if r_time >= stamina:
            distance += (speed * stamina)
            r_time -= stamina
         # Otherwise, make sure the last duration
         # of stamina is truncated if time runs
         # out.
         else:
            distance += (speed * r_time)
            r_time -= r_time

         # Also subtract the time to rest.
         r_time -= rest

      # Keep track of the most distance covered.
      if distance > max_distance:
         max_distance = distance
            
   
   # Display the distance traveled by a reindeer.
   print('Max distance = ' + str(max_distance))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
