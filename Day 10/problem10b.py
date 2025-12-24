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
   return lines[0]


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file which contains only the
   # starting number as a string.   
   sequence = readFile("input10b.txt")

   # Specified to iterate 50 times.
   max_replacement = 50

   for c in range(max_replacement):
      #print(str(c) + "--- %s seconds ---" % (time.time() - start_time))
      # Iterate through the current string.
      # For each new digit encountered, count the
      # number of times that digit occurs
      # sequentially.
      next_string = ''
      i = 0
      while i < len(sequence):
         current_d = sequence[i]
         count = 0
         while (i < len(sequence)) and (sequence[i] == current_d):
            count += 1
            i += 1

         # Concatenate the number of occurrences
         # followed by the digit.
         next_string += str(count)
         next_string += current_d

      # Update the old sequence with the new
      # sequence and repeat the specified number
      # of times.
      sequence = next_string
   
   # Display the length resulting string.
   print('String length = ' + str(len(sequence)))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

