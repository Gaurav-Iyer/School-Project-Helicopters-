#####
#Helicopter Game
#By: Gaurav Iyer
#####




#IMPORTS
from tkinter import *
from time import *
from random import *
from math import * 

#SCREEN CREATION#
root = Tk()
screen = Canvas(root, width=800, height=800, background = "Light Gray")

#SETTING INITIAL VALUES#
def setInitialValues():
    
    #GLOBALS FOR ALL VALUES
    global ySpeed,xPos,yPos, filename, playerImage, playerModel,  wallX, wallY, width, height,  qPressed, dead, score, x, gameStart 
    global xStart, xEnd, wallHeight, wallLength, wall,wall2, secondWall, secondWall2, thirdWall, thirdWall2, fourthWall, fourthWall2
    global fifthWall, fifthWall2, sixthWall, sixthWall2, seventhWall, seventhWall2, eighthWall, eighthWall2, newShape, currWall, currWall2
    global gameStart, fontChoice
    global colour, colour2, colour3, colour4, gameStart, diffScreen, helpScreen, explosion
    global menuWidth, buttonX, buttonY , button2Y, button3Y
    global stars, starX,starY,starWidth
    global fireworks, xc, yc, r, fireworkColour, fontColour, rings


    #FONT SELECTION (PLEASE USE BONEHYMIE IF POSSIBLE) IF NOT IT IS DEFAULT TO TIMES
    fontChoice = "Times"
   
    #MENU VALUES
    
    diffScreen = False
    helpScreen = False
    
    menuWidth = 100
    buttonX = 300

    #MENU BUTTON Y-VALUES
    buttonY = 250
    button2Y = 400
    button3Y = 550

    #MENU BUTTON COLOURS
    colour = "White"
    colour2 = "White"
    colour3 = "White"
    colour4 = "White"
    
    
    #HELICOPTER VALUES
    ySpeed = 0
    xPos = 100
    yPos = 400
    
    filename = ["heli0","heli1","heli2","heli3","heli4"]

    #STARTING VALUES
    score = 0

    gameStart = False
    currWall = None     #EMPTY VALUES FOR THE WALLS
    currWall2 = None    
    x = None
    newShape = True     #BOOLEAN TO CREATE A NEW SHAPE
    qPressed = False    #BOOLEANS TO RUN THE GAMS
    dead = False        

    #EMPTY ARRAYS FOR IMAGES
    playerImage = []
    playerModel = []

    #WALLS ON THE TOP AND BOTTOM CO-ORDINATES
    
    xStart = 0
    xEnd = 800

    wallHeight = 20
    wall = 0
    wall2 = 0

    secondWall = 0
    secondWall2 = 0

    thirdWall = 0
    thirdWall2 = 0

    fourthWall = 0
    fourthWall2 = 0

    fifthWall = 0
    fifthWall2 = 0

    sixthWall = 0
    sixthWall2 = 0

    seventhWall = 0
    seventhWall2 = 0

    eighthWall = 0
    eighthWall2 = 0

    wallLength = 800

    #OBSTACLE WALL CO-ORDINATES
    wallX = 1250
    wallY = randint(150,700)

    width = randint(50, 200)
    height = randint(100,300)

    #APPENDS HELICOPTER IMAGES
    for i in range(0,4):
        playerImage.append(PhotoImage(file = filename[i] + "-copy.gif"))
        playerModel.append(0)

    #CREATES VALUES NEEDED TO MAKE FIREWORKS WHEN THE USER WINS
    fireworks = []
    xc = []
    yc = []
    r = []
    fireworkColour = ["Red", "Blue", "Green", "Orange","Pink"]
    fontColour = ["Black","Green","Navy Blue", "Red"]
    rings = [5,6,10,20]
    
    for i in range(0,360):
        xc.append(randint(0,800))
        yc.append(randint(0,800))
        fireworks.append(0)
        r.append(randint(50,200))
                

#CHOOSES WHICH SCREEN TO DISPLAY BASED ON BOOLEAN VALUES    
def menu():

    if diffScreen == True:
        difficultyScreen()

    elif helpScreen == True:
        helpingScreen()
    
    else:
        normScreen()

