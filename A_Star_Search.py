#!/usr/bin/env python
# coding: utf-8

# In[6]:


# This class represent a graph
class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
            
    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
                
    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
            
    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
        
    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
    
# This class represent a node
class Node:
    
    # Initialize the class
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
        
     # Compare nodes
    def __eq__(self, other):
        return self.name == other.name
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))
    
# A* search
   
def A_Star(graph, heuristics, start, end):
    
    # Create lists for open nodes and closed nodes
        openNodes = []
        closedNodes = []
    # Create a start node and an goal node
        startNode = Node('Arad', None)
        goalNode = Node('Bucharest', None)
        currentNode = Node('Arad', None)
       
    
    # Add the start node
        openNodes.append(startNode)
    
    # Loop until the open list is empty
        low = 600
       # while(openNodes):
        
        city = graph.get(startNode.name)
        
        print(city)
        
        for i in city:
            openNodes.append(Node(i,None))
            if city[i] + heuristics[i] < low:
                nextDestination = i
                low = city[i] + heuristics[i]
                
                
        print("low: ", low)        
        # Sort the open list to get the node with the lowest cost first
        
        
        
        # Get the node with the lowest cost
        
        # Add the current node to the closed list

        closedNodes = currentNode
        
        # Check if we have reached the goal, return the path (From Current Node to Start Node By Node.parent)
        
        if (currentNode.Name == 'Bucharest'):
            print("Reached Goal")

        
            # Return reversed path (Hint: Return Llist of path in this Fashion for Reverse return path[::-1])
            
        # Get neighbours
        neighbors = graph.get(current_node.name)
        
        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
    
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            # Calculate cost to goal
            
            # Check if neighbor is in open list and if it has a lower f value
            if(In_Open(open1, neighbor) == True):
                # Everything is green, add neighbor to open list
                continue
                
                
    # Return None, no path is found
   
# Check if a neighbor should be added to open list
def In_Open(open, neighbor):      
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True


# The main entry point for this module
def main():
    # Create a graph
    graph = Graph()
    
    # Create graph connections (Actual distance)
    graph.connect('Arad', 'Zerind', 75)
    graph.connect('Arad', 'Timisoara', 118)
    graph.connect('Arad', 'Sibiu', 140)
    
    graph.connect('Oradea', 'Zerind', 90)
    graph.connect('Oradea', 'Sibiu', 151)
    
    graph.connect('Timisoara', 'Lugoj', 111)
    graph.connect('Lugoj', 'Mehadia', 70)
    graph.connect('Mehadia', 'Dobreta', 75)
    graph.connect('Dobreta', 'Cralova', 170)
  
    graph.connect('Cralova', 'Pitesti', 170)
    graph.connect('Cralova', 'Rimnicu Vilcea', 138)

    graph.connect('Rimnicu Vilcea', 'Sibiu', 80)
    graph.connect('Rimnicu Vilcea', 'Pitesto', 97)

    
    graph.connect('Sibiu', 'Fagaras', 99)

     # Add Remaining Links From Example Given in Sides (Romania Map)
    graph.connect('Fugaras', 'Bucharest', 211)
    graph.connect('Pitesti', 'Bucharest', 101)
   

    
    
    # Make graph undirected, create symmetric connections
    graph.make_undirected()
    
    # Create heuristics (straight-line distance, air-travel distance) for Destination Bucharest
    heuristics = {}
    heuristics['Arad'] = 366
    heuristics['Timisoara'] = 329
    heuristics['Lugoj'] = 224
    heuristics['Mehadia'] = 241
    heuristics['Dobreta'] = 242
    heuristics['Sibiu'] = 253
    heuristics['Cralova'] = 160
    heuristics['Pitesti'] = 10
    heuristics['Rimnicu Vilcea'] = 193
    heuristics['Fagaras'] = 176
    heuristics['Zerind'] = 374
    
    
    # Add Remaining Heuristics From Example Given in Sides (Romania Map)
    heuristics['Bucharest'] = 0
    
    # Print Graph Nodes
    print(graph.nodes())
    print('\n')
    
    l = (graph.get('Arad'))
   
    print(l['Zerind'])
   
    print(heuristics['Arad'])
    
    # Run search algorithm
    path = A_Star(graph, heuristics, 'Arad', 'Bucharest')
    print('Paths')
    print(path)
    
# Tell python to run main method
if __name__ == "__main__": main()


# In[ ]:




