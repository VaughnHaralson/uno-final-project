import random, pygame as game, time, os
##
colors = ['Red', 'Green', 'Blue', 'Yellow']
values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Skip', 'Reverse', 'Draw 2']
wild_cards = ('Wild Draw 4', 'Wild')

game.init()
game.font.init()
enter = False
playing = False
playerquery = True
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = game.display.Info()
width, height = info.current_w, info.current_h
game.init()
game.font.init()
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,128)
screen = game.display.set_mode((width, height))
clock=game.time.Clock
game.display.set_caption('Uno! - Kalidas, Shyam, Vaughn')
welcomefont = game.font.SysFont('Comic Sans MS', 30)
playfont = game.font.SysFont('Comic Sans MS', 20)
constantinput=''
chosen=None
invalid_time=-1
test=game.image.load("C:/Users/ASUS/Desktop/Computer Science/images/uno.png").convert()

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

def showHand(player, playerHand):
    showhand=[f"Player {player + 1}","Your Hand:","---------"]
    for idx, card in enumerate(playerHand, start=1):
        showhand.append(f"{idx}: {card}")
    return showhand

def wait():
    while True:
        i=0
        screen.fill(black)
        colorquery=["Choose a new color:"]
        for idx, color in enumerate(colors, start=1):
            colorquery.append(f"{idx}: {color}")
        for things in colorquery:
            temptext=playfont.render(things, False, green)
            screen.blit(temptext, (width, (height/10)+i))
            i+=20
        game.display.update()

        for event in game.event.get():
            if event.type == game.QUIT:
                game.quit()
                raise SystemExit
            elif event.type == game.KEYDOWN and (event.key == game.K_1 or event.key == game.K_2 or event.key == game.K_3 or event.key == game.K_4 or event.key == game.K_ESCAPE):
                if event.key == game.K_1:
                    return 1
                elif event.key == game.K_2:
                    return 2
                elif event.key == game.K_3:
                    return 3
                elif event.key == game.K_4:
                    return 4
                elif event.key == game.K_ESCAPE:
                    game.quit()
                    raise SystemExit
            



#{######} [Functions] |V\/^vV^Vv^\/V| [End] {######}#

unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
discards = []
players = []

while playerquery == True:
    screen.fill(black)
    welcomesplash=welcomefont.render("How many players want to play?", False, green)
    splash2=welcomefont.render("(Enter a number between 2 to 4 and press 'Enter'):", False, green)
    quittext=welcomefont.render("Press 'Esc' to quit", False, blue)
    inputsplash=welcomefont.render(f"{constantinput}", False, green)
    screen.blit(welcomesplash, ((width/2)-300,height/2))
    screen.blit(splash2, ((width/2)-300, (height/2)+50))
    screen.blit(quittext,(width/10,height-100))
    screen.blit(inputsplash, (width/2, height/2+300))

    if chosen==2 or chosen==3 or chosen==4:
        numPlayers=chosen
        for _ in range(numPlayers):
            players.append(drawCards(5))
        discards.append(unoDeck.pop(0))
        splitCard = discards[-1].split(" ", 1)
        currentColor = splitCard[0]
        cardVal = splitCard[1] if len(splitCard) > 1 else "Any"
        playerTurn = 0
        playerDirection = 1
        chosen=None
        enter=False
        playerquery=False
    elif chosen is not None and (chosen not in [2, 3, 4]):
        currenttime=game.time.get_ticks()
        while game.time.get_ticks()<currenttime+1000:
            screen.fill(white) 
            welcomesplash = welcomefont.render("Invalid input!!", False, black)
            screen.blit(welcomesplash, ((width / 2) - 280, height / 2 - 100))
            game.display.update()
        chosen=None
        enter = False

    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            raise SystemExit
        elif event.type == game.KEYDOWN:
            if event.key == game.K_0:
                constantinput+='0'
            elif event.key == game.K_1:
                constantinput+='1'
            elif event.key == game.K_2:
                constantinput+='2'
            elif event.key == game.K_3:
                constantinput+='3'
            elif event.key == game.K_4:
                constantinput+='4'
            elif event.key == game.K_5:
                constantinput+='5'
            elif event.key == game.K_6:
                constantinput+='6'
            elif event.key == game.K_7:
                constantinput+='7'
            elif event.key == game.K_8:
                constantinput+='8'
            elif event.key == game.K_9:
                constantinput+='9'
            elif event.key == game.K_RETURN:
                if constantinput=='':
                    pass
                else:
                    enter=True
                    chosen=int(constantinput)
                    constantinput=''
            elif event.key == game.K_ESCAPE:
                game.quit()
                raise SystemExit
            
    game.display.update()

