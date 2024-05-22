num = []
name = []
type1 = []
type2 = []
total =[]
hp = []
attack = []
defense = []
sp_atk = []
sp_def =[]
speed = []
generation = []
legendary = []

attacking =[]	
normal = []	
fire = []	
water = []	
electric = []	
grass = []	
ice = []	
fighting = []	
poison = []	
ground = []	
flying = []	
psychic = []	 
bug	= [] 
rock	= []
ghost = []	
dragon = []
dark = [] 
steel = []
fairy = []

import csv
with open("chart.csv", "r") as chart:
  chart = csv.reader(chart, delimiter=',')
  header = next(chart)
  for row in chart:
    attacking.append(row[0])
    normal.append(row[1])
    fire.append(row[2])
    water.append(row[3])
    electric.append(row[4])
    grass.append(row[5])
    ice.append(row[6])
    fighting.append(row[7])
    poison.append(row[8])
    ground.append(row[9])
    flying.append(row[10])
    psychic.append(row[11])
    bug.append(row[12])
    rock.append(row[13])
    ghost.append(row[14])
    dragon.append(row[15])
    dark.append(row[16])
    steel.append(row[17])
    fairy.append(row[18])

t = [normal, fire, water, electric, grass, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy] 


with open("Pokemon.csv", "r") as file:
  file = csv.reader(file, delimiter=',')
  header = next(file)
  for row in file: # adds each item in a column into their respective list
    num.append(row[0])
    name.append(row[1])
    type1.append(row[2])
    type2.append(row[3])
    total.append(row[4])
    hp.append(row[5])
    attack.append(row[6])
    defense.append(row[7])
    sp_atk.append(row[8])
    sp_def.append(row[9])
    speed.append(row[10])
    generation.append(row[11])
    legendary.append(row[12])

def head(): # header formatting
  print(header[0].ljust(3,' '), header[1].ljust(28,' '), header[2].ljust(10,' '), \
        header[3].ljust(10,' '), header[4].ljust(9,' '), header[5].ljust(9,' '), \
        header[6].ljust(9,' '), header[7].ljust(9,' '), header[8].ljust(9,' '), \
        header[9].ljust(9,' '), header[10].ljust(9,' '), \
        header[11].ljust(12,' '), header[12])

def formatting(line_number): # formatting for each line
  print(num[line_number].ljust(3,' '), name[line_number].ljust(28,' '), \
        type1[line_number].ljust(10, ' '), type2[line_number].ljust(10, ' '), \
        total[line_number].ljust(9, ' '), hp[line_number].ljust(9, ' '), \
        attack[line_number].ljust(9, ' '), defense[line_number].ljust(9, ' '), \
        sp_atk[line_number].ljust(9, ' '), sp_def[line_number].ljust(9, ' '), \
        speed[line_number].ljust(9, ' '), generation[line_number].ljust(12, ' '), \
        legendary[line_number])


def option1(): 
  display_num = input("Enter number of pokemon to be displayed: ")
  if display_num == "all": #if 'all' -> display all pokemon
    display_num = len(num)
  head()
  line_number = 0
  for i in range(0, int(display_num)): # prints each line from 1 to the display_num
    formatting(line_number) 
    line_number += 1


def option2(): 
  type_choice = input("Enter type: ")
  type_choice = type_choice.title()
  if (type_choice in type1) or (type_choice in type2):  #to check whether type is valid
    head()
    line_number = 0
    for i in type1:
      if (type1[line_number]==type_choice) or (type2[line_number]==type_choice): 
        return formatting(line_number)
        # breaks the loop after finding the first pokemon of the type
      elif (type1[line_number]!=type_choice) and (type2[line_number]!=type_choice):
        line_number += 1
  elif (type_choice not in type1) and (type_choice not in type2):  #if invalid type entered
    print('No pokemon of this type.')
    return


def option3():
  total_stats = int(input("Enter total base stat: "))
  line_number = 0
  head()
  for i in total:
    if int(i) == total_stats: # if total stats meet the input requirements
      formatting(line_number)
    line_number += 1
  return


def option4(): 
  sp_atk_copy = [eval(i) for i in sp_atk]
  sp_def_copy = [eval(i) for i in sp_def]
  speed_copy = [eval(i) for i in speed]  
  # ^^convert the numbers in str form into int for the respective stats
  min_spatk = int(input("Enter minimum special attack stat: "))
  min_spdef = int(input("Enter minimum special defense stat: "))
  min_speed = int(input("Enter minimum speed stat: "))
  line_number = 0
  if (max(sp_atk_copy)>=min_spatk) and \
  (max(sp_def_copy)>=min_spdef) and (max(speed_copy)>=min_speed): 
    # if all stats input are smaller than or equal to the maximum stats
    head()
    for i in num:
      if int(sp_atk[line_number]) >= min_spatk and \
      int(sp_def[line_number]) >= min_spdef and int(speed[line_number]) >= min_speed:
        #if the stats for that pokemon are above or equal to the minimum input
        formatting(line_number)
      line_number += 1
  else: #if input stats are greater than max stats
    print("No pokemon with such powerful stats.")
  return





