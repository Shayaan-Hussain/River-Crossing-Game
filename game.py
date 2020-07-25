import pygame as pg
import time
from configuration import *
from pygame import mixer

# Initializing pygame
pg.init()
mixer.init()
screen = pg.display.set_mode((800, 655))
pg.display.set_caption('River Crossing')
pg.display.set_icon(icon)
mixer.music.load('assets/music.mp3')
mixer.music.play()

# This function will convert time to seconds
def timetosec(timer):
    h = int(timer[11:13])
    m = int(timer[14:16])
    s = int(timer[17:19])
    h *= 60 * 60
    m *= 60
    return s + h + m

# This function will show the main game background
def displaygamebg(score1, score2):
    scorep1disp = font1.render(f"Score P1: {score1}", True, (0, 0, 0))
    scorep2disp = font1.render(f"Score P2: {score2}", True, (0, 0, 0))
    rounddisp = font3.render(f"Round {roundplay}", True, (0, 0, 0))
    activeplayer = font2.render("Active", True, (0, 0, 0))
    time_elpassed = timetosec(end_time) - timetosec(starting_time)
    timedisp = font2.render(f"Time : {time_elpassed}", True, (0, 0, 0))
    screen.blit(seabg, (0, 0))
    for i in grassY:
        screen.blit(grass, (0, i))
    for i in brownY:
        screen.blit(brown, (0, i))
    if player1disp:
        screen.blit(activeplayer, (10, 40))
    else:
        screen.blit(activeplayer, (615, 40))
    screen.blit(timedisp, (320, 45))
    screen.blit(scorep1disp, (10, 10))
    screen.blit(scorep2disp, (615, 10))
    screen.blit(rounddisp, (305, 5))

# This function will check player collission with rocks
def checkrock(rockX, rockY, playerX, playerY):
    if playerY - rockY == 15:
        if rockX - playerX < 22 and rockX - playerX > -47:
            return True
        else:
            return False
    else:
        return False

# This function will check player collission with ships
def checkship(shipX, shipY, playerX, playerY):
    if playerY - shipY == 12:
        if shipX - playerX < 15 and shipX - playerX > -200:
            return True
        else:
            return False
    else:
        return False

# This function will check player collission with boats
def checkboat(boatX, boatY, playerX, playerY):
    if playerY - boatY == 12:
        if boatX - playerX < 20 and boatX - playerX > -45:
            return True
        else:
            return False
    else:
        return False

# This function displays Game Over screen
def gameoverdisp(score1, score2):
    gameovertext = font3.render("Game Over", True, (0, 0, 0))
    player1score = font2.render(f"Player 1: {score1}", True, (0, 0, 255))
    player2score = font2.render(f"Player 2: {score2}", True, (255, 0, 0))
    if score1 > score2:
        win = font4.render("Player 1 Wins!", True, (0, 255, 0))
    elif score2 > score1:
        win = font4.render("Player 2 Wins!", True, (0, 255, 0))
    else:
        win = font4.render("Its a Draw!", True, (0, 255, 0))
    screen.blit(gameover, (0, 0))
    screen.blit(gameovertext, (280, 190))
    screen.blit(player1score, (130, 400))
    screen.blit(player2score, (470, 550))
    screen.blit(win, (270, 460))
    
# This function calculates scores for player 1
def scorep1calc():
    global scorep1, row, rowcross, player1disp

    # Checking number of rows passed by player
    for i in range(1, 11):
        if player1Y == rowY[i]:
            row[i] = 1
    
    # Checking if player is crossing the road for first time and add score
    for i in range(1, 11):
        if row[i] and not rowcross[i]:
            scoretemp = 0
            for j in rockY:
                if j == rowY[i - 1] - 15:
                    scoretemp += 5
            for j in shipY:
                if j == rowY[i - 1] - 12:
                    scoretemp += 10
            for j in boatY:
                if j == rowY[i - 1] - 12:
                    scoretemp += 10
            scorep1 += scoretemp
            rowcross[i] = 1

# This function calculates scores for player 2
def scorep2calc():
    global scorep2, row, rowcross, player2disp
    # Checking number of rows passed by player
    for i in range(9, -1, -1):
        if player2Y == rowY[i]:
            row[i] = 1
    
    # Checking if player is crossing the road for first time and add score
    for i in range(9, -1, -1):
        if row[i] and not rowcross[i]:
            scoretemp = 0
            for j in rockY:
                if j == rowY[i + 1] - 15:
                    scoretemp += 5
            for j in shipY:
                if j == rowY[i + 1] - 12:
                    scoretemp += 10
            for j in boatY:
                if j == rowY[i + 1] - 12:
                    scoretemp += 10
            scorep2 += scoretemp
            rowcross[i] = 1

