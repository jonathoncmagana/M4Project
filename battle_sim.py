"""
    Course: CS5980
    Summer 2023
    Battle Simulator 3000
    Name: FIXME
    Created: FIXME
"""


"""
 BattleSim Driver for Battle Simulator 3000
 You may need to set the Python interpreter if you have an error along the top. Choose local, and it should find it
"""

"""
     # we need to create a Ten-sided die to be used for checking initiative
"""
def main():
    # Local variables
    # Include any variable that will need to be accessed throughout the program here

    # sentinel value for the game loop
    play = True
    # String used to determine the winner of the epic battle
    victor = ""
    # game loop
    keep_playing = True

    while keep_playing:
        # print the introduction and rules


        # initialize game
        # Initialize the Warrior and Mugwump classes, set the current victor to "none"
        warrior = None
        mugwump = None
        victor = "none"

        # while neither combatant has lost all of their hit points, report status and battle!
        while victor == "none":
            report(warrior, mugwump);
            victor = battle(warrior, mugwump)

        # declare the winner


        # ask to play again


    # Thank the user for playing your game



"""
   This method displays the introduction to the game and gives a description of the rules.
 """
def intro():
    # Write a suitable introduction to your game
    pass


"""
   This method handles the battle logic for the game.
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
   @return The name of the victor, or "none", if the battle is still raging on
 """
def battle(warrior, mugwump):
    # determine who attacks first (Roll! For! Initiative!) and store the result

    # attack code
    # If the Warrior attacks first

    # Warrior attacks and assigns the resulting damage to the mugwump

    # Check if the Mugwump has been defeated
    # If not, Mugwump attacks!

    # Otherwise, the Warrior wins!

    # Otherwise the Mugwump is first
    # see above

    # If neither combatant is defeated, the battle rages on!
    return None


"""
   This method reports the status of the combatants
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
 """
def report(warrior, mugwump):
    # TODO
    pass


"""
   This method asks the user what attack type they want to use and returns the result
   @return 1 for sword, 2 for shield
 """
def attackChoice() -> int:
    # TODO
    return -1


"""
   Determines which combatant attacks first and returns the result. In the case of a tie,
   re-roll.
   @return 1 if the warrior goes first, 2 if the mugwump goes first
 """
def initiative() -> int:
    # roll for initiative for both combatants
    # until one initiative is greater than the other
    return -1


"""
   This method declares the victor of the epic battle
   @param victor the name of the victor of the epic battle
 """
def victory(victor):
    # TODO
    pass


"""
   This method asks the user if they would like to play again
   @param in Scanner
   @return true if yes, false otherwise
 """
def playAgain() -> bool:
    # TODO
    return False

if __name__ == "__main__":
    main()