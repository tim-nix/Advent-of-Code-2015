# The problem input contains a variety of things:
# arrays ([1,2,3]), objects ({"a":1, "b":2}),
# numbers, and strings.
#
# Find all of the numbers throughout the document
# and add them together. However, ignore any
# object (and all of its children) which has any
# property with the value "red". Do this only for
# objects ({...}), not arrays ([...]).

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


# Conduct a recursive search of the document. The
# is_object parameter is True if searching through
# an object and False if searching an array.
def parseInput(doc, is_object, i):
   is_red = False

   # Last character is different for an object '}'
   # versus and array ']'
   if is_object:
      closing = '}'
   else:
      closing = ']'

   # Iterate through each character within the
   # program input starting at index i.
   num_start = False
   next_num = ''
   num_sum = 0
   while (i < len(doc)) and (doc[i] != closing):
      # Check to see if the possible start of a
      # negative integer value.
      if (doc[i] == '-') and not num_start:
         num_start = True
         next_num = doc[i]
         i += 1
         
      # Check to see if the start of a positive
      # integer value.
      elif doc[i].isdigit() and not num_start:
         num_start = True
         next_num = doc[i]
         i += 1
         
      # If previous characters indicated the start
      # of an integer value and another digit is
      # encountered, then concatenate it to the
      # number.
      elif doc[i].isdigit() and num_start:
         next_num += doc[i]
         i += 1
         
      # If a non-digit is encountered, but
      # previous digits were seen, then convert
      # convert the number from string to int and
      # add it to the total.
      elif not doc[i].isdigit() and num_start:
         num_start = False
         # Make sure it is not a single dash.
         if (next_num[0] != '-') or (len(next_num) > 1):
            num_sum += int(next_num)
            
         else:
            i += 1

      # Otherwise, a non-digit was encountered but
      # not at the end of a number.
      else:
         # If 'red' is found in an object, then
         # find the end of the object.
         if (doc[i] == 'r'):
            if is_object and (i + 2 < len(doc)) and (doc[i+1:i+3] == 'ed'):
               is_red = True
               # Be sure to find the correct
               # closing curly brace.
               brace_count = 1
               while brace_count > 0:
                  if doc[i] == '{':
                     brace_count += 1
                  elif doc[i] == '}':
                     brace_count -= 1
                  i += 1

               # Be sure to end search on index of
               # correct curly brace.
               i -= 1
            
            # Otherwise, just move to the next
            # letter.
            else:
               i += 1

         # If the start of a new array is found,
         # then recurse.
         elif doc[i] == '[':
            sub_total, i = parseInput(doc, False, i + 1)
            num_sum += sub_total

         # If the start of a new object is found,
         # then recurse.
         elif doc[i] == '{':
            sub_total, i = parseInput(doc, True, i + 1)
            num_sum += sub_total

         # Someother character is encountered so
         # move to the next one.
         elif doc[i] != closing:
            i += 1

   # Handle the case when the array or object
   # ended with a number (no non-digit was seen).
   if num_start:
      num_sum += int(next_num)
   
   # Return the sum (or zero if 'red' occurred)
   # and the updated index.
   if is_red:
      return (0, i + 1)
   else:
      return (num_sum, i + 1)

   
   
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file which contains only the
   # starting number as a string.   
   document = readFile("input12b.txt")[0]

   # Starting with object.
   if document[0] == '{':
      num_sum, index = parseInput(document, True, 1)
   # Starting with array.
   elif document[index] == '[':
      num_sum, index = parseInput(document, False, 1)
   
   # Display the length resulting string.
   print('Sum of all numbers = ' + str(num_sum))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
