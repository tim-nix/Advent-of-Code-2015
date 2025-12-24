# Santa needs help mining some AdventCoins. To do
# this, he needs to find MD5 hashes which, in
# hexadecimal, start with at least five zeroes.
# The input to the MD5 hash is some secret key
# (the puzzle input) followed by a number in
# decimal. To mine AdventCoins, find the lowest
# positive number (no leading zeroes: 1, 2, 3,
# ...) that produces such a hash.

import time     # For timing the execution
import hashlib  # For calculating the hash value

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
   
   return lines[0]

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   seed = readFile("input4b.txt")

   # Maintain a decimal count. Append this value,
   # as a string, to the seed value (also as a
   # string). Calculate the MD5 hash and check it.
   found = False
   count = 0
   while not found:
      # Form the string to hash.
      hex_count = str(count)
      byte_data = (seed + hex_count).encode('utf-8')

      # Hash the string.
      md5 = hashlib.md5()
      md5.update(byte_data)
      hex_string = md5.hexdigest()

      # If the hash starts with five zeros, done.
      if hex_string[:5] == '00000':
         found = True
      # Otherwise, increment the count and loop.
      else:
         count += 1
      
   # Display the results.
   print('Hash value = ' + hex_string)
   print('Count = ' + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
