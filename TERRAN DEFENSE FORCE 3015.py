#TERRAN DEFENSE LEAGUE 3015
#Julian Li
#########################################

#Imports everything
from tkinter import *
from math import *
from random import *
from time import *

#Creates initial screen
root = Tk()
screen = Canvas(root, width=500, height=800, background = "black")

#Sets values needed for game to run
def preValues():  
    global playerHP, playerShip, shipImage, mouseX, mouseY, hitPlayer
    global enemyHP, enemyShip, enemyImage, enemyX, enemyY, enemyMove, hitEnemy, enemyOptions, atkChoice
    
    global blaster, blasterSpeed, blasterX, blasterY, blastImage
    global missileX, missileY, missileImage, explosionImage, missileLaunch
    global eBlast, eBlastxSpeed, eBlastySpeed, eBlastX, eBlastY, eBlastImage, eBlastDev, atkImage1, atkImage2

    global star, starX, starY, starSpeed, starSize
    
    global gameRunning, spaceImage


    gameRunning = True

    spaceImage = PhotoImage(file = "space.gif")

    star = []
    starX = []
    starY = []
    starSpeed = []
    starSize = []
    
    shipImage = PhotoImage(file = "ship.gif")
    playerShip = 0
    mouseX = 250
    mouseY = 450
    playerHP = 500
    hitPlayer = False

    enemyImage = PhotoImage(file = "enemy.gif")
    enemyShip = 0
    enemyX = 250
    enemyY = 180
    enemyMove = 0
    enemyHP = 500
    enemyOptions = [1, 2]
    atkChoice = 0
    hitEnemy = False

    blastImage = PhotoImage(file = "blaster.gif")
    blaster = []
    blasterX = []
    blasterY = []
    blasterSpeed = 30

    missileImage = PhotoImage(file = "missile.gif")
    missileX = 0
    missileY = 0
    missileLaunch = False

    eBlast = []
    eBlastxSpeed = []
    eBlastySpeed = []
    eBlastX = []
    eBlastY = []
    eBlastDev = []
    atkImage1 = PhotoImage(file = "enemyBlast2.gif")
    atkImage2 = PhotoImage(file = "enemyBlast.gif")
    eBlastImage = []


#Spawns stars for background
def spawnStars():
    global star, starX, starY, starSpeed, starSize
    
    xPos = randint(0, 500)
    currentSize = randint(5, 10)
    currentSpeed = randint(3, 7)
    
    star.append(0)
    starX.append(xPos)
    starY.append(40)
    starSize.append(currentSize)
    starSpeed.append(currentSpeed)

#Draws stars
def drawStars():
    for i in range(0, len(star)):
        star[i] = screen.create_line(starX[i], starY[i], starX[i], starY[i] + starSize[i], fill = "white")

#Updates stars as they fall down
def updateStars():
    i=0
    while i< len(starY):
        starY[i] = starY[i] + starSpeed[i]
        starArrayDel()
        i+=1

#Deletes stars
def deleteStars():
    for i in range(0, len(star)):
        screen.delete(star[i])

#Gets rid of stars once they're off the screen
def starArrayDel():
    i = 0

    while i < len(star) - 1:
        if starY[i]>800:
            star.pop(i)
            starX.pop(i)
            starY.pop(i)
            starSpeed.pop(i)
        else:
            i = i + 1
    

#Handles keypresses
def keyDownHandler(event):
    global missileLaunch
    if event.keysym == "z":
        spawnBlaster()
    elif event.keysym == "x" and missileLaunch == False:
        spawnMissile()

#####################
#   PLAYER'S SHIP   #
#####################

#Spawns player's secondary missile
def spawnMissile():
    global mouseX, mouseY
    global missileX, missileY, missileLaunch
    missileX = mouseX
    missileY = mouseY
    missileLaunch = True

#Draws missile
def drawMissile():
    global missileX, missileY, missileImage, missileObj
    missileObj = screen.create_image(missileX, missileY, image = missileImage)

#Updates missile position
def updateMissile():
    global missileX, missileY
    missileY = missileY - 10

#Deletes missile after every frame
def deleteMissile():
    global missileObj
    screen.delete(missileObj)

#Spawns player's main weapon
def spawnBlaster():
    global blaster, blasterX, blasterY, mouseX, mouseY
    blasterX.append(mouseX)
    blasterY.append(mouseY)
    blaster.append(0)

#Update positions of player's blaster bullets
def updateBlasters():
    global blaster, blasterX, blasterY

    for i in range(0, len(blasterY)):
        blasterY[i] = blasterY[i] - blasterSpeed

    blasterArrayDel()

