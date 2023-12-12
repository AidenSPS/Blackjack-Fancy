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
    pass

def pickRandomCard():
    ##This function takes a random integer and selects a card id from "shoe.txt".
    ##@params: None
    ##@returns: CARD_ID
    shoe = open("shoe.txt", "r")
    #randomNumber = random.randint(1,52)
    randomNumber = 1
    shoeLineNumber = 1
    currentCard = shoe.readline()
    
    if randomNumber == shoeLineNumber:
        currentCard = "2"
        CARD_ID = currentCard
        return CARD_ID
    
    while shoeLineNumber != randomNumber:
        currentCard = shoe.readline()
        shoeLineNumber += 1
    
    CARD_ID = currentCard
    discardCard()
    return CARD_ID

def discardCard():
    discard = ("discard.txt", "a")
    CARD_ID = pickRandomCard()
    discard.append(CARD_ID)
    discard.close()
    
def userStart():
    ##This function takes the first cards for the user to be added up to value to be displayed to the user
    ##@params: None
    ##@returns: cardValue
    CARD_ID = pickRandomCard()
    CARD_ID = int(CARD_ID)
    aceNumericFlag = None

    clubs = 2
    diamonds = 102
    hearts = 202
    spades = 302

    for i in range(1,13,1):
        if CARD_ID != clubs or CARD_ID != diamonds or CARD_ID != hearts or CARD_ID != spades:
            print("Moving onto the next number of cards")
            clubs += 1
            diamonds += 1
            hearts += 1
            spades += 1
        if CARD_ID == clubs or CARD_ID == diamonds or CARD_ID == hearts or CARD_ID == spades:
            if CARD_ID == clubs:
                cardValue = clubs
                break
            elif CARD_ID == diamonds:
                cardValue = clubs
                break
            elif CARD_ID == hearts:
                cardValue = clubs
                break
            elif CARD_ID == spades:
                cardValue = clubs
                break
            
            
    if clubs == 11 or clubs == 12 or clubs == 13:
        cardValue = 10
        return cardValue
        
    if clubs == 14:
        cardValue = int(input("You have an Ace! Would you want it to be a 1 or an 11?: "))
        if cardValue != 1 and cardValue != 11:
            aceNumericFlag = False
        elif cardValue == 1 or cardValue == 11:
            return cardValue
        else:
            aceNumericFlag = False
    while aceNumericFlag == False:
        cardValue = int(input("INVALID RESPONSE: Please check your answer. Would you like your ace to be a 1 or an 11?: "))
        if cardValue == 1 or cardValue == 11:
            aceNumericFlag = True
    
    return cardValue









































def main():
    fillShoe()
    pickRandomCard()




    
main()
