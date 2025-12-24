# Given a list of strings, determine which strings
# are naughty or nice. A nice string is one with
# all of the following properties:
# - It contains a pair of any two letters that
#   appears at least twice in the string without
#   overlapping.
# - It contains at least one letter which repeats
#   with exactly one letter between them.

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


      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   strings = readFile("input5b.txt")

   # Count the number of nice strings.
   nice_count = 0
   for s in strings:
      # Examine string to see if it contains a
      # pair of any two letters that appears at
      # least twice in the string without
      # overlapping.
      repeat_pair = False
      repeat_letter = False
      for i in range(len(s) - 2):
         for j in range(i + 2, len(s)):
            if s[i:i + 2] == s[j:j + 2]:
               repeat_pair = True

         # Examine string to see if it contains
         # at least one letter which repeats with
         # exactly one letter between them. 
         if s[i] == s[i + 2]:
            repeat_letter = True

      # Increment nice count.
      if repeat_pair and repeat_letter:
         nice_count += 1
      
   # Display the results.
   print('Nice word count = ' + str(nice_count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