playing=True

while playing == True:
    screen.fill(black)
    currenttime=game.time.get_ticks()
    displaytime=0
    
    handtext=showHand(playerTurn, players[playerTurn])
    i=0
    for things in handtext:
        temptext=playfont.render(things, False, green)
        screen.blit(temptext, (width/10, (height/10)+i))
        i+=20
    i=0
    discardtext = playfont.render(f"Discard Pile:", False, green)
    topdiscard = playfont.render(f"{discards[-1]}", False, green)
    inputsplash=playfont.render(f"{constantinput}", False, green)
    screen.blit(discardtext, ((width/2-150),height/2))
    screen.blit(topdiscard, (width/2-150, height/2+40))
    screen.blit(inputsplash, (width/2, height/2+300))

    #start gameplay (loop)"
    if enter == True:
        if canPlay(currentColor, cardVal, players[playerTurn]):
            if chosen <= len(players[playerTurn]) and canPlay(currentColor, cardVal, [players[playerTurn][chosen - 1]]):
                currentplayerindex=playerTurn
                playedCard = players[playerTurn].pop(chosen - 1)

                #screen.blit(test, (width/2, height/2)) #display played card

                discards.append(playedCard)
                splitCard = playedCard.split(" ", 1)
                currentColor = splitCard[0]
                cardVal = splitCard[1] if len(splitCard) > 1 else "Any"

                if "Wild" in currentColor:

                    newcolor=wait()
                    currentColor = colors[newcolor - 1]

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

                    colorquery=["Choose a new color:"]
                    for idx, color in enumerate(colors, start=1):
                        colorquery.append(f"{idx}: {color}")
                    for things in colorquery:
                        temptext=playfont.render(things, False, green)
                        screen.blit(temptext, (width, (height/10)+i))
                        i+=20
                    game.display.update()
                    newcolor=wait()

                    currentColor = colors[newcolor - 1]
                    playerTurn += playerDirection

                if players[currentplayerindex]==[]:
                    print(f"Player {currentplayerindex + 1} wins!")
                    playing = False
                
                playerTurn += playerDirection
                if playerTurn >= numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers - 1
            else:
                currenttime=game.time.get_ticks()
                while game.time.get_ticks()<currenttime+1000:
                    screen.fill(white) 
                    welcomesplash = welcomefont.render("Invalid input!!", False, black)
                    screen.blit(welcomesplash, ((width / 2) - 280, height / 2 - 100))
                    game.display.update()
                chosen=None
        enter=False

    elif not canPlay(currentColor, cardVal, players[playerTurn]):
        currenttime=game.time.get_ticks()
        while game.time.get_ticks()<currenttime+500:
            screen.fill(white) 
            nocard = playfont.render("You cannot play any card. Drawing a card...", False, black)
            screen.blit(nocard, ((width / 2) - 280, height / 2 - 100))
            game.display.update()
        players[playerTurn] += drawCards(1)
        chosen=None
        enter=False

    

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
                elif event.key == game.K_RETURN:
                    if constantinput=='':
                        pass
                    else:
                        enter=True
                        chosen=int(constantinput)
                        constantinput=''
                elif event.key == game.K_ESCAPE:
                    game.quit()
                    raise SystemExit
    game.display.update()




