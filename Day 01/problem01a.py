# Santa is trying to deliver presents in a large
# apartment building, but he can't find the right
# floor. The input consists of a single string of
# opening and closing parentheses. An opening
# parenthesis, (, means he should go up one floor,
# and a closing parenthesis, ), means he should go
# down one floor.
#
# Determine to what floor the instructions take
# Santa.

import time     # For timing the execution

# Read in the data file as a single string and
# return the value.
def readFile(filename):
   line = ""
   try:
      with open(filename, "r") as file:
         line = file.readline()
         file.close()
            
   except FileNotFoundError:
      print("Error: File not found!")
   except:
      print("Error: Can't read from file!")

   return line            


# Iterate through the input string. Start on the
# ground floor (floor = 0). If an open parenthesis
# '(' is encountered, increment the floor count.
# If a closing parenthesis ')' is encountered,
# decrement the floor count.
def getFloor(moves):
   floor = 0
   for c in moves:
      if c == "(":
         floor += 1
      elif c == ")":
         floor -= 1

   # Return the floor count.
   return floor
      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   elevator = readFile("input1b.txt")

   # Calculate the correct floor.
   floor = getFloor(elevator)
   
   # Display the results   
   print("Floor = " + str(floor))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
