# The problem input consists of a string of moves.
# Moves are always exactly one house to the north
# (^), south (v), east (>), or west (<). After
# each move, a present to the house at the new
# location. However, Santa creates a robot version
# of himself, Robo-Santa, to deliver presents with
# him. Santa and Robo-Santa start at the same
# location (delivering two presents to the same
# starting house), then take turns moving based on
# instructions. However, the directions are a
# little off, and Santa and Robo-Santa end up
# visiting some houses more than once.
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



# Given a move (<, ^, >, v), update and return the
# current location.
def makeMove(move, current):
   x, y = current
   if move == '<':
      current = (x - 1, y)
   elif d == '^':
      current = (x, y - 1)
   elif d == '>':
      current = (x + 1, y)
   elif d == 'v':
      current = (x, y + 1)
   else:
      print('Error: invalid character!')

   return current

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   directions = readFile("input3b.txt")
   
   # For each string in directions, iterate 
   # through the string and calculate the number
   # of houses receiving presents, alternating
   # between Santa and Robo-Santa.
   for line in directions:
      # Initialize the start-up
      santa = (0, 0)
      robo = (0, 0)
      turn_santa = True
      total_houses = { santa }
      for d in line:
         # Check to see if it is Santa's turn.
         if turn_santa:
            santa = makeMove(d, santa)
            total_houses.add(santa)
         # Otherwise, it is Robo-Santa's turn.
         else:
            robo = makeMove(d, robo)
            total_houses.add(robo)

         # Update whose turn it is.
         turn_santa = not turn_santa
   
      # Display the results.  
      print("Number of houses = " + str(len(total_houses)))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
