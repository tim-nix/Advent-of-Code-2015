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


# Calculate the amount of ribbon needed for a set
# of measurements. The ribbon needed is the the
# shortest distance around its sides, or the
# smallest perimeter of any one face. Each present
# also requires a bow made out of ribbon as well
# equal to the cubic feet of volume of the present.
def calcRibbon(measurements):
   l, w, h = measurements

   # Find the shortest distance around the present.
   wrap_ribbon1 = (2 * l) + (2 * w)
   wrap_ribbon2 = (2 * w) + (2 * h)
   wrap_ribbon3 = (2 * h) + (2 * l)
   wrap_ribbon = min(wrap_ribbon1, wrap_ribbon2, wrap_ribbon3)

   # Calculate the volume of the present
   bow_ribbon = l * w * h

   # Return the sum of the shortest distance and
   # the volume.
   return wrap_ribbon + bow_ribbon

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and parse the input.   
   fileInput = readFile("input2b.txt")
   dimensions = parseInput(fileInput)
   
   # Calculate the needed ribbon.
   total_ribbon = 0
   for d in dimensions:
      total_ribbon += calcRibbon(d)
   
   # Display the results.  
   print("Amount of ribbon = " + str(total_ribbon))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
