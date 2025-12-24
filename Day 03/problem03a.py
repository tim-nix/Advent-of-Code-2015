# The problem input consists of a string of moves.
# Moves are always exactly one house to the north
# (^), south (v), east (>), or west (<). After
# each move, a present to the house at the new
# location. However, the directions are a little
# off, and Santa ends up visiting some houses more
# than once.
#
# How many houses receive at least one present?

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
   directions = readFile("input3b.txt")
   
   # For each string in directions, iterate 
   # through the string and calculate the number
   # of houses receiving presents.
   for line in directions:
      current = (0, 0)
      total_houses = { current }
      for d in line:
         x, y = current
         if d == '<':
            current = (x - 1, y)
         elif d == '^':
            current = (x, y - 1)
         elif d == '>':
            current = (x + 1, y)
         elif d == 'v':
            current = (x, y + 1)
         else:
            print('Error: invalid character!')
            break
         total_houses.add(current)
   
      # Display the results.  
      print("Number of houses = " + str(len(total_houses)))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
