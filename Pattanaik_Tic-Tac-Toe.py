#This python prgram uses the turtle and time packages to function
from turtle import *
import time

sven = Turtle()
wn = Screen()

wn.bgcolor("black")
sven.pencolor("white")
wn.title("Tic-Tac-Toe")
wn.setup(600,600)
sven.hideturtle()
sven.speed(0)
sven.up()
sven.pensize(10)

gameExit = False

def selectMode():
    mode = input("""Select Game Mode:
1)Player Vs. Player
2)Player Vs. Computer
""")
    return mode

def drawBoard():
    #Horizontal bars
    sven.goto(-300,100)
    sven.pd()
    sven.fd(600)
    sven.pu()
    sven.goto(-300,-100)
    sven.pd()
    sven.fd(600)
    sven.pu()

    #Vertical bars
    sven.goto(-100,300)
    sven.setheading(-90)
    sven.pd()
    sven.fd(600)
    sven.pu()
    sven.goto(100,300)
    sven.pd()
    sven.fd(600)
    sven.pu()


#Draw O's and X's
def drawX(x,y):
    sven.pu()
    sven.goto(x+20,y-20)
    sven.setheading(-45)
    sven.pd()
    sven.fd(226)
    sven.pu()
    sven.goto(x+180,y-20)
    sven.setheading(-135)
    sven.pd()
    sven.fd(226)
    sven.pu()

def drawO(x,y):
    sven.pu()
    sven.goto(x+100,y-180)
    sven.setheading(0)
    sven.pd()
    sven.circle(80)
    sven.pu()

#Set up the board with a list to monitor where the X's and O's are
boardPieces = ["","","","","","","","",""]
nextTurn = "X"


def drawPieces(boardPieces):
    x = -300
    y = 300
    for pieces in boardPieces:
        if pieces == "X":
            drawX(x,y)
        elif pieces == "O":
            drawO(x,y)
        x = x + 200
        if x > 100:
            x = -300
            y = y - 200
            
#Main program

def clicked(x,y):
    global gameExit
    if gameExit == False:
        global nextTurn, pieces
        column = (x+300) //200
        row = (-y+300) //200
        square = column + row*3
        square = int(square)
        boardPieces[square] = nextTurn
        #Checks to draw an X or an O
        if nextTurn == "X":
            nextTurn = "O"
            
        else:
            nextTurn = "X"
        drawPieces(boardPieces)
        threeInARow(boardPieces)
    else:
        pass

def computerMove(pieces):
    if pieces[0] == "X" or pieces[2] == "X" or pieces[6] == "X" or pieces[8] == "X":
        clicked(300,300)
    if pieces[1] == "X" or pieces[3] == "X" or pieces[5] == "X" or pieces[7] == "X":
        clicked(300,300)

def playAgain(boardPieces):
    Q = input("Do you want to play again? ")
    if Q == "yes":
        gameExit = True
        sven.reset()
        boardPieces.clear()
        for i in range(9):
            boardPieces.append("")
        sven.pencolor("white")
        sven.hideturtle()
        sven.speed(0)
        sven.up()
        sven.pensize(10)
        drawBoard()
        selectMode()
    else:
        quit()

#Checks to see if a player got 3 in a row
def threeInARow(pieces):
    #Uses the board as a list to check
    if pieces[0] == "X" and pieces[1] == "X" and pieces[2] == "X":
        print("Player 1 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(0)
        sven.goto(-300,200)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[3] == "X" and pieces[4] == "X" and pieces[5] == "X":
        print("Player 1 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(0)
        sven.goto(-300,0)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[6] == "X" and pieces[7] == "X" and pieces[8] == "X":
        print("Player 1 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(0)
        sven.goto(-300,-200)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[0] == "X" and pieces[3] == "X" and pieces[6] == "X":
        print("Player 1 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(90)
        sven.goto(-200,-300)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[1] == "X" and pieces[4] == "X" and pieces[7] == "X":
        print("Player 1 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(90)
        sven.goto(0,-300)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[2] == "X" and pieces[5] == "X" and pieces[8] == "X":
        print("Player 1 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(90)
        sven.goto(200,-300)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[0] == "X" and pieces[4] == "X" and pieces[8] == "X":
        print("Player 1 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(135)
        sven.goto(300,-300)
        sven.pd()
        sven.fd(848.5)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[2] == "X" and pieces[4] == "X" and pieces[6] == "X":
        print("Player 1 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(45)
        sven.goto(-300,-300)
        sven.pd()
        sven.fd(848.5)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[0] == "O" and pieces[1] == "O" and pieces[2] == "O":
        print("Player 2 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(0)
        sven.goto(-300,200)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[3] == "O" and pieces[4] == "O" and pieces[5] == "O":
        print("Player 2 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(0)
        sven.goto(-300,0)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[6] == "O" and pieces[7] == "O" and pieces[8] == "O":
        print("Player 2 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(0)
        sven.goto(-300,-200)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[0] == "O" and pieces[3] == "O" and pieces[6] == "O":
        print("Player 2 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(90)
        sven.goto(-200,-300)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[1] == "O" and pieces[4] == "O" and pieces[7] == "O":
        print("Player 2 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(90)
        sven.goto(0,-300)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[2] == "O" and pieces[5] == "O" and pieces[8] == "O":
        print("Player 2 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(90)
        sven.goto(200,-300)
        sven.pd()
        sven.fd(600)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[0] == "O" and pieces[4] == "O" and pieces[8] == "O":
        print("Player 2 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(135)
        sven.goto(300,-300)
        sven.pd()
        sven.fd(848.5)
        time.sleep(3)
        playAgain(boardPieces)
    if pieces[2] == "O" and pieces[4] == "O" and pieces[6] == "O":
        print("Player 2 Wins!")
        sven.pu()
        sven.pencolor("red")
        sven.setheading(45)
        sven.goto(-300,-300)
        sven.pd()
        sven.fd(848.5)
        time.sleep(3)
        playAgain(boardPieces)

mode = selectMode()
if mode == "1":
    drawBoard()
    onscreenclick(clicked)
if mode == "2":
    drawBoard()
    onscreenclick(clicked)
    onscreenclick(None)
    computerMove(pieces)
    onscreenclick(clicked)
mainloop()
