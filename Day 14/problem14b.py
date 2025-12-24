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
# At the end of each second, Santa awards one
# point to the reindeer currently in the lead. (If
# there are multiple reindeer tied for the lead,
# they each get one point.)
#
# After exactly 2503 seconds, how many points does
# the winning reindeer have?

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

   # Create and initialize a dictionary entry for
   # each reigndeer (distance, remaining stamina,
   # remaining rest). Also create and initialize
   # (set to zero) a dictionary of points for each
   # reindeer
   r_status = dict()
   points = dict()
   for r in reindeer:
      r_status[r[0]] = (0, r[2], 0)
      points[r[0]] = 0

   # For each passing second, update the status
   # and points for each reindeer.
   for d in range(duration):
      #print('time = ' + str(d))
      # Iterate through each reindeer data and
      # update its status.
      for name, speed, stamina, rest in reindeer:
         dist, r_stamina, r_rest = r_status[name]
         # If stamina remains, increase distance
         # and decrease remaining stamina. If
         # stamina is zero, set up to rest.
         if r_stamina > 0:
            dist += speed
            r_stamina -= 1
            if r_stamina == 0:
               r_rest = rest
         # If rest remains, decrease rest. If rest
         # is zero, set up stamina.
         elif r_rest > 0:
            r_rest -= 1
            if r_rest == 0:
               r_stamina = stamina

         # Update reindeer status.
         r_status[name] = (dist, r_stamina, r_rest)

      # Find the distance traveled by leader(s).
      leader = reindeer[0][0]
      for key in r_status:
         if r_status[key][0] > r_status[leader][0]:
            leader = key

      # Award a point for each of the leaders.
      for key in r_status:
         if r_status[key][0] == r_status[leader][0]:
            points[key] += 1

   # Find maximum points won by reindeer.
   max_points = 0
   for key in points:
      if points[key] > max_points:
         max_points = points[key]
   
   # Display the maximum points awarded.
   print('Max points = ' + str(max_points))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
