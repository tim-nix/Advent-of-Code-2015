# Given a list of strings, determine which strings
# are naughty or nice. A nice string is one with
# all of the following properties:
# - It contains at least three vowels (aeiou).
# - It contains at least one letter that appears
#   twice in a row.
# - It does not contain the strings ab, cd, pq,
#   or xy, even if they are part of one of the
#   other requirements.

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

   # Define data for bad stubs and vowels.
   bad_stubs = [ 'ab', 'cd', 'pq', 'xy' ]
   vowels = set([ 'a', 'e', 'i', 'o', 'u' ])

   # Count the number of nice strings.
   nice_count = 0
   for s in strings:
      # Examine string for niceness.
      vowel_count = 0
      double_letter = False
      bad_stub_found = False
      # Look for each bad stub within the string.
      for stub in bad_stubs:
         if stub in s:
            bad_stub_found = True

      # Look for vowels and double letters.
      for i, c in enumerate(s):
         # Vowel found.
         if c in vowels:
            vowel_count += 1

         # Look for double letter.
         if ((i + 1) < len(s)) and (s[i + 1] == c):
               double_letter = True

      # If 3 or more vowels, at least one double
      # letter, and no bad stubs, then increment
      # the count of nice strings.
      if (vowel_count >= 3) and double_letter and not bad_stub_found:
         nice_count += 1
      
   # Display the results.
   print('Nice word count = ' + str(nice_count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
