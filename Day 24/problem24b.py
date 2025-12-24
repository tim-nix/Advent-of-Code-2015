# The problem input is a list of weights for
# packages. The packages need to be split into
# FOUR groups of exactly the same weight. The
# first group needs as few packages as possible.
# It doesn't matter how many packages are in 
# either of the other three groups, so long as all
# of the groups weigh the same. Furthermore, the
# first group needs be the one of that size with
# the smallest quantum entanglement (qe). The qe
# of a group of packages is the product of their
# weights. Only consider quantum entanglement if
# the first group has the fewest possible number
# of packages in it and all groups weigh the same
# amount.
#
# What is the quantum entanglement of the first
# group of packages in the ideal configuration?

import time          # For timing the execution
import itertools     # For generating permutations
import math          # For math.inf and math.prod()


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



# Convert the file input (strings) into a list of
# integers.
def parseInput(values):
   weights = list()
   for line in values:
      weights.append(int(line))

   # Return the list of weights.
   return weights


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it to a list
   # of weights.
   file_input = readFile("input24b.txt")
   weights = parseInput(file_input)

   # Calculate the total weight and the weight for
   # each of the compartments (1/4 in each).
   total_weight = sum(weights)
   third = total_weight // 4

   # Initialize the tracking of minimum presents
   # and associated minimum qe.
   min_presents = len(weights) // 4
   min_qe = math.inf

   # Need to generate combinations of the correct
   # size. Compartment 1 contains the smallest
   # group which can't be larger than 1/4 of the
   # number of weights. Start there and reduce
   # until no new minimums are found.
   found = False
   while not found:
      found = True

      # Generate all possible load plans of the
      # given size (min_presents).
      load_plans = itertools.combinations(weights, min_presents)

      # Iterate through the permutations. Find the
      # lowest quantum entanglement among the
      # first group with the smallest number of
      # presents.
      for load in load_plans:
         weight = 0
         index = 0
         compartment = list()
         while (weight < third) and (len(compartment) < min_presents):
            compartment.append(load[index])
            weight += load[index]
            index += 1

         # Only consider a compartment load plan
         # that is the correct weight.
         if weight == third:
            if len(compartment) < min_presents:
               # New min_presents, so set up for
               # another round of combinations.
               found = False
               min_presents = len(compartment)
               min_qe = math.prod(compartment)

            # If load plan is the same minimum
            # size, compare the qe with min_qe.
            elif len(compartment) == min_presents:
               qe = math.prod(compartment)
               if qe < min_qe:
                  min_qe = qe
         
   # Display the quantum entanglement of the first
   # group of packages in the ideal configuration
   print('Best quantum entanglement = ' + str(min_qe))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
