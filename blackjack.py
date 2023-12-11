### Program: Blackjack

### Language: Python 3.11.5

### Description: Plays a game of Blackjack (vs Computer) and maintains files (discard and shoe (as text files))
###   and reads, appends, and writes to it at varying times.
###   User draws two cards, can only hit and stand, and whoever wins, gets the difference of score in points.
###   and when the total score is reached (set by user), the user can elect to play again and if so, cleans the discard, resets the shoe and the game starts again. 

### School: Husson University
### Course: IT261
### Author: Aiden Kusmierczak

###Change Log:
###Date:                  Description:

###12-01-2023:            "blackjack.py" is created.

###12-01-2023:            "shoe.txt" is created. Must be imported to Google Drive for MacIntosh Delivery

###12-01-2023:            Prioritize Global Scope and basic functions. (playAgain(), main(), userHit(), userStand(), cpuHit(), cpuStand(), determineWinner(), playAgain()

###12-01-2023:            To keep track of file directory through the OS's, Win11: D:\Seagate 4TB Drive\~~PythonFiles~~\Blackjack

###12-01-2023:            On MAC, is located at (McIntosh\Desktop\Aiden Kusmierczak IT261\Blackjack

###12-03-2023:            File "blackjack.py" and "shoe.txt" are imported to McIntosh Computer (Keep Updating if you work on Windows)

###12-06-2023:            Function "fillShoe()" is finalized. Working as intended

##12-08-2023:             Modified function "fillShoe()" to meet integer parameters required for function "pickRandomCard()"

##12-08-2023:             Function "pickRandomCard()" is initialized

##12-11-2023:             File position changed to randomNumber. CARD_ID is not working as intended. See comments about it for more

##12-11-2023:             Files "blackjack.py" and "shoe.txt" are uploaded to GitHub for ease of access. 

##Imports
import random

##Global Scope
bustNumber = 21 #Integer
#maxScore = int(input("How many points do you want to play to? ")) #Converted String --> Integer
totalCards = 52 #Integer
cpuPoints = None #Integer
userPoints = None #Integer
playAgain = None #Boolean
#cardString = [##Fill this list with the strings as such "AC", "AD", "AH", "AS"...]

##Function Declaration

def fillShoe():
    ##This function opens "shoe.txt" for writing and initialized the deuce of (suits). Then adds the other cards in order and ordered by suits.
    ##When done, closes "shoe.txt"
    ##@params: None
    ##@returns: None
    shoe = open("shoe.txt", "w")
    startClub = 2 ##Deuce of Clubs
    startDmd = 102 ##Deuce of Diamonds
    startHeart = 202 ##Deuce of Hearts
    startSpade = 302 ##Deuce of Spades
    
    for clubs in range(2,15,1): #For the club cards ID's only
        shoe.write(str(clubs) + "\n")
        
    for diamonds in range(102,115,1): #For the diamond cards ID's only
        shoe.write(str(diamonds) + "\n")
    
    for hearts in range(202,215,1): #For the heart cards ID's only
        shoe.write(str(hearts) + "\n")

    for spades in range(302,315,1): #For the spade cards ID's only
        shoe.write(str(spades) + "\n")
    shoe.close()

def pickRandomCard():
    ##This function takes a random integer and selects a card id from "shoe.txt".
    ##@params: None
    ##@returns: CARD_ID
    shoe = open("shoe.txt", "r")
    randomNumber = random.randint(1,52)
    print(randomNumber) #TEST
    print(shoe.seek(randomNumber)) ##TEST (This code works as intended)
    
    CARD_ID = shoe.readline() ##This code breaks. It returns a random line from the file not associated from the random number.
    ##Ex: RandomNumber = 1, shoe.readline(), CARD_ID = 12 (2 is expected)
    
    print(CARD_ID)

    
    ##You need to find a way to read from the discard to tell the program that the
    ##Number you are at is discarded or eliminated from play and to get the next
    ##Card in the shoe. 
        
def userHit():
    ##This function is a response to the input "hit". Will draw a random card from the shoe by calling pickRandomCard()
    ##@params: response = ("hit")
    ##@returns: None
    pickRandomCard()

def cpuHit():
    ##This function is a response to the input "stand". Will draw a random card from the shoe by calling pickRandomCard()
    ##@params: None
    ##@returns: None


def userStand():
    ##This function calls cpuHit which calls pickRandomCard and will validate the points to the computer.
    ##@params: response = ("stand")
    ##@returns: None
    cpuHit()

def main():
    fillShoe()
    pickRandomCard()
main()
