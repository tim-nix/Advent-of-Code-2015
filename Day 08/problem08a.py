# The problem input is a list of double-quoted
# string literals, one on each line. The only
# escape sequences used are \\ (which represents a
# single backslash), \" (which represents a lone
# double-quote character), and \x plus two
# hexadecimal characters (which represents a
# single character with that ASCII code).
#
# Disregarding the whitespace in the file, what is
# the number of characters of code for string
# literals minus the number of characters in
# memory for the values of the strings in total
# for the entire file?

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
      strings.append(list(line)[1:-1])

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
      # Add the total number of values within the
      # list plus the (removed) leading and
      # trailing double-quotes.
      literal_count += (len(string) + 2)

      # Iterate through the list of characters and
      # count the number of character values in
      # the string.
      count = 0
      escape = False
      c_i = 0
      while c_i < len(string):
         # Check for escape character
         if (string[c_i] == '\\') and not escape:
            escape = True
         # Check for an escaped single backslash.
         elif (string[c_i] == '\\') and escape:
            escape = False
            count += 1
         # Check for an escaped double-quote.
         elif (string[c_i] == '"') and escape:
            escape = False
            count += 1
         # Check for an escaped, two-digit
         # hexadecimal number.
         elif (string[c_i] == 'x') and escape:
            escape = False
            count += 1
            c_i += 2     # Two-digit number
         # Otherwise, it should be a single
         # character.
         else:
            count += 1

         # Increment the index of the list
         c_i += 1

      # Add the number of character values for the
      # string to the total count.
      total_count += count

   # Display the results of the difference.
   print('Character count difference = ' + str(literal_count - total_count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
