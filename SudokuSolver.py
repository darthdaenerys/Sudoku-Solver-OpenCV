# import modules and libraries
import cv2
import numpy as np
import time

# The head Sudoku class
class Sudoku:
    def __init__(self,input_matrix):
        self.width=1280
        self.height=720
        self.bgcolor=(103,25,107)
        self.board=np.zeros([self.height,self.width,3],dtype=np.uint8)
        self.cellsize=70
        self.cellstartcorner=(50,50)
        self.myFont=cv2.FONT_HERSHEY_SIMPLEX
        self.digitcolour=(35,162,186)
        self.textcolour=(43,224,61)
        self.flag=True
        self.cntr=0

    # make grid lines
    def makegrid(self):
        j=0
        for i in range(self.cellstartcorner[0],self.cellstartcorner[0]+self.cellsize*10,self.cellsize):
            if j%3==0:
                cv2.line(self.board,(i,self.cellstartcorner[0]),(i,self.cellstartcorner[0]+self.cellsize*9),(0,0,0),3)
            cv2.line(self.board,(i,self.cellstartcorner[0]),(i,self.cellstartcorner[0]+self.cellsize*9),(0,0,0),2)
            j+=1
        j=0
        for i in range(self.cellstartcorner[1],self.cellstartcorner[1]+self.cellsize*10,self.cellsize):
            if j%3==0:
                cv2.line(self.board,(self.cellstartcorner[1],i),(self.cellstartcorner[1]+self.cellsize*9,i),(0,0,0),3)
            cv2.line(self.board,(self.cellstartcorner[1],i),(self.cellstartcorner[1]+self.cellsize*9,i),(0,0,0),2)
            j+=1
        return self.board
    
    # function to clear the board
    def makeBoard(self):
        self.board[:,:]=self.bgcolor
        self.board=self.makegrid()
        return self.board
    
    # fill the grid with user's input
    def putNumbers(self,input_matrix):
        ycell=self.cellstartcorner[1]+int(self.cellstartcorner[1]*1.1)
        for i in range(9):
            xcell=self.cellstartcorner[0]+int(self.cellstartcorner[0]*0.3)
            for j in range(9):
                if input_matrix[i][j]!=0:
                    cv2.putText(self.board,str(input_matrix[i][j]),(xcell,ycell),self.myFont,2,(35,142,166),3)
                xcell+=self.cellsize
            ycell+=self.cellsize
        return self.board
    
    # check safe consition
    def isSafe(self,input_matrix,row,col,num):
        xblock=row-row%3
        yblock=col-col%3
        for i in range(9):
            if input_matrix[row][i]==num:
                return False
        for i in range(9):
            if input_matrix[i][col]==num:
                return False
        for i in range(xblock,xblock+3,1):
            for j in range(yblock,yblock+3,1):
                if input_matrix[i][j]==num:
                    return False
        return True

    # helper function to output sudoku matrix on terminal (if required)
    def displayS(self,input_matrix):
        print('---------------------------')
        [print(_) for _ in input_matrix]
        print('---------------------------')
    
    # solve sudoku function
    def solveSudoku(self,input_matrix,row,col):
        if row==8 and col==9:
            return True
        if col==9:
            row+=1
            col=0
        if input_matrix[row][col]!=0:
            return self.solveSudoku(input_matrix,row, col+1)
        for i in range(1,10,1):
            if self.isSafe(input_matrix,row, col, i):
                input_matrix[row][col]=i
                if self.solveSudoku(input_matrix,row, col+1):
                    self.putNumbers(input_matrix)
                    return True
            input_matrix[row][col]=0
            self.cntr+=1
            self.putNumbers(input_matrix)
            if self.cntr%50==0:
                cleanboard=self.makeBoard()
                self.board=cleanboard
                self.putNumbers(input_matrix)
                cv2.imshow("Sudoku Solver",self.board)
                cv2.waitKey(1)
        return False

if __name__=='__main__':
    # sample test case
    # --------------
    sudoku=[
        [0,2,0,6,0,8,0,0,0],
        [5,8,0,0,0,9,7,0,0],
        [0,0,0,0,4,0,0,0,0],
        [3,7,0,0,0,0,5,0,0],
        [6,0,0,0,0,0,0,0,4],
        [0,0,8,0,0,0,0,1,3],
        [0,0,0,0,2,0,0,0,0],
        [0,0,9,8,0,0,0,3,6],
        [0,0,0,3,0,6,0,9,0]
    ]
    # ---------------

    print('All set to go!')