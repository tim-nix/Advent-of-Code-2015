# The problem input describes all of the possible
# replacements and, at the bottom, the medicine
# molecule that needs to be fabricated. Molecule
# fabrication always begins with just a single
# electron, e, and applying replacements one at a
# time, just like the ones during calibration.
#
# Given the available replacements and the
# medicine molecule in your puzzle input, what is
# the fewest number of steps to go from e to the
# medicine molecule?

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



# Take the file input and convert it to the
# medicine molecule (the last line of the file
# input) and a dictionary of lists for the
# replacement rules. Each key in the dictionary
# can be replaced by on of the values in the
# corresponding list. In this situation, the
# replacement rules are reversed.
def parseInput(values):
   # Pull out the starting molecule.
   start = values[-1]
   end = set()

   # Generate the dictionary of replacements.
   replacements = dict()
   for rule in values[:-2]:
      parts = rule.split()
      if parts[0] == 'e':
         end.add(parts[2])
      else:
         replacements[parts[2]] = parts[0]

   # Return the start and replacement rules.
   return (start, end, replacements)



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Retrieve the data from the input file and
   # convert it into the final medicine molecule
   # string and a dictionary of replacement
   # rules.
   file_input = readFile("input19b.txt")
   start, end, replacements = parseInput(file_input)

   # New molecules need are stored in a list for
   # iteration with 'e' as the starting electron.
   molecules = [ start ]
   new_molecules = set()

   # The goal is to start with the medicine
   # molecule and keep performing replacements
   # until it reverts to one of the smallest
   # elements that map to the starting molecule
   # 'e'. Keep track of how many steps are needed.
   steps = 0
   found = False
   while not found:
      # Check each molecules.
      for m in molecules:
         # Is the molecule one that maps to 'e'?
         # If so, then end.
         if m in end:
            found = True
            break
         
         # Iterate through each character of the
         # current molecule.
         for i in range(len(m)):
            # If a match is found for any
            # replacement rule, then generate a
            # new molecule.
            for key in replacements:
               # Make sure that the remaining
               # length of the starting molecule
               # can support the given key.
               if (i + len(key)) <= len(m):
                  # Calculate the ending index of
                  # the key in the molecule.
                  j = i+len(key)
                  # Is it a match?
                  if m[i:j] == key:
                     # If so, then replace it with
                     # the replacement value.
                     # Concatenate depending on
                     # location of replacement.
                        if i == 0:
                           new_m = replacements[key] + m[j:]
                        elif i == len(m):
                           new_m = m[:i] + replacements[key]
                        else:
                           new_m = m[:i] + replacements[key] + m[j:]

                        new_molecules.add(new_m)

      # Set up for another step. Since the fan-out
      # of the search space increases too much, we
      # limit the next step to the smallest 5
      # molecules.
      steps += 1
      molecules = sorted(list(new_molecules), key=len)[:5]
      
   
   # Display the total number of steps needed to 
   # replicate the medicine molecule.
   print('Number of steps to replicate molecules = ' + str(steps))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
