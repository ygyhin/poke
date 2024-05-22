

import csv
import random
import re
import copy

loop = True

number_list = []
name_list = []
type_1_list = []
type_2_list = []
total_list = []
hp_list = []
attack_list = []
defense_list = []
sp_atk_list = []
sp_def_list = []
speed_list = []
generation_list = []
legendary_list = []

with open('PokeDex.csv', 'r') as file: 
    reader = list(csv.reader(file))  #reads the PokeDex.csv file and stores it in a list called reader

    for row in reader:  #assigns each column in reader as a list to a variable
        number_list.append(row[0])
        name_list.append(row[1])
        type_1_list.append(row[2])
        type_2_list.append(row[3])
        total_list.append(row[4])
        hp_list.append(row[5])
        attack_list.append(row[6])
        defense_list.append(row[7])
        sp_atk_list.append(row[8])
        sp_def_list.append(row[9])
        speed_list.append(row[10])
        generation_list.append(row[11])
        legendary_list.append(row[12])

reader[0] = "No.     Name                     Type 1     Type 2    Total     HP     Attack    Defense  Sp. Atk    Sp. Def   Speed  Generation     Legendary"

error_msg = "Please enter a valid input."

###ALL FUNCTIONS###

def display(i):
    '''
    When called, displays stats of pokemon that has been searched for
    '''
    txt = f"{number_list[i]:<5} {name_list[i]:<26} {type_1_list[i]:<10} {type_2_list[i]:<10} {total_list[i]:<8} {hp_list[i]:<8} {attack_list[i]:<8} {defense_list[i]:<9} {sp_atk_list[i]:<9} {sp_def_list[i]:<10} {speed_list[i]:<8} {generation_list[i]:<12} {legendary_list[i]:<8}"
    print(txt)

def list_all():
    '''
    When called, displays a selected range of pokemon. Leave input blank to display all 
    pokemon
    '''
    print("Leave starting blank to start from 0, leave ending blank to end at 800")
    start = input("Enter the starting index: ")
    end = input("Enter the ending index(inclusive): ")
    if start == "":
        start = 1
    if end == "":
        end = len(number_list) - 1
    start = int(start)
    end = int(end)
    if start >= 0 and end < len(number_list): # number_list contains strings, cant use 'in' to check for int(start)
        print(reader[0]) #prints header
        for i in range(int(start), int(end) + 1):
            display(i)
    else: 
        print(error_msg + " Index is from 1 to 800")

def index_search():
    '''
    When called, searches for pokemon by index number and displays its stats
    '''
    index = input("Enter an index: ")
    if index in number_list:
        print(reader[0]) #prints header
        for i in range(0, len(number_list)):
            if index == number_list[i]:
                display(i)
    else:
        print(error_msg + " Index is from 1 to 800")
            
def name_search():
    '''
    When called, searches for pokemon by name and displays stats of pokemon matching the search
    '''
    name = input("Enter a pokemon name: ").lower()
    print(reader[0]) #prints header
    #if name in name_list.lower():
    for i in range(0, len(name_list)):
        if name in name_list[i].lower():
            display(i)
    #else:
        #print(error_msg + " Pokemon not found")
        
def type_search():
    '''
    When called, searches for pokemon by type and displays stats of pokemon matching the search
    '''
    type_1 = input("Enter type 1: ").lower()
    type_2 = input("Enter type 2(leaves this blank if you only want to search for one type): ").lower()
    print(reader[0]) #prints header
    if type_2 == "":
        for i in range(0, len(name_list)):
            if type_1 in type_1_list[i].lower():   
                display(i)
    else:
        for i in range(0, len(name_list)):
            if (type_1 in type_1_list[i].lower() and type_2 in type_2_list[i].lower()) or (type_2 in type_1_list[i].lower() and type_1 in type_2_list[i].lower()):
                display(i)


def BST_search():
    '''
    When called, searches for pokemon by base stat total
    and displays stats of pokemon matching the range
    '''
    print("Leave minimum empty for 0, leave maximum empty for 780")
    min = input("Enter the minimum BST: ")
    max = input("Enter the maximum BST: ")
    if min == "":
        min = 0
    if max == "":
        max = 780
    if int(min) > 780 or int(max) < 0:
        print(error_msg + " BST is from 0 to 780")
        return
    print(reader[0])
    for i in range(1, len(name_list)):
        if int(total_list[i]) >= int(min) and int(total_list[i]) <= int(max):
            display(i)