def option6():
  import random
  player1_choice = input("Player 1 enter pokemon name or line number: ")
  player2_choice = input("Player 2 enter pokemon name or line number: ")
  print()
  # verify pokemon name, line number or duplicates
  if player1_choice == player2_choice: # duplicates
    print("no duplicates")
    return
  # player 1 choice of pokemon
  if player1_choice.isnumeric() == False: # if player 1 enters a name
    player1_choice = player1_choice.title()
    p1_index = name.index(player1_choice)  
  elif player1_choice.isnumeric() == True: # if player 1 enters a line number
    p1_index = int(player1_choice)-1
  # player 2 choice of pokemon
  if player2_choice.isnumeric() == False: # if player 1 enters a name
    player2_choice = player2_choice.title()
    p2_index = name.index(player2_choice)
  elif player2_choice.isnumeric() == True: # if player 1 enters a line number
    p2_index = int(player2_choice)-1
  
  # random mechanics to calculate dmg using both atk and def stats
  casualty = 0
  round = 1
  hp1 = int(hp[p1_index])*2
  hp1_original = hp1
  hp2 = int(hp[p2_index])*2
  hp2_original = hp2
  damage1 = (int(attack[p1_index])/2 - int(defense[p2_index])/10) 
  damage2 = (int(attack[p2_index])/2 - int(defense[p1_index])/10)
  sp_damage1 = (int(sp_atk[p1_index])/2 - int(sp_def[p2_index])/10) 
  sp_damage2 = (int(sp_atk[p2_index])/2 - int(sp_def[p1_index])/10)

  #type check
  p1_type = type1[p1_index]
  p2_type = type1[p2_index]
  print('Player 1', name[p1_index], 'VS Player 2', name[p2_index])
  print(p1_type, 'type VS', p2_type, 'type\n')
  p1_type_index = attacking.index(p1_type)
  p2_type_index = attacking.index(p2_type)
  p1_multiplier = t[p1_type_index][p2_type_index]
  p2_multiplier = t[p2_type_index][p1_type_index]
  damage1 = damage1*float(p1_multiplier) 
  damage2 = damage2*float(p2_multiplier)
  # damage multiplier by 0, 0.5, 1 or 2 based on type advantage in chart.csv
  
  while casualty < 1:
    print("Round ", round)
    x1 = random.choice([True, False]) # randomly adds special damage
    if x1 == True:
      special_damage1 = f"+ {sp_damage1:.2f} special damage"
    else:
      special_damage1 = ""
    x2 = random.choice([True, False]) # randomly adds special damage
    if x2 == True:
      special_damage2 = f"+ {sp_damage2:.2f} special damage"
    else:
      special_damage2 = ""

    # damage dealt
    print(f"{name[p1_index]} dealt {damage1:.2f} damage {special_damage1} to {name[p2_index]}!")
    print(f"{name[p2_index]} dealt {damage2:.2f} damage {special_damage2} to {name[p1_index]}!")
    
    hp1 = hp1-damage2
    hp2 = hp2-damage1
    if hp1 <= 0:
      hp1 = 0
    elif hp2 <= 0:
      hp2 = 0

    # health left
    print(f"{name[p1_index]} has {hp1:.2f}/{hp1_original} hp left.")
    print(f"{name[p2_index]} has {hp2:.2f}/{hp2_original} hp left. \n")
    round += 1
    input()
    
    if hp1<=0 or hp2<=0: # if hp is depleted
      casualty += 1      # breaks out of while loop
      
  if hp1>hp2:
    print(f"Player 1's {name[p1_index]} wins!")
  else:
    print(f"Player 2's {name[p2_index]} wins!")
  return



loop = True
while loop == True: 
  print("Pokemon Super Search Engine")
  print("1. display selected number of Pokemons with their types and statistics")
  print("2. display the first Pokemon of a Type of the trainer’s choice")
  print("3. display all Pokemons with Total Base stat of the trainer’s choice")
  print("4. display all Pokemons with a minimum set of stats")
  print("5. display all legendary Pokemons of Types of the trainer’s choice")
  print("6. gym battle simulation (surprise)")
  print()
  option = input("Enter option: ")
  print()
  if option == '1':
    option1()
  elif option == '2':
    option2()
  elif option == '3':
    option3()
  elif option == '4':
    option4()
  elif option == '5':
    pass
  elif option == '6':
    option6()
  else: 
    loop = False

    print('-'*120, '\n \n \n \n \n')


  