# This function resets player 1 position and starts player 2 game
def player1reset():
    global player1X, player1Y, player1ch, player2ch
    global p1play, player1disp, player2disp, row, rowcross
    player1X = 380
    player1Y = 610
    player1ch = 0
    player2ch = 0
    p1play += 1
    player1disp = False
    player2disp = True
    for i in range(0, 11):
        row[i] = 0
        rowcross[i] = 0

# This function resets player 2 position and starts player 1 game
def player2reset():
    global player2X, player2Y, player1ch, player2ch
    global p2play, player1disp, player2disp, row, rowcross
    player2X = 380
    player2Y = 80
    player1ch = 0
    player2ch = 0
    p2play += 1
    player2disp = False
    player1disp = True
    for i in range(0, 11):
        row[i] = 0
        rowcross[i] = 0

#This function spawns more rocks
def rockspawn():
    global rockY,rockX
    temp = randint(0, 10)
    temp = rockY[temp]
    rockY.append(temp)
    while True:
        rock = randint(0, 730)
        if temp == 595 or temp == 65:
            rock = randint(0, 730)
            if rock > 450 or rock < 310:
                rockX.append(rock)
                break
        else:
            rockX.append(rock)
            break

# Loop to refresh the screen
while gameloop:
    
    # Main screen background colour (R,G,B)
    screen.fill((0, 0, 0))
    
    # This will start the game after user clicks play button
    if game_start:
        
        # This will execute is game is over
        if gameovervar:
            
            gameoverdisp(sum(p1scorelist), sum(p2scorelist))
            
            # This checks if play again or continue button is pressed
            for event in pg.event.get():
                
                if event.type == pg.QUIT:
                    gameloop = False
                    
                if event.type == pg.MOUSEBUTTONDOWN:
                    
                    if 10 <= mouse[0] <= 150 and 10 <= mouse[1] <= 150:
                        for i in range(0, len(p1scorelist)):
                            p1scorelist.pop()
                        for i in range(0, len(p2scorelist)):
                            p2scorelist.pop()
                        while len(rockX) > 10:
                            rockX.pop()
                            rockY.pop()
                        game_start = False
                    
                    if 650 <= mouse[0] <= 790 and 10 <= mouse[1] <= 50:
                        from configuration import *
                        game_start = True
                        starting_time = time.asctime(time.localtime(time.time()))
                        while len(rockX) > 10:
                            rockX.pop()
                            rockY.pop()
            
            # This will display the play again and continue buttons
            mouse = pg.mouse.get_pos()
            
            if 10 <= mouse[0] <= 150 and 10 <= mouse[1] <= 50: 
                pg.draw.rect(screen, (200, 200, 200), [10, 10, 140, 40])
                playagain = font1.render("Play Again", True, (0, 0, 0))
            else: 
                pg.draw.rect(screen, (255, 255, 255), [10, 10, 140, 40])
                playagain = font1.render("Play Again", True, (25, 90, 114))
            screen.blit(playagain, (22, 10))
            
            if 650 <= mouse[0] <= 790 and 10 <= mouse[1] <= 50: 
                pg.draw.rect(screen, (200, 200, 200), [650, 10, 140, 40])
                playagain = font1.render("Continue", True, (0, 0, 0))
            else: 
                pg.draw.rect(screen, (255, 255, 255), [650, 10, 140, 40])
                playagain = font1.render("Continue", True, (25, 90, 114))
            screen.blit(playagain, (668, 10))
        
        # If game is not over, main game background is shown
        else:
            end_time = time.asctime(time.localtime(time.time()))
            displaygamebg(scorep1 + sum(p1scorelist), 
                          scorep2 + sum(p2scorelist))
        
        # Loop to check any button presses
        for event in pg.event.get():
            
            #If cross is clicked, window closes
            if event.type == pg.QUIT:
                gameloop = False
                
            if event.type == pg.KEYDOWN:
                
                # If escape key is pressed, window closes
                if event.key == pg.K_ESCAPE:
                    gameloop = False
                
                #Movement Keys
                if player1disp:
                    if event.key == pg.K_UP:
                        player1Y -= 53
                    if event.key == pg.K_DOWN:
                        player1Y += 53
                    if event.key == pg.K_LEFT:
                        player1ch = -2.5
                    if event.key == pg.K_RIGHT:
                        player1ch = 2.5
                elif player2disp:
                    if event.key == pg.K_w:
                        player2Y -= 53
                    if event.key == pg.K_s:
                        player2Y += 53
                    if event.key == pg.K_a:
                        player2ch = -2.5
                    if event.key == pg.K_d:
                        player2ch = 2.5
            
            if event.type == pg.KEYUP:
                if player1disp:
                    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                        player1ch = 0
                elif player2disp:
                    if event.key == pg.K_a or event.key == pg.K_d:
                        player2ch = 0
        
        # Modifying player movement value
        if player1disp:
            player1X += player1ch
            scorep1calc()
        elif player2disp:
            player2X += player2ch
            scorep2calc()
        
        # Adding player 1 boundaries
        if player1X >= 750:
            player1X = 750
        elif player1X <= 20:
            player1X = 20
        if player1Y >= 610:
            player1Y = 610
        elif player1Y <= 80:
            player1Y = 80
        
        # Adding player 2 boundaries
        if player2X >= 750:
            player2X = 750
        elif player2X <= 20:
            player2X = 20
        if player2Y >= 610:
            player2Y = 610
        elif player2Y <= 80:
            player2Y = 80
        
        # Checking current time to display
        ending_time = time.asctime(time.localtime(time.time()))
        
        # Displaying obstacles and collissions only if game is on
        if not gameovervar:
            
            # Displaying rocks and checking rock collissions
            for i in range(0, len(rockY)):
                
                screen.blit(rockimg, (rockX[i], rockY[i]))
                
                if player1disp:
                    if checkrock(rockX[i], rockY[i], player1X, player1Y):
                        player1reset()
                        p1crash = True
                        p1scorelist.append(scorep1)
                        scorep1 = 0
                        
                elif player2disp:
                    if checkrock(rockX[i], rockY[i], player2X, player2Y):
                        player2reset()
                        p2crash = True
                        p2scorelist.append(scorep2)
                        scorep2 = 0
                        rockspawn()
                        rockspawn()
            
            # Displaying ships and boats and checking collissions
            for i in range(0, 5):
                
                # Inverting ship image and reversing speed if it reaches end
                if shipX[i] >= 580 and shipspeed[i] > 0:
                    shipspeed[i] *= -1
                    shipimg[i] = pg.transform.flip(shipimg[i], True, False)
                elif shipX[i] <= 0 and shipspeed[i] < 0:
                    shipspeed[i] *= -1
                    shipimg[i] = pg.transform.flip(shipimg[i], True, False)
                
                if boatX[i] >= 730 and boatspeed[i] > 0:
                    boatspeed[i] *= -1
                    boatimg[i] = pg.transform.flip(boatimg[i], True, False)
                elif boatX[i] <= 0 and boatspeed[i] < 0:
                    boatspeed[i] *= -1
                    boatimg[i] = pg.transform.flip(boatimg[i], True, False)
                    
                if player1disp:
                    
                    # Managing ship speeds for player 1
                    if p1wins == 0:
                        shipsp = 1
                        boatsp = 1
                    elif p1wins == 1:
                        shipsp = 1.5
                        boatsp = 2
                    elif p1wins == 2:
                        shipsp = 2
                        boatsp = 4
                    elif p1wins == 3:
                        shipsp = 2.5
                        boatsp = 6
                    elif p1wins == 4:
                        shipsp = 3
                        boatsp = 8
                        
                    shipX[i] += shipspeed[i] * shipsp
                    boatX[i] += boatspeed[i] * boatsp
                    
                    screen.blit(shipimg[i], (shipX[i], shipY[i]))
                    screen.blit(boatimg[i], (boatX[i], boatY[i]))
                    
                    # Checking ship collissions for player 1
                    if checkship(shipX[i], shipY[i], player1X, player1Y):
                        player1reset()
                        p1crash = True
                        p1scorelist.append(scorep1)
                        scorep1 = 0
                        
                    # Checking boat collissions for player 1
                    elif checkboat(boatX[i], boatY[i], player1X, player1Y):
                        player1reset()
                        p1crash = True
                        p1scorelist.append(scorep1)
                        scorep1 = 0
                        
                elif player2disp:
                    
                    # Managing ship speeds for player 2
                    if p2wins == 0:
                        shipsp = 1
                        boatsp = 1
                    elif p2wins == 1:
                        shipsp = 1.5
                        boatsp = 2
                    elif p2wins == 2:
                        shipsp = 2
                        boatsp = 4
                    elif p2wins == 3:
                        shipsp = 2.5
                        boatsp = 6
                    elif p2wins == 4:
                        shipsp = 3
                        boatsp = 8
                        
                    shipX[i] += shipspeed[i] * shipsp
                    boatX[i] += boatspeed[i] * boatsp
                    
                    screen.blit(shipimg[i], (shipX[i], shipY[i]))
                    screen.blit(boatimg[i], (boatX[i], boatY[i]))
                        
                    # Checking ship collissions for player 2
                    if checkship(shipX[i], shipY[i], player2X, player2Y):
                        player2reset()
                        p2crash = True
                        p2scorelist.append(scorep2)
                        scorep2 = 0
                        rockspawn()
                        rockspawn()
                        
                    # Checking boat collissions for player 2
                    elif checkboat(boatX[i], boatY[i], player2X, player2Y):
                        player2reset()
                        p2crash = True
                        p2scorelist.append(scorep2)
                        scorep2 = 0
                        rockspawn()
                        rockspawn()
                        
            # Win condition for player 1
            if player1disp:
                if player1X == 380 and player1Y == 80:
                    player1reset()
                    p1wins += 1
                    
                    # Adding score for early completion
                    timetaken = timetosec(ending_time) - timetosec(starting_time)
                    starting_time = ending_time
                    if 60 - (timetaken * 4) >= 0:
                        scorep1 += 60 - (timetaken * 4)
                    p1scorelist.append(scorep1)
                    scorep1 = 0
                    
            # Win condition for player 2
            elif player2disp:
                if player2X == 380 and player2Y == 610:
                    player2reset()
                    p2wins += 1

                    # Adding score for early completion
                    timetaken = timetosec(ending_time) - timetosec(starting_time)
                    starting_time = ending_time
                    if 60 - (timetaken * 4) >= 0:
                        scorep2 += 60 - (timetaken * 4)
                    p2scorelist.append(scorep2)
                    scorep2 = 0
                    rockspawn()
                    rockspawn()
            
            # Game Over condition
            if p1play == 5 and p2play == 5 or p1crash and p2crash:
                gameovervar = True
                for i in range(0, 11):
                    row[i] = 0
                    rowcross[i] = 0
                    
            # Displaying player's end point
            if player1disp:
                screen.blit(end, (380, 86))
            if player2disp:
                screen.blit(end, (380, 620))
                
            # Displaying players
            screen.blit(player1img, (player1X, player1Y))
            screen.blit(player2img, (player2X, player2Y))
            
            if player1disp:
                roundplay = p1play + 1
                p2crash = False
            else:
                roundplay = p1play
                
    # Information screen in the start will be displayed    
    else:
        
        # Loop to check any button presses
        for event in pg.event.get():
            
            # If escape key is pressed, window closes
            if event.type == pg.QUIT:
                gameloop = False
            
            # Checking if 'Play' button is pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                if 325 <= mouse[0] <= 465 and 580 <= mouse[1] <= 620:
                    from configuration import *
                    game_start = True
                    starting_time = time.asctime(time.localtime(time.time()))
        
        # Getting current mouse position
        mouse = pg.mouse.get_pos()
        
        # Initializing rules to be displayed
        name = font4.render(
            "River Crossing Competition Game", True, (0, 0, 0))
        info1 = font2.render(
            "This is a 2 player game. Players get 5 points for", 
            True, (0, 0, 0))
        info2 = font2.render(
            "passing fixed obstacles and 10 points for passing", 
            True, (0, 0, 0))
        info3 = font2.render("moving obstacles.", True, (0, 0, 0))
        info4 = font2.render("The game ends if:", True, (0, 0, 0))
        info5 = font2.render("1. Both players lose in same round", 
                             True, (0, 0, 0))
        info6 = font2.render("2. Both players complete 5 rounds", 
                             True, (0, 0, 0))
        info7 = font2.render("Controls are:", True, (0, 0, 0))
        info8 = font2.render("Player 1", True, (0, 0, 0))
        info9 = font2.render("Player 2", True, (0, 0, 0))
        info10 = font1.render("Press the button to play the game", 
                              True, (0, 0, 0))
        
        # Displaying Rules
        screen.blit(gamestart, (0, 0))
        screen.blit(name, (95, 30))
        screen.blit(info1, (27, 110))
        screen.blit(info2, (27, 140))
        screen.blit(info3, (257, 170))
        screen.blit(info4, (20, 230))
        screen.blit(info5, (90, 260))
        screen.blit(info6, (90, 290))
        screen.blit(info7, (20, 350))
        screen.blit(p1cont, (165, 370))
        screen.blit(p2cont, (465, 355))
        screen.blit(info8, (170, 490))
        screen.blit(info9, (480, 490))
        screen.blit(info10, (200, 530))
        
        # Displaying "Play" Button
        if 325 <= mouse[0] <= 465 and 580 <= mouse[1] <= 620: 
            pg.draw.rect(screen, (100, 100, 100), [325, 580, 140, 40])
            info11 = font1.render("Play", True, (0, 0, 0))
        else: 
            pg.draw.rect(screen, (0, 0, 0), [325, 580, 140, 40])
            info11 = font1.render("Play", True, (255, 255, 255))
        screen.blit(info11, (370, 580))
    
    #Updating Display
    pg.display.update()
    
pg.quit()