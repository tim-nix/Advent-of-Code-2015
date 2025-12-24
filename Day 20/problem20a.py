# The problem input is a very large integer value.
# Elves are delivering presents. Each Elf is
# assigned a number and delivers presents to
# houses based on that number:
# - The first Elf (number 1) delivers presents to
#   every house: 1, 2, 3, 4, 5, ....
# - The second Elf (number 2) delivers presents to
#   every second house: 2, 4, 6, 8, 10, ....
# - Elf number 3 delivers presents to every third
#   house: 3, 6, 9, 12, 15, ....
# There are infinitely many Elves, numbered
# starting with 1. Each Elf delivers presents
# equal to ten times his or her number at each
# house.
#
# What is the lowest house number of the house to
# get at least as many presents as the number in
# your puzzle input?

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



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input from the data file and convert
   # it to an integer. This number is the minimum
   # number of presents that need to be delivered.
   file_input = readFile("input20b.txt")[0]
   min_presents = int(file_input)

   # This brute-force algorithm is not efficient.
   # Thus, we do not start at house 1. 
   house = 600000
   found = False
   while not found:
      # Calculate the number of presents for this
      # house.
      presents = 0
      for elf in range(1, house + 1):
         if (house % elf) == 0:
            presents += (elf * 10)

      # If the number of presents is greater than
      # or equal to the amount we are looking for,
      # then end our search.
      if presents >= min_presents:
         found = True
      else:
         house += 1  
      
   # Display the first house to receive at least
   # the minimum number of presents.
   print('House number = ' + str(house))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
