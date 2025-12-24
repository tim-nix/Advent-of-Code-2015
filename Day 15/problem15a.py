# The problem input is a recipe of ingredients and
# the associated properties of each ingredient.
# The recipe leaves room for exactly 100 teaspoons
# of ingredients. The properties per teaspoon of
# each ingredient are, as follows:
# - capacity
# - durability
# - flavor
# - texture
# - calories (ignored in this problem)
# The total score of a cookie can be found by
# adding up each of the properties (negative
# totals become 0) and then multiplying together
# everything except calories.
#
# What is the total score of the highest-scoring
# cookie that can be made?

import time          # For timing the execution
import itertools     # For combinations.

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



# Convert the recipe (as string) into a tuple of
# integers for each of the properties: capacity,
# durability, flavor, and texture. Ignore
# calories.
def parseInput(values):
   recipe = list()
   for line in values:
      # Get rid of commas in string.
      line = line.replace(',', '')
      parts = line.split()
      # Property values are found at even indexes
      # starting with 2.
      recipe.append([ int(parts[i]) for i in range(2, len(parts) - 1, 2) ])

   return recipe



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read in the list and properties of the
   # ingredients and convert the properties to
   # integers.
   file_input = readFile("input15b.txt")
   recipe = parseInput(file_input)

   # Ingredients should total this given value.
   total_teaspoons = 100

   # Generate possible combinations that total to
   # the given amount.
   numbers = list(range(101))
   combinations = itertools.product(numbers, repeat=len(recipe))

   # Check each combination
   good_combos = list()
   for combo in combinations:
      if sum(combo) == total_teaspoons:
         good_combos.append(combo)

   # Calculate the score for each combo and find
   # the best overall score.
   best_score = 0
   for combo in good_combos:
      total_score = 1
      # Iterate through each property.
      for j in range(len(recipe[0])):
         # Calculate score for property.
         score = 0
         for i in range(len(combo)):
            score += combo[i] * recipe[i][j]

         # Negative scores revert to zero.
         if score < 0:
            score = 0
            
         # Total score is the product of each
         # property score.
         total_score *= score

      # Retain the highest total score found.
      if total_score > best_score:
         best_score = total_score
   
   # Display highest total score.
   print('Best score = ' + str(best_score))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