#Keeps framerate from dropping by deleting off-screen player bullets from array
def blasterArrayDel():
    i = 0

    while i < len(blasterY) - 1:
        if blasterY[i]<30:
            blasterY.pop(i)
            blasterX.pop(i)
            blaster.pop(i)

        else:
            i = i + 1

#Draws images for blaster bullets once they've been spawned
def drawBlaster():
    global blastImage
    for i in range(0, len(blasterY)):
        blaster[i] = screen.create_image(blasterX[i], blasterY[i], image = blastImage)

#Deletes blaster bullets when certain conditions are met
def deleteBlaster():
    for i in range(0, len(blasterY)):
        screen.delete(blaster[i])
    
#Detects mouse movements for ship's X and Y values
def shipMovementHandler(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y
    drawShip()
    screen.update()

#Draws image of ship on screen
def drawShip():
    global playerShip, shipImage, mouseX, mouseY
    screen.delete(playerShip)
    playerShip = screen.create_image(mouseX, mouseY, image = shipImage)


########################
#      ENEMY SHIP      #
########################

#Draws image of enemy ship on screen
def drawEnemy():
    global enemyShip, enemyImage, enemyX, enemyY
    screen.delete(enemyShip)
    enemyShip = screen.create_image(enemyX, enemyY, image = enemyImage)
    

#Moves enemy ship side-to-side
def enemyUpdate():
    global enemyShip, enemyX, enemyY, enemyMove, enemySpeed
    enemyX = -150*cos(0.01*enemyMove) + 250
    enemyMove = enemyMove + 1

#Enemy ship chooses to switch its attack every once in a while
def enemyChoice():
    global enemyOptions, atkChoice
    atkChoice = choice(enemyOptions)

#####################
#   ENEMY ATTACKS   #
#####################



#Spawns bullets for enemy attacks
def spawnEnemyAttack():
    
    global eBlast, eBlastxSpeed, eBlastySpeed, eBlastX, eBlastY, atkChoice, eBlastDev
    global enemyX, enemyY
    global eBlastImage, atkImage1, atkImage2

    #Attack pattern #1: Spray of bullets from enemy ship's center
    if atkChoice == 1:

        eBlastImage.append(atkImage1)
        
        speedX = randint(-3, 3)
        speedY = randint(3, 5)
        eBlastxSpeed.append(speedX)
        eBlastySpeed.append(speedY)

        eBlastDev.append(0)
        
        eBlastX.append(enemyX)
        eBlastY.append(enemyY)
        eBlast.append(0)

    #Attack pattern #2: Hail of bullets falling vertically from the enemy ship
    elif atkChoice == 2:

        eBlastImage.append(atkImage2)

        speedX = 0
        speedY = randint(5, 7)
        eBlastxSpeed.append(speedX)
        eBlastySpeed.append(speedY)

        deviation = randint(-142, 142)
        eBlastDev.append(deviation)
        
        eBlastX.append(enemyX)
        eBlastY.append(enemyY)
        eBlast.append(0)

#Draws bullets for enemy attacks
def drawEnemyAttack():
    
    global eBlast, eBlastxSpeed, eBlastySpeed, eBlastX, eBlastY, blastImage, atkChoice, eBlastDev

    for i in range(0, len(eBlastY)):
        eBlast[i] = screen.create_image(eBlastX[i] + eBlastDev[i], eBlastY[i] + 100, image = eBlastImage[i])

#Updates bullets for enemy attacks
def updateEnemyAttack():
    global eBlast, eBlastX, eBlastY, eBlastxSpeed, eBlastySpeed

    for i in range(0, len(eBlastY)):
        eBlastX[i] = eBlastX[i] + eBlastxSpeed[i]
        eBlastY[i] = eBlastY[i] + eBlastySpeed[i]

    enemyBlastArrayDel()

#Prevents framerate from dropping by removing off-screen enemy energy blasts from array
def enemyBlastArrayDel():
    i = 0

    while i < len(eBlastY) - 1:
        if eBlastY[i]>800:
            eBlastY.pop(i)
            eBlastX.pop(i)
            eBlast.pop(i)
            eBlastxSpeed.pop(i)
            eBlastySpeed.pop(i)
            eBlastDev.pop(i)
            eBlastImage.pop(i)

        else:
            i = i + 1

#Deletes bullets for enemy ship when certain conditions are met
def deleteEnemyBlasts():
    for i in range(0, len(eBlast)):
        screen.delete(eBlast[i])
        

#####################
#   HIT DETECTION   #
#####################


#Detects if a player's blaster bullet has hit the enemy ship and then deals damage accordingly
def playerHit():
    global enemyHP, enemyShip, enemyX, enemyY
    global blaster, blasterSpeed, blasterX, blasterY
    global hitEnemy

    for i in range(0, len(blasterY)):
        if enemyX - 141 <= blasterX[i] <= enemyX + 141 and enemyY - 100 <= blasterY[i] <= enemyY + 100:
            screen.delete(blaster[i])
            blasterY.pop(i)
            blasterX.pop(i)
            blaster.pop(i)
            enemyHP = enemyHP - 1
            hitEnemy = True
            break

#Detects if a player's missile has hit the enemy ship OR if it has went off the screen
def missileHit():
    global missileX, missileY, missileObj, missileLaunch
    global enemyX, enemyY, enemyHP, hitEnemy
    missileEnemyDist = distCheck(missileX, missileY, enemyX, enemyY)

    if missileEnemyDist < 150:
        hitEnemy = True
        missileX = 0
        missileY = 0
        enemyHP = enemyHP - 20
        screen.delete(missileObj)
        speedMult = 5
        missileLaunch = False

    elif missileY < 90:
        missileX = 0
        missileY = 0
        screen.delete(missileObj)
        speedMult = 5
        missileLaunch = False
    

#Finds distance between two objects (Needed for hit detection)
def distCheck(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

#Detects if an enemy bullet has hit the player ship and then deals damage accordingly
def enemyHit():
    global playerHP, playerShip, mouseX, mouseY
    global eBlast, eBlastX, eBlastY, eBlastxSpeed, eBlastySpeed, eBlastDev
    global hitPlayer
    Poppables = []
    for i in range(0, len(eBlast)):
        
        shipBulletDist = distCheck(mouseX, mouseY, eBlastX[i] + eBlastDev[i], eBlastY[i] + 100)
        
        if shipBulletDist < 20:
            playerHP = playerHP - 50
            hitPlayer = True
            Poppables.append(i)
            
    for i in range(len(eBlast)):
        if i in Poppables:
            screen.delete(eBlast[i])
            eBlastY.pop(i)
            eBlastX.pop(i)
            eBlast.pop(i)
            eBlastxSpeed.pop(i)
            eBlastySpeed.pop(i)
            eBlastImage.pop(i)
            eBlastDev.pop(i)

#Check if the player's ship has hit the enemy ship; if so, depletes player's entire health bar
def shipCollision():
    global playerHP, playerShip, mouseX, mouseY
    global enemyHP, enemyShip, enemyX, enemyY
    global hitPlayer

    shipEnemyDist = distCheck(mouseX, mouseY, enemyX, enemyY)

    if shipEnemyDist < 150:
        playerHP = 0
        hitPlayer = True

#Displays player HP at the bottom of the screen
def drawPlayerHP():
    global playerHP, playerHPBar, playerHPText
    dudHP = playerHP/50
    healthText = "HP: " + str(dudHP)
    playerHPBar = screen.create_rectangle(0, 20, playerHP, 40, fill = "Dark Green")
    playerHPText = screen.create_text(250, 30, text = healthText, font = "Helvetica 10", anchor = CENTER, fill = "white")

#Displays enemy HP at the bottom of the screen
def drawEnemyHP():
    global enemyHP, enemyHPBar, enemyHPText
    healthText = "MOTHERSHIP HP: " + str(enemyHP)
    enemyHPBar = screen.create_rectangle(0, 0, enemyHP, 20, fill = "Dark Blue")
    enemyHPText = screen.create_text(250, 10, text = healthText, font = "Helvetica 10", anchor = CENTER, fill = "white")

#####################
#   MISCELLANEOUS   #
#####################

#Checks as to whether or not the game should still be running
def runningCheck():
    global gameRunning
    if enemyHP <= 0 or playerHP <= 0:
        gameRunning = False

#Detects if the player has moved into the interface bar and pushes the player back
def offLimits():
    global mouseY, offLimit, gameRunning
    if mouseY < 40:
        gameRunning = False
        offLimit = True

#Creates menu screen
def menuCreate():
    global playButton, infoButton, spaceImage, space, infoPressed, Title
    
    preValues()
    
    infoPressed = False
    
    space = screen.create_image(250, 400, image = spaceImage)
    playButton = Button(screen, text="Play", font=("Helvetica", 18), command = run)
    infoButton = Button(screen, text="Info", font=("Helvetica", 18), command = createInfo)

    Title = screen.create_text(250, 200, text = "TERRAN DEFENSE LEAGUE 3015", font = "Helvetica 20", anchor = CENTER, fill = "white")
    
    playButton.place(x = 250, y = 400, anchor = CENTER)
    infoButton.place(x = 250, y = 450, anchor = CENTER)

#Creates text for game's plot and instructions
def createInfo():
    global infoPressed, text1, text2, text3
    if infoPressed == False:
        infoPressed = True
        text1 = screen.create_text(250, 500, text = "ALIENS ARE TRYING TO DESTROY EARTH", font = "Helvetica 14", anchor = CENTER, fill = "white")
        text2 = screen.create_text(250, 530, text = "DESTROY THEIR MOTHERSHIP TO STOP THEM", font = "Helvetica 14", anchor = CENTER, fill = "white")
        text3 = screen.create_text(250, 560, text = "MOUSE TO MOVE, Z FOR MAIN GUNS, X FOR MISSILE", font = "Helvetica 14", anchor = CENTER, fill = "white")

    elif infoPressed == True:
        infoPressed = False
        screen.delete(text1)
        screen.delete(text2)
        screen.delete(text3)
        
    
    
#Puts everything together to run
def run():
    global hitEnemy, hitPlayer, enemyHPBar, offLimits, playButton, infoButton, space, infoPressed, Title
    global playerHPText, enemyHPText
    global spaceImage
    preValues()
    drawEnemyHP()
    drawPlayerHP()

    frame = 0
    playButton.destroy()
    infoButton.destroy()
    screen.delete(space)
    screen.delete(Title)

    if infoPressed == True:
        screen.delete(text1)
        screen.delete(text2)
        screen.delete(text3)
    
    while gameRunning == True:

        runningCheck()

        offLimits()

        updateEnemyAttack()
        updateBlasters()
        updateMissile()
        updateStars()

        if frame%2 == 0:
            spawnStars()
        drawStars()
        drawShip()
        drawEnemy()
        drawBlaster()
        drawMissile()

        playerHit()
        enemyHit()
        missileHit()
        shipCollision()

        if frame%5 == 0:
            spawnEnemyAttack()
            
        drawEnemyAttack()

        if frame%100 == 0:
            enemyChoice()
        
        if hitEnemy == True:
            screen.delete(enemyHPBar)
            screen.delete(enemyHPText)
            drawEnemyHP()
            hitEnemy = False

        if hitPlayer == True:
            screen.delete(playerHPBar)
            screen.delete(playerHPText)
            drawPlayerHP()
            hitPlayer = False

        screen.update()
        sleep(0.01)
        enemyUpdate()
        deleteBlaster()
        deleteEnemyBlasts()
        deleteMissile()
        deleteStars()


        frame = frame + 1

    contextual = 0

    if enemyHP <= 0:
        endText = "YOU BLEW UP THE ALIEN MOTHERSHIP"
        contextual = 1
    elif playerHP <= 0:
        endText = "YOU WERE BLOWN UP BY THE ALIEN MOTHERSHIP"
        contextual = 2
    elif offLimit == True:
        endText = "YOU FLED FROM THE MOTHERSHIP"
        contextual = 3
    
    screen.create_image(250, 400, image = spaceImage)
    
    screen.create_text(250, 400, text = endText, font = "Helvetica 14", anchor = CENTER, fill = "white")

    if contextual == 1:
        screen.create_text(250, 430, text = "UPON RETURNING TO EARTH,", font = "Helvetica 14", anchor = CENTER, fill = "white")
        screen.create_text(250, 460, text = "YOU ARE GIVEN A MEDAL FOR YOUR HEROISM", font = "Helvetica 14", anchor = CENTER, fill = "white")

    elif contextual == 2:
        screen.create_text(250, 430, text = "NOW IT'S DESTROYING EARTH", font = "Helvetica 14", anchor = CENTER, fill = "white")
        screen.create_text(250, 460, text = "I HOPE YOU'RE PROUD OF YOURSELF", font = "Helvetica 14", anchor = CENTER, fill = "white")

    elif contextual == 3:
        screen.create_text(250, 430, text = "NOW NOTHING CAN STOP ITS RAMPAGE ON EARTH", font = "Helvetica 14", anchor = CENTER, fill = "white")
        screen.create_text(250, 460, text = "YOU BLEW IT, BOZO", font = "Helvetica 14", anchor = CENTER, fill = "white")

    screen.delete(playerShip)
    screen.delete(enemyShip)
    screen.update()
        
       

root.after(5, menuCreate)

screen.bind("<Motion>", shipMovementHandler)
screen.bind("<Key>", keyDownHandler)
screen.pack()
screen.focus_set()

root.mainloop()