def legendary_search():
    """
    When called, searches for legendary pokemons of specific types and displays stats of pokemon matching the search
    """
    type_1 = input("\n\nLeave both types blank to see all legendary pokemons. \n\nEnter type 1: ").lower()
    type_2 = input("Enter type 2: ").lower()
  
    check_legend = False
    counter = 0
  
    for i in range(1, len(name_list)):
        if counter == 0 and legendary_list[i] == 'TRUE' and (type_1 in type_1_list[i].lower() and type_2 in type_2_list[i].lower() or type_2 in type_1_list[i].lower() and type_1 in type_2_list[i].lower()):         
          print(reader[0])
          counter += 1 # so header stops printing
          check_legend = True                        # so typo error message doesn't print


    for i in range(1, len(name_list)):
      if legendary_list[i] == 'TRUE' and (type_1 in type_1_list[i].lower() and type_2 in type_2_list[i].lower() or type_2 in type_1_list[i].lower() and type_1 in type_2_list[i].lower()):
        display(i)
        
          
              
    if not type_1.isalpha() and type_1 != '' or not type_2.isalpha() and type_2 != '':
        print(error_msg)
        return

    if check_legend == False:
      print("Check for typos. No legendary pokemon of the given types were found")
        

        
def random_pokemon():
    '''
    Displays a random pokemon from the list
    '''
    print(reader[0])
    i = random.randint(1, len(name_list))
    display(i)

def adv_stat_search():
    '''
    Searches for pokemon with a minimum amount in certain stat values
    '''
    min_hp = input("Minimum HP: ")
    min_atk = input("Minimum Attack: ")
    min_spatk = input("Minimum Special Attack: ")
    min_def = input("Minimum Defense: ")
    min_spdef = input("Minimum Special Defense: ")
    min_speed = input("Minimum Speed: ")
    min_stat = [min_hp, min_atk, min_def, min_spatk, min_spdef, min_speed]

    check_poke_stats = False   # Variable to track if any pokemon stats match the criteria

    for stat in range(0, len(min_stat)):
        if min_stat[stat] == "":
            min_stat[stat] = str(0)

    # checks if the entered values are valid
    if not (min_hp.isdigit() or min_hp == '') or not (min_atk.isdigit() or min_atk == '') or not (min_spatk.isdigit() or min_spatk == '') or not (min_def.isdigit() or min_def == '') or not (min_spdef.isdigit() or min_spdef == '') or not (min_speed.isdigit() or min_speed == ''):
      print("Error: Input must be integers or empty strings.")
      return
      


  

    check_poke_stats = False

    counter = 0
  
    for i in range(1, len(name_list)):
      if counter == 0 and int(hp_list[i]) >= int(min_stat[0]) and int(attack_list[i]) >= int(min_stat[1]) and int(sp_atk_list[i]) >= int(min_stat[2]) and int(defense_list[i]) >= int(min_stat[3]) and int(sp_def_list[i]) >= int(min_stat[4]) and int(speed_list[i]) >= int(min_stat[5]):
        check_poke_stats = True                # if stats match criteria, then check_poke_stats becomes true
        if check_poke_stats:
          print(reader[0])
          counter += 1


    for i in range(1, len(name_list)):
        if int(hp_list[i]) >= int(min_stat[0]) and int(attack_list[i]) >= int(min_stat[1]) and int(sp_atk_list[i]) >= int(min_stat[2]) and int(defense_list[i]) >= int(min_stat[3]) and int(sp_def_list[i]) >= int(min_stat[4]) and int(speed_list[i]) >= int(min_stat[5]):
          check_poke_stats = True                # if stats match criteria, then check_poke_stats becomes true
          if check_poke_stats:
            display(i)

    
        
          

    if check_poke_stats == False:                # and if it does not, then check_poke_stats remains false
      for i in range(1, len(name_list)):
        if (int(min_stat[0]) > int(hp_list[i]) or 
          int(min_stat[1]) > int(attack_list[i]) or 
          int(min_stat[2]) > int(sp_atk_list[i]) or 
          int(min_stat[3]) > int(defense_list[i]) or 
          int(min_stat[4]) > int(sp_def_list[i]) or 
          int(min_stat[5]) > int(speed_list[i])):
            print('No pokemon has such powerful stats.')
        break
 
        
