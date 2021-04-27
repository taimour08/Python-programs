
import random
import numpy as np

#create 2D numpy array with zeros
board = np.zeros((8, 8))
conflicts = 0

#print numpy array

for i in range(0,8):
    j = random.randint(0, 7)
    board[i][j] = 1
   
   
print(board)


def objectiveFunction(board):
    
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] == 1:
                computeConflicts(i,j)
                break

    print("Total Conflicts:", conflicts)
    
def computeConflicts(i,j):

    global conflicts
 
 # Check for below    
    x = i + 1
    while(x < 8):
        if board[x][j] == 1:
          print(x,",",j)
          conflicts += 1
        x += 1
     
   
    x = i + 1 
    y = j + 1

#check right diagnol    
    while (x < 8 and y < 8):
        if board[x][y] == 1:
           print(x,",",y)
           conflicts += 1
        x += 1
        y += 1
 
    x = i + 1 
    y = j - 1
 
#check left diagnol    
    while (x < 8 and y > 0):
        if board[x][y] == 1:
            print(x,",",y)
            conflicts += 1
        x += 1
        y -= 1
                        
        
   
    
objectiveFunction(board)

    
        

    