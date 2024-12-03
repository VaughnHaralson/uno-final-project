import random, pygame as game, time
##
colors = ['Red', 'Green', 'Blue', 'Yellow']
values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Skip', 'Reverse', 'Draw 2']
wild_cards = ('Wild Draw 4', 'Wild')

def buildDeck():
    deck = []
    for x in colors:
        for y in values:
            cardVal = f"{x} {y}"
            deck.append(cardVal)
            if y != 0:
                deck.append(cardVal)
    for _ in range(4):
        deck.append(wild_cards[0])
        deck.append(wild_cards[1])
    return deck

def shuffleDeck(deck):
    for card_pos in range(len(deck)):
        rand_pos = random.randint(0, len(deck) - 1)
        deck[card_pos], deck[rand_pos] = deck[rand_pos], deck[card_pos]
    return deck

def drawCards(numCards):
    cardsDrawn = []
    for _ in range(numCards):
        if unoDeck: 
            cardsDrawn.append(unoDeck.pop(0))
        else:
            deckempty=True
    return cardsDrawn

def canPlay(color, value, playerHand):
    for card in playerHand:
        if 'Wild' in card:
            return True
        elif color in card or value in card:
            return True
    return False

# def showHand(player, playerHand):
#     print(f"Player {player + 1}")
#     print("Your Hand:")
#     print("---------")
#     for idx, card in enumerate(playerHand, start=1):
#         print(f"{idx}: {card}")
#     print("")
#Do we still need this?^^

#{######} [Functions] |V\/^vV^Vv^\/V| [End] {######}#
enter = False
playing = True
playerquery = True
x=1920
y=1080
game.init()
game.font.init()
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,128)
screen=game.display.set_mode((x,y))
clock=game.time.Clock
game.display.set_caption('Uno! - Kalidas, Shyam, Vaughn')
welcomefont = game.font.SysFont('Comic Sans MS', 30)
constantinput=''

while playing == True:
    screen.fill(black)

    # get player number (loop)

    while playerquery == True:
        screen.fill(black)
        unoDeck = buildDeck()
        unoDeck = shuffleDeck(unoDeck)
        discards = []
        players = []
        welcomesplash=welcomefont.render("How many players want to play?", False, green)
        splash2=welcomefont.render("(Enter a number between 2 to 4):", False, green)
        screen.blit(welcomesplash, ((x/2)-300,y/2))
        screen.blit(splash2, ((x/2)-300, (y/2)+50))

        for event in game.event.get():
            if event.type == game.QUIT:
                game.quit()
                raise SystemExit
            elif event.type == game.KEYDOWN:
                if event.key == game.K_2:
                    numPlayers=2
                    playerquery=False
                    continue
                elif event.key == game.K_3:
                    numPlayers=3
                    playerquery=False
                    continue
                elif event.key == game.K_4:
                    numPlayers=4
                    playerquery=False
                    continue
                else:
                    screen.fill(white)
                    welcomesplash=welcomefont.render("Invalid input!!", False, black)
                    screen.blit(welcomesplash, ((x/2)-280, y/2-100))
                    time.sleep(1)
                    
        game.display.update()
    
    #setup the game (only once)

    if playerquery==False:
        for _ in range(numPlayers):
            players.append(drawCards(5))
        discards.append(unoDeck.pop(0))
        splitCard = discards[-1].split(" ", 1)
        currentColor = splitCard[0]
        cardVal = splitCard[1] if len(splitCard) > 1 else "Any"
        playerTurn = 0
        playerDirection = 1
        playerquery=None
                
    #render discard pile, player n's deck (loop)

    # print(f"\nCard on top of discard pile: {discards[-1]}")
    # showHand(playerTurn, players[playerTurn])

    #start gameplay (loop)

    if canPlay(currentColor, cardVal, players[playerTurn]):
        #Render 
        cardChosen = int(input("Enter the index of the card you want to play: "))
        #
        if cardChosen < 1 or cardChosen > len(players[playerTurn]) or not canPlay(currentColor, cardVal, [players[playerTurn][cardChosen - 1]]):

            cardChosen = int(input("Invalid input. Please enter the index of a valid card: "))

        playedCard = players[playerTurn].pop(cardChosen - 1)

        print(f"You played {playedCard}")

        discards.append(playedCard)
        splitCard = playedCard.split(" ", 1)
        currentColor = splitCard[0]
        cardVal = splitCard[1] if len(splitCard) > 1 else "Any"

        if "Wild" in currentColor:
            for idx, color in enumerate(colors, start=1):
                print(f"{idx}: {color}")
            newColor = int(input("Choose a new color (1:Red, 2:Green, 3:Blue, 4:Yellow): "))
            while newColor < 1 or newColor > 4:
                newColor = int(input("Invalid choice. Choose a color (1:Red, 2:Green, 3:Blue, 4:Yellow): "))
            currentColor = colors[newColor - 1]

        if cardVal == "Reverse":
            playerDirection *= -1
        elif cardVal == "Skip":
            playerTurn += playerDirection
        elif cardVal == "Draw 2":
            nextPlayer = (playerTurn + playerDirection) % numPlayers
            players[nextPlayer] += drawCards(2)

        elif cardVal == "Draw 4":
            nextPlayer = (playerTurn + playerDirection) % numPlayers
            players[nextPlayer] += drawCards(4)
            for idx, color in enumerate(colors, start=1):
                print(f"{idx}: {color}")
            newColor = int(input("Choose a new color (1:Red, 2:Green, 3:Blue, 4:Yellow): "))
            while newColor < 1 or newColor > 4:
                newColor = int(input("Invalid choice. Choose a color (1:Red, 2:Green, 3:Blue, 4:Yellow): "))
            currentColor = colors[newColor - 1]
            playerTurn += playerDirection

        if not players[playerTurn]:
            print(f"Player {playerTurn + 1} wins!")
            playing = False

    else:
        print("You cannot play any card. Drawing a card...")
        players[playerTurn] += drawCards(1)

    playerTurn += playerDirection
    if playerTurn >= numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers - 1

    for event in game.event.get():
            if event.type == game.QUIT:
                game.quit()
                raise SystemExit
            elif event.type == game.KEYDOWN:
                if event.key == game.K_0:
                    constantinput+='0'
                    continue
                elif event.key == game.K_1:
                    constantinput+='1'
                    continue
                elif event.key == game.K_2:
                    constantinput+='2'
                    continue
                elif event.key == game.K_3:
                    constantinput+='3'
                    continue
                elif event.key == game.K_4:
                    constantinput+='4'
                    continue
                elif event.key == game.K_5:
                    constantinput+='5'
                    continue
                elif event.key == game.K_6:
                    constantinput+='6'
                    continue
                elif event.key == game.K_7:
                    constantinput+='7'
                    continue
                elif event.key == game.K_8:
                    constantinput+='8'
                    continue
                elif event.key == game.K_9:
                    constantinput+='9'
                    continue
                elif event.key == game.K_KP_ENTER:
                    enter=True
                    cardChosen=constantinput
                    constantinput=''
                    continue

    game.display.update()




