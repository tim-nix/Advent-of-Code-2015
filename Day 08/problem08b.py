# The problem input is a list of double-quoted
# string literals, one on each line. The only
# escape sequences used are \\ (which represents a
# single backslash), \" (which represents a lone
# double-quote character), and \x plus two
# hexadecimal characters (which represents a
# single character with that ASCII code).
#
# Encode each code representation as a new string
# in which every backslash, double-quoteand find the number of characters of the new
# encoded representation, including the
# surrounding double quotes.
#
# Find the total number of characters to represent
# the newly encoded strings minus the number of
# characters of code in each original string
# literal.

import time     # For timing the execution

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
   
   return lines



# Convert the string representation of each
# instruction to list of characters.
def parseInput(values):
   strings = list()
   for line in values:
      # Append the string as a list of characters
      # without the leading and training double-
      # quotes.
      strings.append(list(line))

   # Return the list of lists of characters.
   return strings

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   file_data = readFile("input8b.txt")
   strings = parseInput(file_data)

   # Iterate through the list of lists of
   # characters and keep track of the total number
   # of literal characters and the total number of
   # character values represented within all
   # strings. 
   literal_count = 0
   total_count = 0
   for string in strings:
      # Count the number of values within the list
      # plus the (implied) leading and trailing
      # double-quotes.
      l_count = (len(string) + 2)

      # Count the number of values within the list.
      t_count = len(string)

      # Iterate through the list of characters and
      # add any implied escape characters to the
      # count of literal characters.
      c_i = 0
      while c_i < len(string):
         # Check for single backslash.
         if (string[c_i] == '\\'):
            escape = False
            l_count += 1

         # Check for double-quote.
         elif (string[c_i] == '"'):
            l_count += 1

         # Increment the index of the list
         c_i += 1

      # Add the number of character values for the
      # literal count and the character count to
      # their respective totals
      literal_count += l_count
      total_count += t_count

   # Display the results of the difference.
   print('Character count difference = ' + str(literal_count - total_count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
