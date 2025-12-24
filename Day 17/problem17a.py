# The problem input is a list of the sizes of
# containers used for storing eggnog. To fit all
# of the eggnog into the refrigerator, the eggnog
# needs to be stored within the listedcontainers.
# 150 liters of eggnog need to be stored.
#
# Filling all selected containers entirely, how
# many different combinations of containers can
# exactly fit all 150 liters of eggnog?

import time          # For timing the execution
import itertools     # For combination function

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



# Convert the file input (a list of strings) into
# a list of integer values.
def parseInput(values):
   containers = list()
   for line in values:
      containers.append(int(line))

   return containers


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Convert the file input into a list of integer
   # values denoting the container sizes.
   file_input = readFile("input17b.txt")
   containers = parseInput(file_input)

   # The total amount of eggnog that needs to be
   # stored.
   total_eggnog = 150

   # There may be from 1 container up to all of
   # the containers used. Iterate through the
   # possible number of containers.
   good_combos = 0
   for num_containers in range(1, len(containers) + 1):
      # Generate the possible combinations of the
      # given size.
      combos = itertools.combinations(containers, num_containers)

      # For each combination of containers, if
      # they store the correct amount of eggnog,
      # increment the count.
      for c in combos:
         if sum(c) == total_eggnog:
            good_combos += 1

   # Display the total number of combinations that
   # store the correct amount of eggnog.
   print('Possible combinations = ' + str(good_combos))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