#THE STANDARD MENU SCREEN
def normScreen():
    global title,t1,t2,t3,b1,b2,b3, b4, t4 ,s

    
    s = screen.create_rectangle(0,0,800,800, fill = "Green")
    title = screen.create_text(400,100, anchor = "center", text = "HELICOPTERZ", font = str(fontChoice) + " 75", fill = "Black")       
    b1 = screen.create_rectangle(buttonX,buttonY, buttonX + 2* menuWidth, buttonY + menuWidth, fill = colour)
    t1 = screen.create_text(buttonX + menuWidth, buttonY + (menuWidth / 2), text = "PLAY" , font = str(fontChoice) + " 50")
    b2 = screen.create_rectangle(buttonX,button2Y, buttonX + 2* menuWidth, button2Y + menuWidth, fill = colour2)
    t2 = screen.create_text(buttonX + menuWidth, button2Y + (menuWidth / 2), text = "HELP" , font = str(fontChoice) + " 50")
    b3 = screen.create_rectangle(buttonX,button3Y, buttonX + 2* menuWidth, button3Y + menuWidth, fill = colour3)
    t3 = screen.create_text(buttonX + menuWidth, button3Y + (menuWidth / 2), text = "QUIT" , font = str(fontChoice) + " 50")
    b4 = 0
    t4 = 0
    
    screen.update()
    screen.delete(title,t1,t2,t3,b1,b2,b3, s, b4,t4)


#SCREEN CONTAINING THE VARIOUS DIFFICULTIES THAT THE USER CAN CHOOSE
def difficultyScreen():
    global title, b1,t1,b2,t2,t3, t4,b4, s
    s = screen.create_rectangle(0,0,800,800, fill = "Red")
    title = screen.create_text(400,100, anchor = "center", text = "HELICOPTERZ", font = str(fontChoice) + " 75" , fill = "Green")       

    b1 = screen.create_rectangle(buttonX,buttonY, buttonX + 2* menuWidth, buttonY + menuWidth, fill = colour)
    t1 = screen.create_text(buttonX + menuWidth, buttonY + (menuWidth / 2), text = "EASY" , font =  str(fontChoice) + " 50")
    b2 = screen.create_rectangle(buttonX,button2Y, buttonX + 2* menuWidth, button2Y + menuWidth, fill = colour2)
    t2 = screen.create_text(buttonX + menuWidth, button2Y + (menuWidth / 2), text = "MEDIUM" , font =  str(fontChoice) + " 45")
    b3 = screen.create_rectangle(buttonX,button3Y, buttonX + 2* menuWidth, button3Y + menuWidth, fill = colour3)
    t3 = screen.create_text(buttonX + menuWidth, button3Y + (menuWidth / 2), text = "HARD" , font =  str(fontChoice) + " 50")
    b4 = screen.create_rectangle(buttonX + (menuWidth * 3.5), button3Y + (menuWidth/2), buttonX + (4.5*menuWidth), button3Y + menuWidth, fill = colour4)
    t4 = screen.create_text(buttonX + (menuWidth * 4), button3Y + (menuWidth * 3/4),anchor = "center", text = "BACK", font =  str(fontChoice) + " 20")

    screen.update()
    screen.delete(title,t1,t2,t3,b1,b2,b3, s, b4,t4)

#DISPLAYS HELP FOR THE USER TO PLAY THE GAME
def helpingScreen():
    global title , s , b4, t4

    s = screen.create_rectangle(0,0,800,800, fill = "White")
    title = screen.create_text(400,400, text = "Welcome to HELICOPTERZ! \n\nThe goal of the game is to get to 5,000 points!\n\nPress the <Space Bar> to make your helicopter fly upwards\n\nbut remember that it will go down when you are not holding space!\n\nDont get hit by anything coloured green!\n\nGOOD LUCK!\nOh yeah. Press 'Q' to quit...but why would you want to quit?", font = "ComicSans 25", fill = "Black")       
    b4 = screen.create_rectangle(buttonX + (menuWidth * 3.5), button3Y + (menuWidth/2), buttonX + (4.5*menuWidth), button3Y + menuWidth, fill = colour4)
    t4 = screen.create_text(buttonX + (menuWidth * 4), button3Y + (menuWidth * 3/4),anchor = "center", text = "BACK", font =  str(fontChoice) + " 20")

    screen.update()
    screen.delete(title,t1,t2,t3,b1,b2,b3, s, b4,t4)

