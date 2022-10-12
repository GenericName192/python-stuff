import random


# Knight class used to store user created knight data. 
class Knight:

    """
    :arg knight_number - The unique identifying number for a knight object.
    :arg name - The name of the knight, for user identifying.
    :arg age - The age of the knight, just for extra flavour.
    :arg weapon - The weapon of the knight, again just for extra flavour.
    :arg level - The level of the knight, used to assign strength, speed and health values for the dueling function.
    """

    # Creates an instance of the knight class.
    def __init__(self, knight_number: int, name: str, age: int, weapon: str, level: int):
        self.knight_number = knight_number
        self.name = name
        self.age = age
        self.weapon = weapon
        self.level = level
        self.strength = 1
        self.speed = 1
        self.health = 1
        self.set_knight_stats()

    # Call this to print out all knight object attributes.
    def print_self(self):
        print("Name: {}\nAge: {}\nWeapon: {}\nLevel: {}\nStrength: {}\nSpeed: {}\nHealth: {}".format(self.name, self.age, self.weapon, self.level, self.strength, self.speed, self.health))

    # Call this to set: strength, speed and health attributes through the use of a random number generator.
    def set_knight_stats(self):

        if  self.level < 6:
            min_stat = 1
            max_stat = 5
        elif self.level < 11:
            min_stat = 3
            max_stat = 10
        elif self.level < 16:
            min_stat = 5
            max_stat = 15
        else: 
            min_stat = 7
            max_stat = 20
        
        self.strength = random.randint(min_stat, max_stat)
        self.speed = random.randint(min_stat, max_stat)
        self.health = random.randint(min_stat, max_stat) + (5 * self.level)


# Call for this when you want to create a new knight.
def create_knight(knights: list) -> None:
    """
    :arg knights - list that will store all of the knight objects 
    """
    print("Lets create a knight!")


    # Set the data up for the knight.
    number = len(knights) + 1
    name = string_checker("What is the knights name: \n")
    age = int_checker("How old is the knight: (18 - 80) \n",18, 80 )
    weapon = string_checker("What weapon does your knight use: \n")
    level = int_checker("What level is your knight: (1 - 20) \n",1,20 )

    # Creates a new knight object using the data collected above.
    new_knight = Knight(number, name, age, weapon, level)

    # Adds the instance of the knight to the list for later retrival.
    knights.append(new_knight)

    # Calls the print self function which prints out all of the knights data.
    print("Your new knight: \n")
    new_knight.print_self()

# Call this to print out a message then make sure the input is a string.
def string_checker(input_string_message: str) -> str:
    """ 
    :arg input_string_message - inputed message to prompt user to input something 
    :return - returns the user input as a string
    """

    user_input = input(input_string_message)
    # checks if user_input is a empty string by checking if user_input is a falsey.
    while not user_input:
        user_input = input("Please try again \n")
    return user_input
     

# Call this like above to print out a message but then make sure the input is an number/int.
def int_checker(input_string_message: str, min_number: int, max_number: int) -> int:
    """ 
    :arg input_string_message - inputed message to prompt user to input something 
    :return - returns the user input as an int
    """

    # This saves the inputted number then checks its a number then checks again agasint the min and max number to make sure its a valid number/int.
    checker = True
    while checker:

        try:
            inputted_number = int(input(input_string_message))
            if inputted_number < min_number or inputted_number > max_number:
                inputted_number = int(input(("Please enter a number between: " + str(min_number) + " and " + str(max_number))))
            else: 
                return inputted_number

        except:
            print("Please try again")
            
   


