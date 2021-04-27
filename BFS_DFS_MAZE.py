











































class state:
      def __init__(self, i, j, parent):    
        self.i = i
        self.j = j
    #    self.maze = maze
        self.parent = parent
    #    self.cost = cost
        
start = state(4, 11, None)
end = state(10, 0, None)
visited = []
current = start
    
maze =    [[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
           [ 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1,0], 
           [ 0, 1, 0, 1, 0, 1, 0, 0, 0, 0 ,1,0], 
           [ 0, 0, 0, 1, 0, 1, 1, 1, 1, 0 ,1,0], 
           [ 0, 1, 1, 1, 1, 0, 0, 0, 1, 0 ,1,1], 
           [ 0, 0, 0, 0, 1, 0, 1, 0, 1, 0 ,1,0], 
           [ 0, 1, 1, 0, 1, 0, 1, 0, 1, 0 ,1,0], 
           [ 0, 0, 1, 0, 1, 0, 1, 0, 1, 0 ,1,0], 
           [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 0 ,1,0],
           [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 ,1,0],
           [ 1, 1, 1, 1, 1, 1, 1, 0, 1, 1 ,1,0],
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0,0]]



def notVisited(x, y):
    
    visit = True
    
    for check in visited:
        if (x == check.i and y == check.j):
            visit = False
     
    return visit
            #put visited functionality
        


def bfs(maze):
    
    queue = []
    queue.append(start)
    current = start
    cost = 0
    
    while not(current.i == end.i and current.j == end.j):
    
    
        current = queue.pop(0)

        print(current.i,current.j)
    
           
        visited.append(current) 
        cost = cost+1 
    
       
    #    print(visited[0].j)
        
       # check up 
        if (current.i > 0):    
       
            if (maze[current.i-1][current.j] == 1 and notVisited(current.i-1, current.j)): 
                queue.append(state(current.i-1, current.j, current))
        
        
       # check left 
        if (current.j > 0):    
       
            if (maze[current.i][current.j-1] == 1 and notVisited(current.i, current.j-1)):  
                queue.append(state(current.i, current.j-1, current))
   
    
       # check right 
        if (current.j < 11):    
            if (maze[current.i][current.j+1] == 1 and notVisited(current.i, current.j+1)):  
                queue.append(state(current.i, current.j+1, current))
  
        if (current.i < 11):    
     
            if (maze[current.i+1][current.j] == 1 and notVisited(current.i+1, current.j)):  
                queue.append(state(current.i+1, current.j, current))
   
   
        
    print("BFS Total Cost: ", cost)

def dfs(maze):
    
    stack = []
    stack.append(start)
    current = start
    cost = 0
    
    while not(current.i == end.i and current.j == end.j):
    
    
        current = stack.pop(0)

        print(current.i,current.j)
    
           
        visited.append(current) 
        cost = cost+1 
    
       
    #    print(visited[0].j)
        
       # check up 
        if (current.i > 0):    
       
            if (maze[current.i-1][current.j] == 1 and notVisited(current.i-1, current.j)):  # if path
        
                stack.append(state(current.i-1, current.j, current))
        
        
       # check left 
        if (current.j > 0):    
       
            if (maze[current.i][current.j-1] == 1 and notVisited(current.i, current.j-1)):  # if path
    
                stack.append(state(current.i, current.j-1, current))
   
    
       # check right 
        if (current.j < 11):    
            if (maze[current.i][current.j+1] == 1 and notVisited(current.i, current.j+1)):  # if path

                stack.append(state(current.i, current.j+1, current))
  
        if (current.i < 11):    
     
            if (maze[current.i+1][current.j] == 1 and notVisited(current.i+1, current.j)):  # if path

                stack.append(state(current.i+1, current.j, current))
   
   
        
    print("DFS Total Cost: ", cost)
        


