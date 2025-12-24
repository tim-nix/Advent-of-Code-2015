# Santa is trying to deliver presents in a large
# apartment building, but he can't find the right
# floor. The input consists of a single string of
# opening and closing parentheses. An opening
# parenthesis, (, means he should go up one floor,
# and a closing parenthesis, ), means he should go
# down one floor.
#
# Determine the position of the character that
# causes Santa to first enter the basement (the
# first character in the string is at position
# one).

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

def getFloor(moves):
   floor = 0
   position = 1
   for c in moves:
      if c == "(":
         floor += 1
      elif c == ")":
         floor -= 1
      if floor < 0:
         return position
      position += 1

   return position
      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   elevator = readFile("input1b.txt")

   # Calculate the correct floor.
   position = getFloor(elevator)
   
   # Display the results   
   print("Position = " + str(position))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