# Call a knight and change their data
def change_data(knight: Knight):

    """
    :arg knight - instance of the knight class to update attributes
    """

    print("What would you like to update? \n")
    print("1: knights name: " + knight.name)
    print("2: Knights age: " + str(knight.age))
    print("3: Knights weapon: " + knight.weapon)
    print("4: Knights level: " + str(knight.level) + "\n")

    # Checks if the input is valid
    try: 
        selection = int(input("Select your option: \n"))
        tester = True
        while tester == True:

            if selection == 1:
                knight.name = string_checker("what is their new name: ")
                print("Your knights new name is: " + knight.name + "\n")
                tester = False

            elif selection == 2:
                knight.age = int_checker("what is their new age: (18 - 80) ", 18, 80)
                print("Your knights new age is: " + str(knight.age) + "\n")
                tester = False

            elif selection == 3:
                knight.weapon = string_checker("what is their new weapon: ")
                print("Your knights new weapon is: " + knight.weapon + "\n")
                tester = False

            elif selection == 4:
                knight.level = int_checker("what is their new level: ", 1, 20)
                print("Your knights new level is: " + str(knight.level) + "\n")
                knight.set_knight_stats()
                tester = False

            else: 
                print("--- Please select a valid option ---")
                selection = int(input("Select your option: "))

    # Will catch if the input isnt a number/int
    except:
        print("--- Try again! --- \n")
        change_data(knights)
        return
        

# Show the current knights and select one
def select_knight(knights: list, choice: str):
    """
    :arg knights - list of all of the knight objects
    :arg choice - string passed for the sake of being able to reuse this function - choices which function to call after a valid selection is made.
    """

    checker = True
    while checker:
        print("Pick a knight: \n")
        # This creates a list for the number to select a knight from the knight number inside of the knights dictionary
        for knight in knights:
            print(str(knight.knight_number) + ": " + knight.name)

        try:
            selection = (int(input("\nSelect the Knights number: \n")) - 1)
            # Choice is set in menu and dictates with function the knights selected will be passed to
            if choice == "change":
                change_data(knights[selection])
                checker = False

            elif choice == "train":
                train_knight(knights[selection])
                checker = False

            elif choice == "duel":
                return knights[selection]

        # Catches if they dont select a valid knight
        except:
            print("--- Try again ---\n")
            
            

# Call this to increase one of the knights stats by 1, randint is used to decided which stat is increased.      
def train_knight(knight: Knight):
    """ :arg knight - instance of the knight class passed to allow for changes to the instances data"""

    # Uses randint to decide which stat gets increased.
    stat_picker = random.randint(1, 3)

    if stat_picker == 1:
        knight.strength += 1
        stat = "strength"

    elif stat_picker == 2:
        knight.speed += 1
        stat = "speed"

    else:
        knight.health += 1
        stat = "health"

    print("The knight " + knight.name + " trains very hard and gains 1 " + stat + "\n")

# Call this to get two knights to duel, which knight attacks first is decided by the knights speed stat and then they deal damage using the deal_damage funection and ends when one of the knights 
# health reaches 0 which is checked with the health_checker function

def duel_knights(knight_one: Knight, knight_two: Knight):
    """
    :arg knight_one - first picked instance of the knight class, used to get attributes for the duel function
    :arg knight_two - second picked instance of the knight class, again used for the attributes for the duel function
    """

    # Checks if the user has selected the same knight twice and returns them to the menu if they have.
    if knight_one.knight_number == knight_two.knight_number:
        print("The knight cannot duel themselves, try again \n")
        menu()
        return
    
    print("The duel between " + knight_one.name + " and " + knight_two.name + " will now begin: \n")
    # Sets the knights health to a new variable that can be changed without affecting the Knights actual health
    knight_one_health = knight_one.health
    knight_two_health = knight_two.health
    loop_checker = True
    while loop_checker == True:

        # Checks if the first knight has the better speed then the second knight then runs the attack round with that knight attacking first
        if knight_one.speed >= knight_two.speed:
            # Uses the deal_damage funection to remove health from the new knights health variable
            knight_two_health -= deal_damage("one", knight_one, knight_two)

            # Checks if a knight has been defeated
            if health_checker(knight_two_health):
                print(knight_two.name + " has been defeated! What a match!")
                loop_checker = False

            else:
                # Knight with the lower speed attacks, using the same functions as above.
                knight_one_health -= deal_damage("two", knight_one, knight_two)

                if health_checker(knight_one_health):
                    print(knight_one.name + " has been defeated! What a match!")
                    loop_checker = False

        # If the first knight does not have better speed it runs this so knight two attacks first
        else:
            knight_one_health -= deal_damage("two", knight_one, knight_two)

            if health_checker(knight_one_health):
                print(knight_one.name + " has been defeated! What a match!")
                loop_checker = False
            
            else:
                knight_two_health -= deal_damage("one", knight_one, knight_two)
                if health_checker(knight_two_health):
                    print(knight_two.name + " has been defeated! What a match!")
                    loop_checker = False

        input("Press enter for the next round. \n")
    menu()