#PROCEDURE FOR USER CLICKING THE 'QUIT' BUTTON
def quitScreen():

    global title , s , b4, t4
    screen.delete(title,t1,t2,t3,b1,b2,b3, s, b4,t4)

    s = screen.create_rectangle(0,0,800,800, fill = "Light Blue")
    title = screen.create_text(400,400, text = "GOOD BYE", font = "ComicSans 65", fill = "Black")       
    

    screen.update()

    sleep(5)
    root.destroy()

#CHANGES BUTTON COLOUR BASED ON THE POSITION OF THE USER'S MOUSE
def motionHandler(event):
    global colour, colour2, colour3, colour4 ,buttonX 
    
    x = event.x
    y = event.y
    
    if buttonX <= x <= buttonX + 2 * menuWidth: #CHECKS IF THE USER IS IN THE RANGE OF THE MIDDLE BUTTONS
        
        if buttonY <= y <= buttonY + menuWidth:  #IF THE USER'S CURSOR IS ON THE BUTTON, THE BUTTON BECOMES GRAY
            colour = "Gray"
            colour2 = "White"
            colour3 = "White"
            colour4 = "White"

            
            

        elif button2Y <= y <= button2Y + menuWidth:
            colour = "White"
            colour2 = "Gray"
            colour3 = "White"
            colour4 = "White"


        elif button3Y <= y <= button3Y + menuWidth:
            colour = "White"
            colour2 = "White"
            colour3 = "Gray"
            colour4 = "White"


    elif buttonX + (menuWidth * 3.5)<= x <=  buttonX + (4.5*menuWidth) and button3Y + (menuWidth/2) <= y <=  button3Y + menuWidth:
        colour = "White"
        colour2 = "White"
        colour3 = "White"
        colour4 = "Gray"
           
    else:
        colour = "White"
        colour2 = "White"
        colour3 = "White"
        colour4 = "White"

#CHECKS IF THE USER CLICKS ON A MENU ITEM
def mouseClickHandler(event):
    global buttonX, diffScreen, helpScreen
    x = event.x
    y = event.y


    if buttonX <= x <= buttonX + 2 * menuWidth: #CHECKS IF USERS MOUSE IS IN THE RANGE OF THE MIDDLE BUTTONS
        
        if buttonY <= y <= buttonY + menuWidth:     #CHECKS WHICH BUTTON THE USER IS CLICKING ON

            if diffScreen == True:
                setEasyValues()
                
            else:
                diffScreen = True

        elif button2Y <= y <= button2Y + menuWidth:

            if diffScreen == True:
                setMediumValues()

            else:
                helpScreen = True


        elif button3Y <= y <= button3Y + menuWidth:
            if diffScreen == True:
                setHardValues()

            else:
                quitScreen()
                
    if diffScreen == True or helpScreen == True:
        if buttonX + (menuWidth * 3.5)<= x <=  buttonX + (4.5*menuWidth) and button3Y + (menuWidth/2) <= y <=  button3Y + menuWidth:
            
            if diffScreen == True:
                diffScreen = False

            elif helpScreen == True:
                helpScreen = False


#SETS THE EASY VALUES FOR THE GAME TO LOAD
def setEasyValues():
    global gameStart,title,t1,t2,t3,t4,b1,b2,b3,b4, s, backMove, wallMove, hardMode, difficulty
    
    gameStart = True        #SETS THE BOLLEAN VALUE TO BE TRUE

    screen.delete(s,title,t1,t2,t3,t4,b1,b2,b3,b4)
    difficulty = 'easy'
    hardMode = False
    backMove = 5
    wallMove = 5

#SETS THE MEDIUM VALUES FOR THE GAME TO LOAD
def setMediumValues():
    global gameStart,title,t1,t2,t3,b1,b2,b3, s, backMove, wallMove, hardMode, difficulty
    
    gameStart = True

    screen.delete(s,title,t1,t2,t3,b1,b2,b3)
    difficulty = 'medium'
    hardMode = False
    backMove = 10
    wallMove = 10

    
#SETS THE HARD VALUES FOR THE GAME TO LOAD
def setHardValues():
    global gameStart,title,t1,t2,t3,b1,b2,b3, s, backMove, wallMove, hardMode, difficulty
    
    gameStart = True        
    difficulty = 'hard'
    screen.delete(s,title,t1,t2,t3,b1,b2,b3)    

    hardMode = True

    backMove = 15
    wallMove = 15