###BATTLE SIMULATOR###

normal_list = []
fire_list = []
water_list = []
electric_list = []
grass_list = []
ice_list = []
fighting_list = []
poison_list = []
ground_list = []
flying_list = []
psychic_list = []
bug_list = []
rock_list = []
ghost_list = []
dragon_list = []
dark_list = []  
steel_list = []
fairy_list = []

matchup_dict = {}

with open('TypeMatchup.csv', 'r') as file: 
    typereader = list(csv.reader(file))  #reads the TypeMatchup.csv file and stores it in a list called typereader

    for row in typereader:  #assigns each column in typereader as a list to a variable
        normal_list.append(row[1])
        fire_list.append(row[2])
        water_list.append(row[3])
        electric_list.append(row[4])
        grass_list.append(row[5])
        ice_list.append(row[6])
        fighting_list.append(row[7])
        poison_list.append(row[8])
        ground_list.append(row[9])
        flying_list.append(row[10])
        psychic_list.append(row[11])
        bug_list.append(row[12])
        rock_list.append(row[13])
        ghost_list.append(row[14])
        dragon_list.append(row[15])
        dark_list.append(row[16])
        steel_list.append(row[17])
        fairy_list.append(row[18])
        matchup_dict[row[0]] = row[1:19]

lowercase_matchup_dict = {key.lower(): value for key, value in matchup_dict.items()}


type_to_index = {'normal': 0, 'fire': 1, 'water': 2, 'electric': 3, 'grass': 4, 'ice': 5, 'fighting': 6, 'poison': 7, 'ground': 8, 'flying': 9, 'psychic': 10, 'bug': 11, 'rock': 12, 'ghost': 13, 'dragon': 14, 'dark': 15, 'steel': 16, 'fairy': 17}


class Pokemon:
    def __init__ (self, name, type_1, type_2, hp, attack, defense, sp_atk, sp_def, speed, i):
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.i = i

def match_up(atktype, deftype):
    '''
    When called, returns the type matchup of the attacking pokemon and the defending pokemon
    '''
    lowercase_matchup_dict = {key.lower(): value for key, value in matchup_dict.items()}
  
    matchup_value = lowercase_matchup_dict[atktype.lower()][type_to_index[deftype.lower()]]
    return float(matchup_value)

def damage_calc(atkstat, atktype, defstat, deftype):
    '''
    Calculates damage dealt by attacker to defender
    '''
    damage = int(atkstat)/(int(defstat)/2) * random.randint(10, 15)
    damage = damage * match_up(atktype, deftype)
    return damage


def battle_sim():
    '''
    initialises battle simulator
    '''
    Battle = True

   

    
    print("Battle Simulator")
    print("(Leave the followings blank for random pokemon)")
    index1 = input("Enter the index of the first pokemon: ")
    index2 = input("Enter the index of the second pokemon: ")
  
    # if left blank
    if index1 == "":
        index1 = random.randint(1, len(name_list))
    if index2 == "":
        index2 = random.randint(1, len(name_list))

    #pokemon value placeholders
    pokemon1 = Pokemon("", "", "", 1, 1, 1, 1, 1, 1, 1)
    pokemon2 = Pokemon("", "", "", 1, 1, 1, 1, 1, 1, 1)
    actual_index1 = int(number_list[int(index1)])
    actual_index2 = int(number_list[int(index2)])

    pokemon1 = Pokemon(name_list[actual_index1], type_1_list[actual_index1], type_2_list[actual_index1], 
                       hp_list[actual_index1], attack_list[actual_index1], defense_list[actual_index1], 
                       sp_atk_list[actual_index1], sp_def_list[actual_index1], speed_list[actual_index1], actual_index1)


#

#assigns stats to pokemon2
#if int(index2) in number_list:
    pokemon2 = Pokemon(name_list[actual_index2], type_1_list[actual_index2], type_2_list[actual_index2], 
       hp_list[actual_index2], attack_list[actual_index2], defense_list[actual_index2], 
       sp_atk_list[actual_index2], sp_def_list[actual_index2], speed_list[actual_index2], actual_index2)


    
