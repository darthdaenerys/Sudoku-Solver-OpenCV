import cv2
import numpy as np
import time
import sys
from SudokuSolver import Sudoku

print('Enter your Sudoku board (0 refers to a blank space)')

sudoku=[]
for i in range(9):
    temp = list(map(int, input().split()))
    sudoku.append(temp)
    
# create window and set properties
cv2.namedWindow("Sudoku Solver",cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Sudoku Solver',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

# setup mouse call function
def mouseCall(event,xpos,ypos,*args):
    if mySudoku.flag and event==cv2.EVENT_LBUTTONDOWN:
        if xpos>int(mySudoku.width-mySudoku.width*0.31) and xpos<int(mySudoku.width-mySudoku.width*0.14) and ypos>int(mySudoku.height*0.3) and ypos<int(mySudoku.height*0.4):
            t1=time.time()
            result=mySudoku.solveSudoku(sudoku,0,0)
            t2=time.time()
            if result==False:
                cv2.putText(mySudoku.board,"Impossible to solve!",(int(mySudoku.width-mySudoku.width*0.42),int(mySudoku.height*0.8)),mySudoku.myFont,1.5,mySudoku.textcolour,3)
            else:
                cv2.putText(mySudoku.board,"Time to solve: ",(int(mySudoku.width-mySudoku.width*0.42),int(mySudoku.height*0.8)),mySudoku.myFont,2,mySudoku.textcolour,3)
                cv2.putText(mySudoku.board,f'{round(t2-t1,4)} secs',(int(mySudoku.width-mySudoku.width*0.4),int(mySudoku.height*0.9)),cv2.FONT_HERSHEY_PLAIN,4,mySudoku.textcolour,3)
            cv2.imshow("Sudoku Solver",mySudoku.board)
            cv2.waitKey(3000)
            cv2.destroyAllWindows()
            sys.exit()

cv2.setMouseCallback('Sudoku Solver',mouseCall)

# The sudoku object
mySudoku=Sudoku(sudoku)

# The welcome screen
bg=cv2.blur(mySudoku.board,(18,18))
cv2.putText(bg,'Welcome to Sudoku Solver',(mySudoku.width//2-250,mySudoku.height//2+10),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv2.imshow('Sudoku Solver',bg)
cv2.waitKey(1200)
mySudoku.board[:,:]=mySudoku.bgcolor

mySudoku.board=mySudoku.makeBoard()
mySudoku.putNumbers(sudoku)
cv2.putText(mySudoku.board,'Sudoku',(int(mySudoku.width-mySudoku.width*0.32),int(mySudoku.height*0.16)),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)

# Solve button
cv2.rectangle(mySudoku.board,(int(mySudoku.width-mySudoku.width*0.31),int(mySudoku.height*0.3)),(int(mySudoku.width-mySudoku.width*0.14),int(mySudoku.height*0.4)),(0,0,0),-1)
cv2.line(mySudoku.board,(int(mySudoku.width-mySudoku.width*0.31),int(mySudoku.height*0.305)),(int(mySudoku.width-mySudoku.width*0.31),int(mySudoku.height*0.4)),(255,255,255),2)
cv2.line(mySudoku.board,(int(mySudoku.width-mySudoku.width*0.31),int(mySudoku.height*0.4)),(int(mySudoku.width-mySudoku.width*0.142),int(mySudoku.height*0.4)),(255,255,255),2)
cv2.putText(mySudoku.board,'SOLVE',(int(mySudoku.width-mySudoku.width*0.3),int(mySudoku.height*0.38)),mySudoku.myFont,2,(255,255,255),3)

# program loop
while True:
    # display the board
    cv2.imshow("Sudoku Solver",mySudoku.board)

    # check quit conditions
    if cv2.waitKey(1) & 0xff==ord('q'):
        mySudoku.displayS(sudoku)
        break
cv2.destroyAllWindows()
