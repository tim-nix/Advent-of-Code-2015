# The problem input contains a variety of things:
# arrays ([1,2,3]), objects ({"a":1, "b":2}),
# numbers, and strings.
#
# Find all of the numbers throughout the document
# and add them together.

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

   
   
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file which contains only the
   # starting number as a string.   
   file_input = readFile("input12b.txt")[0]

   # Iterate through each character within the
   # program input.
   num_start = False
   next_num = ''
   num_sum = 0
   for char in file_input:
      # Check to see if the possible start of a
      # negative integer value.
      if (char == '-') and not num_start:
         num_start = True
         next_num = char
      # Check to see if the start of a positive
      # integer value.
      elif char.isdigit() and not num_start:
         num_start = True
         next_num = char
      # If previous characters indicated the start
      # of an integer value and another digit is
      # encountered, then concatenate it to the
      # number.
      elif char.isdigit() and num_start:
         next_num += char
      # If a non-digit is encountered, but
      # previous digits were seen, then convert
      # convert the number from string to int and
      # add it to the total.
      elif not char.isdigit() and num_start:
         num_start = False
         # Make sure it is not a single dash.
         if (next_num[0] != '-') or (len(next_num) > 1):
            num_sum += int(next_num)

   # Handle the case when the string ended with a
   # number (no non-digit was seen).
   if num_start:
      num_sum += int(next_num)

   # Display the length resulting string.
   print('Sum of all numbers = ' + str(num_sum))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
