# The problem input provides the distances between
# every pair of locations. Starting and ending at
# any two (different) locations but visiting each
# location exactly once (Hamiltonian path), what
# is the shortest distance that can be traveled to
# achieve this?

import time          # For timing the execution
import itertools     # For generating permutations
import math          # For math.inf

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



# Convert the list of strings into a sorted list
# of cities (labels for vertices) and an adjacency
# matrix representation of the graph.
def parseInput(values):
   # Iterate through the strings and split them
   # into their constituent parts. Make tuples
   # of the two connected cities and their
   # corresponding distance. Also, make a set of
   # the city names.
   vertices = 0
   cities = set()
   data = list()
   for line in values:
      parts = line.split()
      data.append(( parts[0], parts[2], int(parts[4]) ))
      cities.add(parts[0])
      cities.add(parts[2])

   # Convert the set of city names into a sorted
   # list.  Then, iterate through the tuples and
   # create a weighted graph of the city
   # connections and their distances.
   city_list = sorted(list(cities))
   graph = [ [ math.inf for i in range(len(city_list)) ] for j in range(len(city_list)) ]
   for d in data:
      i = city_list.index(d[0])
      j = city_list.index(d[1])
      graph[i][j] = d[2]
      graph[j][i] = d[2]

   # Return the graph (city names are not needed).
   return graph


# Calculate the distance along the given path
# using the weighted graph. Start at the first
# index within the path and add up the distance
# for each edge within the path.
def findDistance(path, graph):
   distance = 0
   current_v = path[0]
   for next_v in path[1:]:
      distance += graph[current_v][next_v]
      current_v = next_v

   return distance


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it into a
   # list of cities and a adjacency matrix graph.   
   file_data = readFile("input9b.txt")
   graph = parseInput(file_data)

   # Generate permutations all of the vertices.
   # Each permutation is a Hamiltonian path
   # through the graph.
   vertices = [ i for i in range(len(graph)) ]
   v_perm = list(itertools.permutations(vertices))

   # Find the distance of the shortest Hamiltonian
   # path.
   min_distance = math.inf
   for p in v_perm:
      distance = findDistance(p, graph)
      if distance < min_distance:
         min_distance = distance
   
   # Display the length of the shortest
   # Hamiltonian path.
   print('Shortest path = ' + str(min_distance))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
