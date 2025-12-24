# In this game, the player and the enemy take
# turns attacking. The boss's actual stats are in
# your puzzle input. The player always goes first.
# Now, however, you don't get any equipment;
# instead, you must choose one of your spells to
# cast. The first character at or below 0 hit
# points loses. Since you're a wizard, you don't
# get to wear armor, and you can't attack
# normally. However, since you do magic damage,
# your opponent's armor is ignored, and so the
# boss effectively has zero armor as well. If
# armor (from a spell, in this case) would reduce
# damage below 1, it becomes 1 instead - that is,
# the boss' attacks always deal at least 1 damage.
# Spells cost mana; you start with 500 mana, but
# have no maximum limit. You must have enough mana
# to cast a spell, and its cost is immediately
# deducted when you cast it. Your spells are Magic
# Missile, Drain, Shield, Poison, and Recharge.
# - Magic Missile costs 53 mana. It instantly does
#   4 damage.
# - Drain costs 73 mana. It instantly does 2
#   damage and heals you for 2 hit points.
# - Shield costs 113 mana. It starts an effect that
#   lasts for 6 turns. While it is active, your
#   armor is increased by 7.
# - Poison costs 173 mana. It starts an effect
#   that lasts for 6 turns. At the start of each
#   turn while it is active, it deals the boss 3
#   damage.
# - Recharge costs 229 mana. It starts an effect
#   that lasts for 5 turns. At the start of each
#   turn while it is active, it gives you 101 new
#   mana.
# On this run through the game, the difficulty is
# set to HARD. At the start of each player turn
# (before any other effects apply), you lose 1 hit
# point. If this brings you to or below 0 hit
# points, you lose.
#
# What is the least amount of mana you can spend
# and still win the fight?

import time          # For timing the execution

# Global constants and variables
spells = ( 'magic missile', 'drain', 'shield', 'poison', 'recharge' )
min_mana = 10000



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
# into a list of integers consisting of the hp and
# damage.
def parseAttributes(values):
   attributes = list()
   # Original data contains one string per
   # attribute.
   for line in values:
      parts = line.split()
      attributes.append(int(parts[-1]))

   # Return converted attributes.
   return attributes



#
def playGame(game_status):
   # Game status: e_hp, e_damage, p_hp, p_mana,
   # shield, poison, recharge, mana_cost)

   global min_mana
   
   # Iterate (cast) through each spell.
   for spell in spells:
      # Extract game state.
      e_hp = game_status[0]
      e_damage = game_status[1]
      p_hp = game_status[2] - 1  # Lose 1 hp
      p_mana = game_status[3]
      shield = game_status[4]
      poison = game_status[5]
      recharge = game_status[6]
      mana_cost = game_status[7]

      # If the hp deduction results in death, then
      # no need to pursue this level.
      if p_hp <= 0:
         return

      # To prevent an unending battle, end if mana
      # cost is too high.
      if mana_cost > min_mana:
         continue

      # Player's Turn:

      # Apply active spells.
      if shield > 0:
         p_armor = 7
         shield -= 1
      else:
         p_armor = 0

      if poison > 0:
         e_hp -= 3
         poison -= 1

      if recharge > 0:
         p_mana += 101
         recharge -= 1

      # Check to see if player won.
      if e_hp <= 0:
         if mana_cost < min_mana:
            min_mana = mana_cost
         continue
      
      # Cast magic missile.
      if (spell == 'magic missile') and (p_mana >= 53):
         p_mana -= 53
         mana_cost += 53
         e_hp -= 4

      # Cast drain.
      elif (spell == 'drain') and (p_mana >= 73):
         p_mana -= 73
         mana_cost += 73
         e_hp -= 2
         p_hp += 2

      # Cast shield.
      elif (spell == 'shield') and (shield == 0) and (p_mana >= 113):
         p_mana -= 113
         mana_cost += 113
         shield = 6

      # Cast poison.
      elif (spell == 'poison') and (poison == 0) and (p_mana >= 173):
         p_mana -= 173
         mana_cost += 173
         poison = 6

      # Cast recharge.
      elif (spell == 'recharge') and (recharge == 0) and (p_mana >= 229):
         p_mana -= 229
         mana_cost += 229
         recharge = 5

      # If no spell is cast, move to the next COA.
      else:
         continue

      # Check to see if player won.
      if e_hp <= 0:
         if mana_cost < min_mana:
            min_mana = mana_cost
            continue
         
      # Boss's turn

      # Apply active spells.
      if shield > 0:
         p_armor = 7
         shield -= 1
      else:
         p_armor = 0

      if poison > 0:
         e_hp -= 3
         poison -= 1

      if recharge > 0:
         p_mana += 101
         recharge -= 1

      # Check to see if player won.
      if e_hp <= 0:
         if mana_cost < min_mana:
            min_mana = mana_cost
         continue
         
      # Calculate Boss's damage.
      damage = e_damage - p_armor
      if damage <= 0:
         damage = 1

      # Apply Boss's damage.
      p_hp -= damage

      # End game if boss wins. Otherwise, recurse.
      if p_hp > 0:
         playGame((e_hp, e_damage, p_hp, p_mana, shield, poison, recharge, mana_cost))




if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it to the
   # attributes of the enemy (hp, damage).
   file_input = readFile("input22b.txt")
   e_hp, e_damage = parseAttributes(file_input)


   # Initialize the player's hp and mana and
   # define game_status.
   p_hp = 50
   p_mana = 500
   
   # Game status: e_hp, e_damage, p_hp, p_mana,
   # shield, poison, recharge, mana_cost)
   game_status = (e_hp, e_damage, p_hp, p_mana, 0, 0, 0, 0)

   # Play the game.
   playGame(game_status)
   
   # Display the minimum mana cost of a win
   print('Minimum mana cost of a win = ' + str(min_mana))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
