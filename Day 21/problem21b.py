# In this game, the player and the enemy take
# turns attacking. The boss's actual stats are in
# your puzzle input. The player always goes first.
# Each attack reduces the opponent's hit points by
# at least 1. The first character at or below 0
# hit points loses. Damage dealt by an attacker
# each turn is equal to the attacker's damage
# score minus the defender's armor score. An
# attacker always does at least 1 damage. Your
# damage score and armor score both start at zero.
# They can be increased by buying items in
# exchange for gold. You start with no items and
# have as much gold as you need. Your total damage
# or armor is equal to the sum of those stats from
# all of your items. You have 100 hit points.
#
# Turns out the shopkeeper is working with the
# boss, and can persuade you to buy whatever items
# he wants.
#
# You must buy exactly one weapon. Armor is
# optional, but you can't use more than one. You
# can buy 0-2 rings (at most one for each hand).
# You must use any items you buy.
#
# What is the most amount of gold you can spend
# and still lose the fight?

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



# Convert the file input of the enemy's attributes
# into a list of integers consisting of the
# (hp, damage, armor).
def parseAttributes(values):
   attributes = list()
   # Original data contains one string per
   # attribute.
   for line in values:
      parts = line.split()
      attributes.append(int(parts[-1]))

   # Return converted attributes.
   return attributes



# Convert the file input of the shop data. The
# file data is organized as all weapons are listed
# first, all armor is listed next, and all rings
# are listed last. Each group has a heading and an
# empty string splits each group. Each item is
# split on whitespace into label, cost, damage
# modifier, and armor modifier. The label is
# ignored. Three lists are made; one for each
# class.
def parseShop(values):
   weapons = list()
   armor = list()
   rings = list()
   item_class = ''
   for line in values:
      parts = line.split()
      # Ignore the empty list.
      if len(parts) == 0:
         continue
      # Entering the 'weapons' portion.
      elif parts[0] == 'Weapons:':
         item_class = 'weapons'
      # Entering the 'armor' portion.
      elif parts[0] == 'Armor:':
         item_class = 'armor'
      # Entering the 'rings' portion.
      elif parts[0] == 'Rings:':
         item_class = 'rings'
      # If 'weapons' portion, then add to weapons.
      elif item_class == 'weapons':
         weapons.append((int(parts[1]), int(parts[2]), int(parts[3])))
      # If 'armor' portion, then add to armor.
      elif item_class == 'armor':
         armor.append((int(parts[1]), int(parts[2]), int(parts[3])))
      # If 'rings' portion, then add to rings.
      elif item_class == 'rings':
         rings.append((int(parts[2]), int(parts[3]), int(parts[4])))

   # Return the three lists.
   return (weapons, armor, rings)



# Given the enemy attributes and the player
# attributes, determine who the winner will be.
def isWin(enemy, player):
   e_hp, e_damage, e_armor = enemy
   p_hp, p_damage, p_armor = player

   # Calculate the enemy's damage per round.
   e_dpr = e_damage - p_armor
   if e_dpr <= 0:
      e_dpr = 1

   # Calculate the player's damage per round.
   p_dpr = p_damage - e_armor
   if p_dpr <= 0:
      p_dpr = 1

   # Determine how many rounds needed to kill the
   # enemy.
   e_rounds = e_hp // p_dpr
   if e_hp % p_dpr != 0:
      e_rounds += 1

   # Determine how many rounds needed to kill the
   # player.
   p_rounds = p_hp // e_dpr
   if p_hp % e_dpr != 0:
      p_rounds += 1

   # Return whether or not it takes longer to kill
   # the player or not.
   return p_rounds >= e_rounds



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it to the
   # attributes of the enemy (hp, damage, armor).
   file_input = readFile("input21b.txt")
   e_attr = parseAttributes(file_input)

   # Read the shop data file and convert it to
   # by class to (cost, damage, armour).
   file_input = readFile("shop_items.txt")
   weapons, armor, rings = parseShop(file_input)

   # Initialize the player's hp and set the
   # maximum cost (to zero).
   p_hp = 100
   max_cost = 0

   # You must buy exactly one weapon; no dual-
   # wielding. Armor is optional, but you can't
   # use more than one. You can buy 0-2 rings (at
   # most one for each hand).

   # Iterate through the weapons choices.
   for w in weapons:
      # With no armor and no rings.
      p_damage = w[1]
      cost = w[0]
      if not isWin(e_attr, (p_hp, p_damage, 0)):
         if cost > max_cost:
            min_cost = cost

      # Iterate through the armor choices.
      for a in armor:
         # With armor and no rings.
         cost = w[0] + a[0]
         p_armor = a[2]
         if not isWin(e_attr, (p_hp, p_damage, p_armor)):
            if cost > max_cost:
               max_cost = cost

         # Iterate through the first ring choices.
         for i in range(len(rings)):
            # With no armor and one ring.
            cost = w[0] + rings[i][0]
            p_damage = w[1] + rings[i][1]
            p_armor = rings[i][2]
            if not isWin(e_attr, (p_hp, p_damage, p_armor)):
               if cost > max_cost:
                  max_cost = cost

            # With armor and one ring.
            cost = w[0] + a[0] + rings[i][0]
            p_damage = w[1] + rings[i][1]
            p_armor = a[2] + rings[i][2]
            if not isWin(e_attr, (p_hp, p_damage, p_armor)):
               if cost > max_cost:
                  max_cost = cost

            # Iterate through the second ring
            # choices.
            for j in range(i + 1, len(rings)):
               # With no armor and two rings.
               cost = w[0] + rings[i][0] + rings[j][0]
               p_damage = w[1] + rings[i][1] + rings[j][1]
               p_armor = rings[i][2] + rings[j][2]
               if not isWin(e_attr, (p_hp, p_damage, p_armor)):
                  if cost > max_cost:
                     max_cost = cost

               # With armor and two rings.
               cost = w[0] + a[0] + rings[i][0] + rings[j][0]
               p_damage = w[1] + rings[i][1] + rings[j][1]
               p_armor = a[2] + rings[i][2] + rings[j][2]
               if not isWin(e_attr, (p_hp, p_damage, p_armor)):
                  if cost > max_cost:
                     max_cost = cost

   # Display the maximum cost of a loss.
   print('Maximum cost of a loss = ' + str(max_cost))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