#CHECKING IF THE USER WANTS TO QUIT
def keyChecker( event ):
    global qPressed
    if event.keysym == "q" or event.keysym == "Q":
        qPressed =  True
    else:
        qPressed = False






#CREATING THE BACKGROUND WALLS
def backgroundCreator():
    global xStart, xEnd, wallHeight, wallLength, wall,wall2, secondWall, secondWall2, thirdWall, thirdWall2, fourthWall, fourthWall2
    global fifthWall, fifthWall2, sixthWall, sixthWall2, seventhWall, seventhWall2, eighthWall, eighthWall2

    
    wall = screen.create_rectangle(xStart,0,xEnd,wallHeight,fill = "Green", outline = "Green")
    wall2 = screen.create_rectangle(xStart,800,xEnd, 700 - wallHeight,fill = "Green", outline = "Green")

    secondWall = screen.create_rectangle(xStart + wallLength, 0, xEnd + wallLength, wallHeight + 20,fill = "Green", outline = "Green")
    secondWall2 = screen.create_rectangle(xStart + wallLength, 800, xEnd + wallLength, 710- (wallHeight + 20),fill = "Green", outline = "Green")

    thirdWall = screen.create_rectangle(xStart + (wallLength * 2), 0, xEnd + (2 *wallLength), wallHeight + 40,fill = "Green", outline = "Green")                
    thirdWall2 = screen.create_rectangle(xStart + (wallLength * 2), 800, xEnd + (2 *wallLength), 710 -(wallHeight + 40),fill = "Green", outline = "Green")

    fourthWall = screen.create_rectangle(xStart + (wallLength * 3), 0, xEnd + (3 *wallLength), wallHeight + 60,fill = "Green", outline = "Green")                
    fourthWall2 = screen.create_rectangle(xStart + (wallLength * 3), 800, xEnd + (3 *wallLength), 710 -(wallHeight + 60),fill = "Green", outline = "Green")

    fifthWall = screen.create_rectangle(xStart + (wallLength * 4), 0, xEnd + (4 *wallLength), wallHeight + 60,fill = "Green", outline = "Green")                
    fifthWall2 = screen.create_rectangle(xStart + (wallLength * 4), 800, xEnd + (4 *wallLength), 710 -(wallHeight + 60),fill = "Green", outline = "Green")

    sixthWall = screen.create_rectangle(xStart + (wallLength * 5), 0, xEnd + (5 *wallLength), wallHeight + 40,fill = "Green", outline = "Green")                
    sixthWall2 = screen.create_rectangle(xStart + (wallLength * 5), 800, xEnd + (5 *wallLength), 710 -(wallHeight + 40),fill = "Green", outline = "Green")

    seventhWall = screen.create_rectangle(xStart + (wallLength * 6), 0, xEnd + (6 *wallLength), wallHeight + 20,fill = "Green", outline = "Green")                
    seventhWall2 = screen.create_rectangle(xStart + (wallLength * 6), 800, xEnd + (6 *wallLength), 710 -(wallHeight + 20),fill = "Green", outline = "Green")
    
    eighthWall = screen.create_rectangle(xStart + (wallLength * 7), 0, xEnd + (10 *wallLength), wallHeight ,fill = "Green", outline = "Green")                
    eighthWall2 = screen.create_rectangle(xStart + (wallLength * 7), 800, xEnd + (10 *wallLength), 710 - wallHeight,fill = "Green", outline = "Green")



def backgroundUpdater():
    global xStart, xEnd
    if xStart +(wallLength * 7) < -100:        
        xStart = 0
        xEnd = 800
        
    xStart = xStart - backMove
    xEnd = xEnd - backMove

    
#CHECKING THE USERS MOUSE TO SET THE MOVEMENT OF THEIR HELICOPTER       
def spaceClickEvent(event):
    global ySpeed
    for i in range(0,5):
        ySpeed = -5
        
def spaceReleaseEvent(event):
    global ySpeed
    ySpeed = 5


#UPDATES THE HELICOPTER POSITION BASED ON THE CURRENT Y SPEED   
def updateHeliPosition():
    global yPos
    
    yPos = yPos + ySpeed