#main battle loop
    print('\nBattle Start!')
    print()
    print(f"{pokemon1.name} vs {pokemon2.name}!")
    print(f"{pokemon1.name} HP: {pokemon1.hp}")
    print(f"{pokemon2.name} HP: {pokemon2.hp}")
    input("\n\nEnter anything to continue")
    round = 1
    while Battle:
      #calculate based off atk and def
        if pokemon1.attack > pokemon1.sp_atk:
            damage = damage_calc(pokemon1.attack, pokemon1.type_1,  pokemon2.defense, pokemon2.type_1)
      #calculate based off spatk and spdef
        else:
            damage = damage_calc(pokemon1.sp_atk, pokemon1.type_1,  pokemon2.sp_def, pokemon2.type_1)
          
        print(f"\n\nRound {round}! \n{pokemon1.name} dealt {damage:.1f} damage to {pokemon2.name}!")
        pokemon2.hp = float(pokemon2.hp) - damage
        if pokemon2.hp <= 0:
            pokemon2.hp = 0

      
      #calculate based off atk and def
        if pokemon1.attack > pokemon1.sp_atk:
            damage = damage_calc(pokemon1.attack, pokemon1.type_1,  pokemon2.defense, pokemon2.type_1)
      #calculate based off spatk and spdef
        else:
            damage = damage_calc(pokemon1.sp_atk, pokemon1.type_1,  pokemon2.sp_def, pokemon2.type_1)
          
        print(f"{pokemon2.name} dealt {damage:.1f} damage to {pokemon1.name}!")
        pokemon1.hp = float(pokemon1.hp) - damage
        if pokemon1.hp <= 0:
            pokemon1.hp = 0
          

        if pokemon1.hp > 0 and pokemon2.hp > 0:
            print(f"\n{pokemon1.name} HP: {pokemon1.hp:.1f}")
            input(f"{pokemon2.name} HP: {pokemon2.hp:.1f} \n \nPress enter to begin next round!")
            round += 1
    
        if pokemon1.hp <= 0 and pokemon2.hp <= 0:
          print(f"\n\nTie! Both {pokemon1.name} and {pokemon2.name} fainted at the same time.")
          Battle = False
          return
                 
        if pokemon1.hp <= 0:
            print(f"\n{pokemon1.name} HP: {pokemon1.hp:.1f}")
            print(f"{pokemon2.name} HP: {pokemon2.hp:.1f}")
            print(f"\n{pokemon1.name} fainted! {pokemon2.name} wins!")
            Battle = False
            return
        elif pokemon2.hp <= 0:
            print(f"\n{pokemon2.name} HP: {pokemon2.hp:.1f}")
            print(f"{pokemon1.name} HP: {pokemon1.hp:.1f}")
            print(f"\n{pokemon2.name} fainted! {pokemon1.name} wins!")
            Battle = False
            return
          

        
        
            
        
                
            

###MENU LOOP###
    
def menu_loop():
    '''
    Initialises menu loop (loops when called)
    '''
    global loop             # when user chooses 0,  loop = False inside menu_loop stops loop outside this function
    print('''                
    Welcome to the PokeDex!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Options:
    1. Display a selected range of Pokemon by index
    2. Display a selected Pokemon by index
    3. Search for Pokemon by name
    4. Search for Pokemon by type
    5. Search for Pokemon by BST range
    6. Search for Pokemon by minimum stats
    7. Display all legendary Pokemon by type
    8. Display a random Pokemon
    9. Inititate Battle Simulator
    0. Exit PokeDex
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    To select a function, enter the number of the function you would like to use.
    ''')
    choice = input()
    if choice == '1':
        list_all()
    elif choice == '2':
        index_search()
    elif choice == '3':
        name_search()
    elif choice == '4':
        type_search()
    elif choice == '5':
        BST_search()
    elif choice == '6':
        adv_stat_search()
    elif choice == '7':
        legendary_search()
    elif choice == '8':
        random_pokemon()
    elif choice == '9':
        battle_sim()
    elif choice == '0': 
        print("Goodbye!")
        loop = False
    else: 
     print("Invalid input. Please try again.")
     menu_loop()

###MAIN PROGRAM###
# counter added so the 'again' input below doesnt appear at the start 
# does not affect while loop
menu_loop()

while loop:
  again = input("\nWould you like to search again? (y/n) ") #asks user if they want to search again
  if again == "n":
      print("Goodbye!")
      loop = False
  else:
      menu_loop()

    




