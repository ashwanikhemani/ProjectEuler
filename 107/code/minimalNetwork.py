# -*- coding: utf-8 -*-
"""
@author: ashwa

Solution for Problem 107 : Minimal network

https://projecteuler.net/problem=107

"""
import sys
import numpy as np 
#import urllib.request as urlreq

import time

"""
Class to represent the given network

"""
class Network():
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.initialCost = 0
        self.totalCost = 0
        self.savings = 0
    """    
    Class to reprsent the output network
        
    """    
    class MstSet():
        def __init__(self):
            self.parent = None;
            self.weight = 0;
    """
    
    Function to find the vertex with minimum distance value from the set of vertices not included in the MST
    
    Parameters
    ----------
    weights : the weights of all vertices for the network 
    minSpanSet : The set containing the information about presence of a vertex in the minimumn spanning tree
        
    Returns
    -------
    out : int
         The index of vertex at the minimum distance not in the MST set 

    """
    def getMinVertex(self,weights, minsSpanSet):
        min_value = sys.maxsize
        min_index = -1 
        for v in range(self.vertices):
            if weights[v] < min_value and minsSpanSet[v] == False:
                min_value = weights[v]
                min_index = v 
        return min_index        
        
    """
    
    Function to construct and print the minimally connected network
    
    """
    
    def reduceNetwork(self):
        
       #The set containing the information about presence of a vertex in the minimumn spanning tree
        minSpanSet = [False]*self.vertices
        
       # list contaning the minimum weight edge for all vertices  
        weights = [sys.maxsize]*self.vertices        
        
       # object to represent the vertices of the output network
        mstSet = [self.MstSet() for vertex in range(self.vertices)]         
        
       # Initialize one vertex to zero to set the initial vertex 
        weights[0] = 0        
        
       # Set the first vertex as root having no parent.
        mstSet[0].parent = -1 
                
        
        for i in range(self.vertices):
            vertex = self.getMinVertex(weights,minSpanSet)            
            minSpanSet[vertex] = True            
            for j in range(self.vertices):
                if self.graph[vertex][j] > 0 and minSpanSet[j] == False and weights[j] > self.graph[vertex][j]:
                    weights[j] = self.graph[vertex][j]
                    mstSet[j].weight = self.graph[vertex][j]
                    mstSet[j].parent = vertex
        
        self.printNetwork(mstSet)
            
    """
    
    Function to get the reduced network , the cost of the reduced network
    and the savings achieved 
    
    Parameters
    ----------
    mstSet : The set containing the mininum spanning vertexes

    """
    def printNetwork(self,mstSet):
        print("\nThe reduced network is:")
        file = open("reducedNetwork.txt","w")
        for i in range(1,self.vertices):
            file.write("Edge: {}-{} weight: {} \n".format(i,mstSet[i].parent,mstSet[i].weight))
            print("Edge: {}-{} weight: {} ".format(i,mstSet[i].parent,mstSet[i].weight))
            self.totalCost = self.totalCost + mstSet[i].weight        

        # get the savings from the network 
        self.savings = self.initialCost-self.totalCost    

        print("\nThe savings which can be achieved for the network : {} ".format(self.savings))
    
    
    def createNetwork(self,fileName):
        
        # fetch file from the URL (could affect runtime if the connection is slow)
        # NETWORK_URL = 'https://projecteuler.net/project/resources/p107_network.txt'    
        # urlreq.urlretrieve(NETWORK_URL, "p107_network.txt")   
    
        # read the adjacency matrix for the given network    
        self.graph = np.loadtxt(fileName, dtype='str' , delimiter=',')
        
        # not defined edge weights initialized to zero 
        self.graph[self.graph == '-'] = 0
        self.graph = self.graph.astype(np.int)
    
        # get the initial cost of the network 
        self.initialCost = np.triu(self.graph).sum()
        print("The initial cost of the network: {} ".format(self.initialCost))
        
        

def main():
    
    start_time = time.time()

    """Minimal network"""
    # Create a network for the given number of vertices 
    network = Network(40)
    file_input = "p107_network.txt"
    network.createNetwork(file_input)
    
    # reduced the network using minimum spanning tree
    network.reduceNetwork()
        
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()