# The problem input is a single number (as a
# string). Then, sequences are generated
# iteratively, using the previous value as input
# for the next step. For each step, take the
# previous value, and replace each run of digits
# (like 111) with the number of digits (3)
# followed by the digit itself (1).
#
# Starting with the digits in your puzzle input,
# apply this process 50 times. What is the length
# of the result?

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



# Parse Conway's elements into a dictionary of
# tuples
def parseInput(values):
   elements = dict()
   for line in values:
      parts = line.split()
      elements[parts[0]] = (parts[1], parts[2])

   return elements
   

if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file which contains only the
   # starting number as a string.   
   sequence = readFile("input10b.txt")[0]

   # Read the data file storing Conway's elements.
   element_data = readFile("conways_elements.txt")
   elements = parseInput(element_data)

   # Specified to iterate 50 times.
   max_replacement = 50

   # Find the key in the dictionary associated
   # with the starting string (sequence).
   start_element = ''
   for key in elements:
      if elements[key][0] == sequence:
         start_element = key
         break

   # Iterate the specified number of times and
   # expand the sequence using the elements data
   # stored in the dictionary. 
   current = [ start_element ]
   for _ in range(max_replacement):
      next_sequence = list()
      # Replace the current element with its
      # expansion given in the dictionary.
      for c in current:
         next_sequence += elements[c][1].split('.')

      # The new sequence (as elements) is ready
      # for another round.
      current = next_sequence

   # Iterate through the final sequence and
   # calculate the total characters within the
   # sequence by looking up the element sequence
   # in the dictionary.
   count = 0
   for c in current:
      count += len(elements[c][0])
   
   # Display the length resulting string.
   print('String length = ' + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