#DRAWS THE PLAYER MODEL OVER ITSELF SO THAT THE GIF IMAGES ARE COMBINED
def drawHeli():
    global xPos,yPos,playerModel
    for i in range(0,4):
        playerModel[i] = screen.create_image(xPos,yPos,image = playerImage[i], tags = "model")


#MOVES OBSTACLES AND RESETS THEIR X-VALUE IF IT IS OFF THE SCREEN
def wallUpdater():
    global wallX, wallY, height , width, score, newShape
    
    if wallX <= -200 :
        newShape = True
        wallX = 1300
        width = randint(25, 200)
        height = randint(175,225)
        wallY = randint(100,350)
        
    wallX = wallX - wallMove


#DECIDES WHAT KIND OF WALLS SHOULD BE CREATED
def wallCreator():

    global x, hardMode
    
    someList = ["a","b"]

    if hardMode == True:        #ON HARD MODE THERE ARE SPECIAL WALLS ON THE BOTTOM
        hardWallCreator()

    else:
        if newShape == True:
            x = choice(someList)

        if x == "a":
            rectangleCreator()
        else:
            circleCreator()

#CREATES NORMAL RECTANGLE WALLS   
def rectangleCreator():
    global currWall, newShape
    
    currWall = screen.create_rectangle(wallX,wallY,wallX + width, wallY + height, fill = "Green", outline = "Green")
    newShape = False



#CREATES WALLS THAT ARE CIRCLES INSTEAD OF RECTANGLES   
def circleCreator():
    global currWall, newShape
    
    currWall = screen.create_oval(wallX,wallY, wallX + width, wallY + height, fill = "Green", outline = "Green")
    newShape = False


#CREATES THE BOTTOM WALLS ON HARD MODE
def hardWallCreator():
    global currWall, currWall2
    currWall = screen.create_rectangle(wallX,0,wallX + 50, wallY,fill = "Green", outline = "Green")
    currWall2 = screen.create_rectangle(wallX,800,wallX + 50 , wallY + height, fill = "Green", outline = "Green")


#COLLISION DETECTOR
def collisionFinder():
    global dead
    box = screen.bbox("model")

    overlappingItems = screen.find_overlapping(box[0] + 5,box[1] + 40, box[2] - 40 , box[3] - 30 )
    
    if len(overlappingItems) > 4:           #OVERLAPPING ITEMS NORMALLY HAS 4 ITEMS IN IT ( 4 CO-ORDINATES). IF THERE IS 5 IT IS OVERLAPPING WITH ANOTHER ITEM

        
       dead = True
       
    else:
        dead = False

#CREATES AND UPDATES THE SCORE BASED ON USER'S DIFFICULTY   
def scoreCreator():
    global score, currScore
    
    if difficulty == 'easy':
        
        score += 1

    elif difficulty == 'medium':

        score += 2
        
    else:
        
        score += 5
    
    currScore = screen.create_text(100,20, text = "Score : " + str(score), font = "ComicSans 30")

#INCREASES THE SPEED UNTIL THE SPEED IS CAPPED
def speedUpdater():
    global backMove,wallMove

    if score> 0 and score % 1000 == 0:

        if difficulty == 'easy':
            if backMove < 25:
                backMove += 2
                wallMove += 2

            else:
                bacMove = 25
                wallMove = 25
                
        if difficulty == 'medium':
            if backMove < 30:
                backMove += 3
                wallMove += 3

            else:
                bacMove = 30
                wallMove = 30

        if difficulty == 'hard':
            if backMove < 30:
                backMove += 3
                wallMove += 3

            else:
                bacMove = 30
                wallMove = 30

                
#DELETES OBJECTS AND UPDATES THE SCREEN
def objDeleter():
    global playerModel, currWall, currWall2, currScore
    global xStart, xEnd, wallHeight, wallLength, wall,wall2, secondWall, secondWall2, thirdWall, thirdWall2, fourthWall, fourthWall2
    global fifthWall, fifthWall2, sixthWall, sixthWall2, seventhWall, seventhWall2, eighthWall, eighthWall2

    screen.update()
    sleep(0.01)
    collisionFinder()
    
    for i in range(0,4):
        screen.delete(playerModel[i])
        screen.delete(wall,wall2, secondWall, secondWall2, thirdWall, thirdWall2, fourthWall, fourthWall2)
        screen.delete(fifthWall, fifthWall2, sixthWall, sixthWall2, seventhWall, seventhWall2, eighthWall, eighthWall2)
        screen.delete(currWall, currWall2)
        screen.delete(currScore)

