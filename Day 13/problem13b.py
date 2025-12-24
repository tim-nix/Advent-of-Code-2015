# The problem input is a list of everyone invited
# and the amount their happiness would increase or
# decrease if they were to find themselves sitting
# next to each other person. All guests are seated
# at a circular table that will be just big enough
# to fit everyone comfortably, and so each person
# will have exactly two neighbors. Add myself to
# the seating arrangement.
#
# What is the total change in happiness for the
# optimal seating arrangement of the actual guest
# list?

import time          # For timing the execution
import itertools     # For generating permutations

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



# Convert the program input into a dictionary of
# values such that, for each pair of guests as the
# key, the value is the change in happiness should
# those guests sit by each other. Also generated
# is a list of all guests.
def parseInput(values):
   happiness = dict()
   guests = set()

   # Iterate through each line of input.
   for line in values:
      # Remove the period at the end of the line.
      line = line.replace('.', '')
      parts = line.split()
      # Convert the value into an integer
      # (positive if 'gain' and negative if
      # 'loss'.
      if parts[2] == 'gain':
         value = int(parts[3])
      else:
         value = - int(parts[3])

      # Add to dictionary
      happiness[(parts[0], parts[-1])] = value
      # Add to set of guests.
      if parts[0] not in guests:
         guests.add(parts[0])

   # Return as tuple.
   return (list(guests), happiness)



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it into a
   # list of guests and a dictionary of happiness
   # values.   
   file_input = readFile("input13b.txt")
   guests, happiness = parseInput(file_input)

   # Add myself to the dictionary with a happiness
   # change of zero for each guests.
   for g in guests:
      happiness[('myself', g)] = 0
      happiness[(g, 'myself')] = 0

   # Add myself to the list of guests.
   guests.append('myself')

   # Generate all permutations of guests.
   seating = list(itertools.permutations(guests))

   # Iterate through all permutations.
   max_happiness = 0
   for s in seating:
      # Add the guest at the beginning to the end.
      current = list(s)
      current.append(s[0])

      # Calculate the change in happiness from
      # this seating.
      this_happiness = 0
      for i in range(len(current) - 1):
         this_happiness += happiness[(current[i], current[i+1])]
         this_happiness += happiness[(current[i+1], current[i])]
         # If this is the best change, update it.
         if this_happiness > max_happiness:
            max_happiness = this_happiness
   
   # Display the highest change in happiness.
   print('Max happiness = ' + str(max_happiness))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
