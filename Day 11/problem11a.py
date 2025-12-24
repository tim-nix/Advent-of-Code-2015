# We need to find the next possible password.
# Passwords must be exactly eight lowercase
# letters, so the new password is found by
# incrementing the old password string repeatedly
# until it is valid. Incrementing is just like
# counting with numbers: xx, xy, xz, ya, yb, and
# so on. Increase the rightmost letter one step;
# if it was z, it wraps around to a, and repeat
# with the next letter to the left until one
# doesn't wrap around. Password requirements:
# - Passwords must include one increasing straight
#   of at least three letters, like abc, bcd, cde,
#   and so on, up to xyz. They cannot skip
#   letters; abd doesn't count.
# - Passwords may not contain the letters i, o,
#   or l, as these letters can be mistaken for
#   other characters and are therefore confusing.
# - Passwords must contain at least two different,
#   non-overlapping pairs of letters, like aa, bb,
#   or zz.
#
# Given the current password (your puzzle input),
# what should his next password be?

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



# Check the password to see if it meets all of the
# requirements.
def checkPassword(password):
   # Passwords may not contain the letters i, o,
   # or l.
   if len(set(list(password)).intersection({'i', 'o', 'l'})) > 0:
      return False

   # Passwords must contain at least two different,
   # non-overlapping pairs of letters, like aa, bb,
   # or zz.
   double_count = 0
   i = 0
   while i < (len(password) - 1):
      if password[i] == password[i + 1]:
         double_count += 1
         i += 2
      else:
         i += 1
      
   if double_count < 2:
      return False

   # Passwords must include one increasing straight
   # of at least three letters, like abc, bcd, cde,
   # and so on, up to xyz. They cannot skip
   # letters; abd doesn't count.
   for j in range(len(password) - 2):
      if (ord(password[j]) + 2) == (ord(password[j+1]) + 1) == (ord(password[j+2])):
         return True   

   return False

   
   
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file which contains only the
   # starting number as a string.   
   passwords = readFile("input11b.txt")
   
   for password in passwords:
      found = False
      while not found:
         # Generate the next incremented password.
         new_password = ''
         carry = 1
         # Iterate through the characters in
         # reverse order.
         for char in password[::-1]:
            next_char = ord(char) + carry
            if next_char > ord('z'):
               new_password += 'a'
               carry = 1
            else:
               new_password += chr(next_char)
               carry = 0

         # Reverse the incremented password back
         # and check if for legality.
         password = new_password[::-1]
         found = checkPassword(password)

      # Display the length resulting string.
      print('New password = ' + str(password))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
