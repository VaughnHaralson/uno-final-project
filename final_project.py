import random

def build_deck(): #Shyam
    color = ('RED','GREEN','BLUE','YELLOW')
    number = ('0','1','1','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','Skip','Skip','Reverse','Reverse','Draw 2','Draw 2')
    Wild = ('Draw 4','Draw 4','Draw 4','Draw 4','Wild','Wild','Wild','Wild')
    deck = []
    for x in color:
        for y in number:
            cards = x + ' ' + y
            deck.append(cards)
    for x in Wild:
        deck.append(x)
    return deck

def initialize_deck(deck): #Shyam
    deck = build_deck()
    computer_deck= []
    player_deck = []
    for x in range(8):
        computer_deck.append(random.choice(deck))
    for y in range(8):
        player_deck.append(random.choice(deck))
    return [computer_deck, player_deck]
print("Computer Deck:")
print(initialize_deck(build_deck())[0])
print("Player Deck:")
print(initialize_deck(build_deck())[1])
def skip(number_1,turn):
  if (number_1 == "Skip"): #Kalidas
    if(turn%2==0):
      turn = turn
    else:
      turn = 1
    return turn
  else:
    return ""
def valid_move(chosencard,topcard): #Vaughn
  if chosencard(0)==topcard(0) or chosencard(1)==topcard(1):
    return True
  else:
    return False
def draw_card(computer_deck,player_Deck):
def playerturn(player_deck,topcard): #Vaughn
  x=int(input("Select a card: "))-1
  chosencard=player_deck(x)
  if valid_move(chosencard, topcard)==True:
    topcard=chosencard
    turn=turn+1
    print("Top Card is ", topcard)
  else:
    print("Invalid Move.")
    return playerturn(player_deck,topcard)
def computerturn(computer_deck, topcard):
  x=1
  for card in computer_deck:
    if valid_move(card, topcard)==True:
      topcard=card
      x=x-1
      turn=turn+1
      print("Top Card is ",topcard)
    else:
      if x>0:
        continue
      else:
        draw(computer_deck)
        return computerturn(computer_deck, topcard)
#GAME PROCESS SUDO CODE - Kalidas
#initalize the deck
#pick out a random card from the main deck
#computer should play first
#check if a valid move exists
#if the computer cannot play it should draw a card until it plays
#once it plays the top card should update from the previous card to the new card
#then it should display the user's deck and ask for an input
#Once the index of the input is entered, it checks if the move is valid
#if it is valid it updates the top card from the previous card to the new card
#otherwise it says invalid move and asks the user again
#the game keeps going until one person wins 