# Call this to have one knight deal damage to the other, returns the damage done as an int
def deal_damage(attacking_knight: str, knight_one: Knight, knight_two: Knight) -> int:
    """
    :arg attack_knight: string to be used in an if statment to decide which knight is dealing damage
    :arg knight_one: instance of the knight class, used for getting hold of attributes
    :arg knight_two: instance of the knight claass, again used for getting hold of attributes
    :return - returns an int of the calculated damage, used to decide which knight wins the duel
    """

    if attacking_knight == "one":
        damage = random.randint(1, 10) + knight_one.strength
        print("Knight " + knight_one.name + " gets in a with there " + knight_one.weapon + "blow dealing " + str(damage) + "\n")
        return damage

    else:
        damage = random.randint(1, 10) + knight_two.strength
        print("Knight " + knight_two.name + " gets in a hit with there " + knight_two.weapon + " for " + str(damage) + "\n")
        return damage

# Call to make sure the knights health remaining health is above 0
def health_checker(health: int) -> bool:
    """
    :arg health - an int repressing the health of the knight being checked, it is used to decide when a knight has lost the duel
    :return - returns a bool, with true being the knight has lost and false if they still have health left.
    """

    if health <= 0:
        return True
    return False


# This is the menu and we make our selections here
def menu():
    # Print the display here
    print("What would you like to do? \n")
    print("0: View all")
    print("1: Create a knight")
    print("2: Update a knight")
    print("3: Training ground")
    print("4: Duel 2 knights")
    print("5: Exit \n")

    # Allows a selection to be tested
    try:
        # Takes the users selection option and checks it agasint the menu
        select = int(input("Selection number: "))
        print() # creates a blank space

        # Checks to see if there is atleast one knight then prints out all knights if there is
        if select == 0:
            if int(len(knights)) == 0:
                print("Oh no you have no knights, better make some and try again \n")
                menu()

            else: 
                # Goes through every item in the knights list and prints all the data from each knight.
                print("--- All your Knights! ---\n")
                for knight in knights: 
                    knight.print_self()
                    print()
                menu()

        # Calls the create a knight function and prints out the created knight.
        elif select == 1:
            create_knight(knights)
            menu()

        # Checks to see if there is atleast one knight then calls select_knight function if there is with the parameter change.
        elif select == 2:
            # Checks if the knights list is empty or not
            if int(len(knights)) == 0:
                print("You need to create a knight first \n")
                menu()
                
            else:
                select_knight(knights, "change")
                menu()

        # Checks if there is atleast one knight then calls the select_knight function with train.
        elif select == 3:

            if int(len(knights)) == 0:
                print("You need to create a knight first \n")
                menu()

            else: 
                select_knight(knights, "train")
                menu()

        # Checks if there are atleast 2 knights then calls the select_knight function with duel
        elif select == 4:

                if int(len(knights)) <= 1:
                    print("You need at least 2 knights to duel \n")
                    menu()

                first_knight = select_knight(knights, "duel")
                second_knight = select_knight(knights, "duel")
                duel_knights(first_knight, second_knight)

        # Posts a goodbye message then should end the program
        elif select == 5:
            print("Goodbye, and thanks for playing!")
            

        # When the user doesnt enter a correct number   
        else:
            print("--- Try again! ---\n")
            menu()

        # When the user doesnt enter a number
    except:
        print("--- Try again! ---\n")
        menu()
    
# Setting the scene
knights = []

# Run the program
menu()