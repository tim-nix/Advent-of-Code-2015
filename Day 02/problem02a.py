# The problem input consists of a list of the
# dimensions (length l, width w, and height h)
# of each present. All numbers in the list are
# in feet. For each set of dimensions, calculate
# the required wrapping paper for each gift by
# finding the surface area of the box, which is
# 2*l*w + 2*w*h + 2*h*l and adding to that the
# extra paper needed for each present; that is,
# the area of the smallest side.  
#
# How many total square feet of wrapping paper
# should be ordered?

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

# Convert the list of dimensions (as a list of
# strings) into a list of tuples containing
# integers.
def parseInput(values):
   dimensions = []
   for line in values:
      dimensions.append([ int(i) for i in line.split('x') ])

   return dimensions


# Calculate the amount of paper needed for a set
# of measurements. The paper needed is the surface
# area of the present plus the extra paper needed;
# the area of the smallest side.
def calcPaper(measurements):
   l, w, h = measurements

   # Calculate the surface area.
   surface_area = (2 * l * w) + (2 * w * h) + (2 * h * l)

   # Find the area of the smallest side.
   area1 = l * w
   area2 = w * h
   area3 = h * l
   extra = min(area1, area2, area3)

   # Return the sum of the surface area and extra.
   return surface_area + extra

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and parse the input.   
   fileInput = readFile("input2b.txt")
   dimensions = parseInput(fileInput)
   
   # Calculate the needed wrapping paper.
   total_paper = 0
   for d in dimensions:
      total_paper += calcPaper(d)
   
   # Display the results.  
   print("Amount of paper = " + str(total_paper))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
