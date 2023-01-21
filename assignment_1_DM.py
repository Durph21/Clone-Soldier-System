#Program includes Clone Class with Subclasses, as well as a Weapon Class
#Note - Clones are basically soldiers, but from Star Wars
#There is also a mini game to implement such class objects

#Importing functions such as the following:
from random import randint
from os import system
from typing import ClassVar
from datetime import datetime

#Class to create simple clone model
#Clones must be given a name, rank, and regiment.
#A Clone id id then created using different parts of the strings, name, rank and regiment
#, as well as adding a number to the end, increasing, so no matter what name or rank someone has that 
# No 2 clone id's are the same. 
class clone:
     #number given to first clone, with every clone increasing
    num_of_clones: ClassVar[int] = 0
    number: ClassVar[int] = 1

    name: ClassVar[str]
    rank: ClassVar[str]
    regiment: ClassVar[str]
    number: ClassVar[int]
    clone_id: ClassVar[str]
    def __init__(self, name:str , rank:str, regiment:str) -> None:
        if type(name) == str:
            self.name = name
        else:
            raise ExceptionError("Please enter a valid name, as a string")
        if type(rank) == str:
            self.rank = rank
        else:
            raise ExceptionError("Please enter a valid rank, as a string")
        if type(regiment) == str:
            self.regiment = regiment
        else:
            raise ExceptionError("Please enter a valid regiment, as a string")
        self.number = clone.number

        #clone id made using parts of strings concatenated together 
        self.clone_id= name[:2].lower() + rank[:2].lower() + regiment[:3] + "-" + str(clone.number)
        clone.num_of_clones += 1
        clone.number += 1

    #Property and setter
    @property
    def rank(self):
        return self.__rank
    
    def name(self):
        return self.__name
    
    def regiment(self):
        return self.__regiment

    @rank.setter
    def rank(self, rank: str): 
        self.__rank = rank
    
    def name(self, name: str):
        self.__name = name

    def regiment(self, regiment: str):
        self.__regiment = regiment

    #function to return information to do with said clone
    def clone_credentials(self) -> str:
        #simple string return with place holders to display basic information about a
        #particular clone trooper
        return 'Clone {}:\n{}\n{}\n{}\n'.format(self.clone_id, self.name, self.rank, self.regiment)

    #function to return a name and id of clones under said commander
    def commands(self) -> str:
        return '{}, {} '.format(self.name, self.clone_id)

    def ranking_order(self):
        pass

    #repr + str functions for returning said information in a more user friendly format
    def __repr__(self):
        return "Clone Trooper:('{}', '{}', '{}', '{}')".format(self.name, self.rank, self.regiment, self.clone_id)

    def __str__(self):
        return '{} - {}'.format(self.clone_id(), self.name)
    
    #Control len, returns the length(amount of characters) of clone credentials
    def __len__(self):
        return len(self.clone_credentials())

    def __add__(self, other):
        return self.name + ", " + other.name

    #Rank Promotions:
    #function to apply promotion in rank to a clone
    #example: trooper ---> captain
    def apply_promotion(self):
        self.rank = self.promotion_rank

     #method to set what the promotion for a clone is going to be
     # captain, commander, lieutenant   
    @classmethod
    def set_promotion(cls, promotion):
        cls.promotion_rank = promotion

    #simple static method to check if a certain day is a day for being on active duty
    @staticmethod
    def on_duty(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#captain class, similar to clone except it also takes into account their (jedi) general
#uses supper() to call in previously made function above
class captain(clone):
    #to count number of captains
    num_of_captains:ClassVar[int] = 0
    def __init__(self, name, rank, regiment, general):
        super().__init__(name, rank, regiment)
        self.general = general

    num_of_captains += 1

#commander class, this class again takes in the basic clone information as above by using super()
#it then implements a new parameter 'clones' which shows us the clones under commandment by said commander
#it can return a list like feature of clones or the number of clones under said command 
class commander(clone):

    #as usual, easy commander counter
    num_of_commanders = 0
    def __init__(self, name, rank, regiment, clones=None):
        super().__init__(name, rank, regiment)
        #this empty list is used if there is no clones under commandment
        if clones is None:
            self.clones=[]
        else:
            self.clones = clones
        commander.num_of_commanders += 1

    #function to add a clone to the list of clones under command
    def add_clone(self, cl):
        if cl not in self.clones:
            self.clones.append(cl)

    #function for removing any clones from the list returned of clones under command
    def remove_clone(self, cl):
        if cl in self.clones:
            self.clones.remove(cl)

    #this function gives structure to the list returned and makes it more readable
    def print_clone(self):
        print(self.name + " Commands: ")
        for cl in self.clones:
            print("-->", cl.commands())

#Weapons Class
class weapon:
    #Define Variables
    #weapon Inventory
    inventory: ClassVar[dict] = {}

    #Weapon object variables
    weapon_name: ClassVar[str]
    ammunition: ClassVar[str]
    rounds: ClassVar[int]
    weapon_id: ClassVar[int] = 0

    num_of_weapons: ClassVar[int] = 0
    number: ClassVar[int] = 1
    num = 1
    #Create init function
    #Define each variable according to self, with error handling.
    def __init__(self, weapon_name:str , ammunition:str, rounds:int) -> None:
        if type(weapon_name) == str:
            self.weapon_name = weapon_name
        else: 
            raise ExceptionError("Please enter the name of a weapon. As a string")
        if type(ammunition) == str:
            self.ammunition = ammunition
        else:
            raise ExceptionError("Please enter a valid form of ammunition, as a string")
        if type(rounds) == int:
            self.rounds = rounds
        else:
            raise ExceptionError("Please enter a valid integer for rounds")
        self.number = weapon.number
        self.weapon_id = weapon_name[:2].lower() + "-" + str(weapon.number)

        #dictionary to store weapons and their quantity, like a inventory
        #New Weapon objects are added to the inventory, while others are just raised in quantity
        num = 1
        if weapon_name in weapon.inventory:
            weapon.inventory[weapon_name] += 1
    
        else:
            weapon.inventory[weapon_name] = num

    #property methods
    @property
    def ammunition(self):
        return self.__ammunition
    
    def rounds(self):
        return self.__rounds
    
    def weapon_name(self):
        return self.__weapon_name

    #getters and setters
    @ammunition.setter
    def ammunition(self, ammunition: str):
        self.__ammunition = ammunition
    
    def rounds(self, rounds: int):
        self.__rounds = rounds

    def weapon_name(self, weapon_name: str):
        self.__weapon_name = weapon_name
    
    #repr + str functions for returning said information in a more user friendly format
    def __repr__(self):
        return "Weapon:('{}', '{}', '{}', '{}')".format(self.weapon_name, self.ammunition, self.rounds, self.weapon_id)

    def __str__(self):
        return '{} - {}'.format(self.weapon_id(), self.weapon_name)

    #function to return a weapon inventory, using 2 lists from the dictionary displaying them..
    #... in a more readable manner, showing weapon name and the quantity
    def weapon_arsenal() -> str:
        a = weapon.inventory.keys()
        b = weapon.inventory.values()
        string = "\n".join("Weapon: {}, Quantity: {}".format(x, y) for x, y in zip(a, b))
        return string

#Class for error handling
class ExceptionError(Exception):
    pass   
    
#create clones(soldiers) objects
clone1 = clone('Echo', 'Trooper', '501st' )
clone2 = captain('Jek', 'Captain', '101st', 'Plo Koon') #Note - Captains take one extra parameter, as per the class definition
clone3 = captain('Rex', 'Captain', '501st', 'Sky-walker')
clone4 = clone('Fives', 'Trooper', '501st' )
clone5 = clone("Jesse", "Trooper", "501st")
#Note - Commander below had parameter that shows all clones under his commandment
clone6 = commander('Cody', 'Commander', '212th', [clone1, clone2, clone3, clone4, clone5])

#create weapon(guns) objects
weapon1 = weapon('Blaster', '23Cal', 80)
weapon2 = weapon('Pistol', '13bl', 26)
weapon3 = weapon('Sniper', '50cal', 7)
weapon4 = weapon('Flame Thrower', '23 GAS', 1000)
weapon5 = weapon('Light Saber', 'Light', 1000000000000)
weapon6 = weapon('Pistol', '23Cal', 95)



def mini_game():
    system('clear')
    print("List of Clones:")
    a = True
    b = True
    c = True
    while a == True:
        clones = [clone1.name, clone2.name, clone3.name, clone4.name, clone5.name]
        for clone in clones:
            print("--> " + clone)
        clone_choice = input("\nChoose a Clone Trooper:\n")
        if clone_choice in clones:
            system('clear')
            break
    while b == True:
        weapons = [weapon1.weapon_name, weapon2.weapon_name, weapon3.weapon_name, weapon4.weapon_name, weapon5.weapon_name, weapon6.weapon_name]
        for weapon in weapons:
            print("--> " + weapon)
        weapon_choice = input("\nChoose a Weapon: \n")
        if weapon_choice in weapons:
            system('clear')
            break
    while c == True:
        planets = ["Hoth", "Endor", "Tatooine", "Courosant", "Ryloth"]
        print("Choose a planet:\n")
        for planet in planets:
            print("-->" + planet)
        print("\n")
        planet_choice = input("Set coordinates for: ")
        if planet_choice in planets:
            system('clear')
            print("\nYou chose Clone Trooper " + clone_choice + ", weapon of choice, a " + weapon_choice + ".\n\nYou have just landed on " + planet_choice+".")
            if planet_choice == "Hoth":
                    print("You're lucky you brought warm cloths.")
            if planet_choice == "Endor" and weapon_choice == "Sniper":
                    print("Good thing you chose a sniper. You'll can shoot from the trees. You've got this.\n ")
            if planet_choice == "Tatooine":
                    print("Uughh Sand, its course and rough and gets everywhere.")
            if planet_choice == "Courosant":
                    print("Ah yes, home to the jedi temple.")
            if planet_choice == "Ryloth":
                    print("I hate this planet.")
            break

    action = ["run", "hide", "fight"]
    c = True
    while c == True:
        print("Quick! Theres droids approaching! What are you going to do?\n")
        for i in action:
            print("--> " + i)
        action_choice = input()
        if action_choice in action:
            system('clear')
            print("You chose to " + action_choice+"!\n")
            if action_choice == "fight":
                droids = randint(1, 100)
                print("\nYou give your all for the republic, taking out", droids ,"droids.\n")
                fight_actions = ["escape", "keep fighting"]
                if droids >= 45:
                    print("What will you do now?")
                    for i in fight_actions:
                        print("-->" + i)
                    fight_choice = input()
                    if fight_choice == "keep fighting":
                        print("\nHelp finally arrives and you earn a rank promotion by Obi Wan Kenobi\n")
                        return 'Game over'
                    elif fight_choice == "escape":
                        system('clear')
                        print("\nAfter giving your all, you manage to escape only to run into General Grevious.\nYou Challenge him to hand to hand combat but unfortunately he rips your arms off and you die.\n")
                        return 'Game Over'
                        
                else:
                   print("You were overwhelmed by separatist forces, and died fighting for the grand republic.\n")
                   return "Game Over"

            if action_choice == "hide":
                droids = randint(1, 100)
                print("\nYou manage to hide while the separatist forces march by.\n")
                fight_actions = ["escape", "ambush"]
                if droids >= 10:
                    print("What will you do now?")
                    for i in fight_actions:
                        print("-->" + i)
                    fight_choice = input()
                    if fight_choice == "ambush":
                        system('clear')
                        print("\nIn a fit of rage you, you burst out of your hiding spot and seek vengeance for all\n your fallen brothers.\nThe droids are strong in numbers but you have the heart of a lion, and keep on fighting.\nEventually, backup arrives and you win the battle. Soon you are promoted to a commander in the grand republic army\n")
                        return "Game over, or is it..."
                        
                    if fight_choice == "escape":
                        print("\nAfter a petty attempt to escape, you run into General Grevious.\nYou Challenge him to hand to hand combat but unfortunately he rips your arms off and you die.\n")
                        return 'Game Over'

            if action_choice == "run":
                droids = randint(1, 100)
                print("\nYou manage to hide while the separatist forces march by.\n")
                fight_actions = ["run", "fight"]
                if droids >= 7:
                    print("What will you do now?")
                    for i in fight_actions:
                        print("-->" + i)
                    fight_choice = input()
                    if fight_choice == "fight":
                        system('clear')
                        print("\nIn a fit of rage you, you turn back and charge towards the droids and seek vengeance for all your \nfallen brothers.\nThe droids are strong in numbers but you have the heart of a lion, and keep on fighting.\nEventually, backup arrives and you win the battle. Soon you are promoted in the grand republic army.\nYou Are A Hero\n")
                        return "Game over, or is it..."
                        
                    if fight_choice == "run":
                        system('clear')
                        print("\nAfter not even attempting to fight the droids, you are called out for being a deserter and court martialed. You Failed the republic\n")
                        return 'Game Over'
                else:
                   print("Despite being chased by thousands of droids, you make it back to base where you find backup.\nYou return to outnumber and overwhelm the separatists,\n achieving a monumental victory for the Republic in the Clone Wars\n You Are A Hero")
                   return "Game Over"
                return

    
            

#print statements
#just comment or uncomment to easier see how each class and object is callable.

#basic functionality
print(clone1.name)
print(clone3.rank)
print(clone4.regiment)
print(clone2.general)
print(clone3.clone_id)
print(clone.num_of_clones, "Clones")
print(commander.num_of_commanders, "Commander")
print(captain.num_of_captains, "Captain")
print("--------------------------")


#clone credentials
print(clone1.clone_credentials())
print(clone2.clone_credentials())
print(clone3.clone_credentials())
print(clone4.clone_credentials())
print(clone5.clone_credentials())
print("--------------------------")

#print commander and commanded
clone6.print_clone()
print("--------------------------")

#checking subclasses and instances
print(issubclass(commander, clone))
print(isinstance(clone3, clone))
print(isinstance(clone2, commander))
print(isinstance(clone2, captain))
print("--------------------------")

#Print weapon classes
print(weapon3.weapon_name)
print(weapon3.ammunition)
print(weapon3.rounds)
print(weapon3.weapon_id)
print("\n")
print(weapon.inventory)
print(weapon.weapon_arsenal())
print(type(weapon1.weapon_name))
print("--------------------------")

#Mini game. Fun way to see some of the class objects implemented
#Just Simply uncomment the print statement below and run the program.
#Hope you like it 

'''print(mini_game())'''

def FizzBuzz(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 ==0 and i % 5 !=0:
            print("Fizz")
        elif i % 5 == 0 and i %3 != 0:
            print("Buzz")
        else:
            print(i)
FizzBuzz(15)