#VARIOUS OUTCOMES OF THE GAME ENDING
def endDecider():
    if qPressed == True:
        whyWouldYouQuitThisWonderfulGame()

    elif dead == True:
        endingAnim()

    else:
        winAnim()
        
#USER HAS PUSHED Q
def whyWouldYouQuitThisWonderfulGame():

    screen.create_text(400,400, text = "It seems you have accidentaly pushed the 'Q' button.\nThis must be an accident because there is no way that you would \nwillingly quit this beautiful game.\nHave a nice day! Remember to re-open the game!", font = "ComicSans 25")
    screen.update()
    sleep(15)
    root.destroy()



#USER HAS WON THE GAME
def winAnim():
    timesRan = 0

    screen.create_rectangle(0,0,800,800, fill = "Purple")


    for fc in range(0,5):
        
        col = fc % len(fireworkColour)      #SELECTS A VALUE FROM COL COL2 AND NUM
        col2 = fc % len(fontColour)
        num = fc % len(rings)
        
        for angle in range(0,360,rings[num]):   #CREATES LINES UNTIL A FULL CIRCLE HAS BEEN CREATED
            
            screen.create_text(400,50,text = "YOU WIN",font = "Times 100", fill = fontColour[col2])
            angleRad = angle * pi/180
            x = r[fc] * cos(angleRad) + xc[fc]
            y = r[fc] * sin(angleRad) + yc[fc] 
            fireworks[angle] = screen.create_line(xc[fc],yc[fc],x,y,fill = fireworkColour[col],width = 4)

        screen.update()
        sleep(0.9)
       
        for angle in range(0,360):
            screen.delete(fireworks[angle])
                
            
    
    root.destroy()

#USER HAS LOST       
def endGame():
    global playerModel, currWall, currWall2, currScore
    global xStart, xEnd, wallHeight, wallLength, wall,wall2, secondWall, secondWall2, thirdWall, thirdWall2, fourthWall, fourthWall2
    global fifthWall, fifthWall2, sixthWall, sixthWall2, seventhWall, seventhWall2, eighthWall, eighthWall2

    
    screen.delete(wall,wall2, secondWall, secondWall2, thirdWall, thirdWall2, fourthWall, fourthWall2)
    screen.delete(fifthWall, fifthWall2, sixthWall, sixthWall2, seventhWall, seventhWall2, eighthWall, eighthWall2)
    endingAnim()

#USER HAS LOST
def endingAnim():
    global playerModel
    boxCount = 0
    drawHeli()
    while boxCount < 3:

        box = screen.create_rectangle(xPos - 100, yPos - 100, xPos + 100,yPos + 100, fill = "light gray", outline = "light gray")
        screen.create_text(400,100, text = "A TERRIBLE MISTAKE HAS OCCURED!", font = "Times 40")

        screen.update()
        sleep(1)
        screen.delete(box)
        screen.update()
        sleep(1)
        boxCount += 1

    screen.delete(playerModel)
    screen.update()
    root.destroy()

#GAMES RUNNER
def runGame():
    
    setInitialValues()

    while gameStart == False:           #RUNS THE MENU UNTIL THE USER SELECTS A DIFFICULTY
        menu()
        
    while qPressed == False and dead == False and gameStart == True and score < 5000:          #RUNS THE GAME WHILE THE CONDITIONS FOR THE GAME TO END HAVE NOT BEEN MET
        
        backgroundUpdater()
        backgroundCreator()
        wallUpdater()
        wallCreator()
        updateHeliPosition()
        drawHeli()
        scoreCreator()
        speedUpdater()
        objDeleter()

    endDecider()
    
#GIVES POWER TO RUNGAME
root.after(100, runGame)

#BIND STATEMENTS
screen.bind("<Motion>",motionHandler)
screen.bind("<space>", spaceClickEvent)
screen.bind("<Button-1>",mouseClickHandler)
screen.bind("<KeyRelease-space>",spaceReleaseEvent)
screen.bind("<Key>",keyChecker)

#SCREEN PACKING AND SETTING
screen.pack()
screen.focus_set()
root.mainloop()
