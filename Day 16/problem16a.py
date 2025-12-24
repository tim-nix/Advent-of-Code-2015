# The problem input is data on 500 Aunts named
# "Sue". The goal is to figure out which Aunt Sue
# (which are numbered 1 to 500) matches additional
# input (stored in sue_data.txt). Things missing
# from the data about the 500 Aunt Sues aren't
# zero.  Those values are simply not remembered.
#
# What is the number of the Sue that matches the
# additional input?

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



# Take the list of strings and convert into a list
# of lists containing the file data. Colons and
# commas are removed and the line is split on
# white space.
def parseInput(values):
   sue_list = list()
   for line in values:
      line = line.replace(':', '')
      line = line.replace(',', '')
      sue_list.append(line.split())

   return sue_list


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read in and parse the data on the all of the
   # different Aunt Sues.
   file_input = readFile("input16b.txt")
   sues = parseInput(file_input)

   # Read in, parse the data on the specific
   # Aunt Sue, and add the data to a dictionary.
   file_input = readFile("sue_data.txt")
   correct_data = parseInput(file_input)

   correct_sue = dict()
   for key, value in correct_data:
      correct_sue[key] = value

   # Iterate through all of the Aunt Sues and
   # calculate the number of matches for the entry
   # and the additional data. If there is at least
   # one match, store the number of the Aunt Sue
   # and the total number of matches.
   matches = list()
   for sue in sues:
      count = 0
      for i in range(2, len(sue), 2):
         if sue[i+1] == correct_sue[sue[i]]:
            count += 1

      if count > 0:
         matches.append((sue[1], count))

   # Find the Aunt Sue with the greatest count.
   max_sue = 0
   max_count = 0
   for sue, count in matches:
      if count > max_count:
         max_count = count
         max_sue = sue
         
   
   # Display number of the correct Aunt Sue.
   print('Correct Aunt Sue = ' + str(max_sue))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
