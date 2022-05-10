# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:44:15 2021

@author: Brandon
"""
from Node import Node
import numpy as np
import random
import copy 

# Creates a start from board. 
# It always makes 0 your home.
def makeStart(board):
    size = board.shape[0]
    #I'll use 0 as my home.
    path = [0]
    morePath = []
    for i in range(1, size):
        morePath.append(i)
    #Shuffle all other numbers in path.
    random.shuffle(morePath)
    path = path + morePath
    cost = generateCost(board, path)
    myNode = Node(path, cost)
    return myNode

# This is hillclimbing neighbor node creator.
# Makes all possible swaps that don't move home
# and checks which is smallest.
def runOffStart(board,current):
    size = board.shape[0]
    path = current.path
    testPaths = []
    # Initialize return value
    val = Node(None, None)
    for i in range(1,size - 1):
        for j in range(i + 1, size):
            newPath = path
            temp = newPath[i]
            newPath[i] = newPath[j]
            newPath[j] = temp
            testPaths.append(newPath)
    # Now we need to find the best cost
    # from the new nodes.
    while(len(testPaths) > 0):
        pathState = testPaths.pop(0)
        cost = generateCost(board, pathState)
        if(val.cost == None):
            val = Node(pathState, cost)
        elif(val.cost > cost):
            val = Node(pathState, cost)
    return val

## Takes a board and path and
## returns the cost of the path.
def generateCost(board, path):
    total = 0
    for i in range(0, len(path) - 1):
        ### [row][column]
        total += board[path[i]][path[i + 1]]
    #We need to return home.
    total += board[path[-1]][path[0]]
    return total

# The hillclimbing function takes a board
# and performs normal hillclimbing with no random restart.
def hillclimbing(board, plt):
    current = 0
    neighbor = 0
    current = makeStart(board)
    plt.append(current.cost)
    # Will go 10 times at max before returning a value.
    #for in range(0, 10)
    ### Now we go until we have a local minimum.
    while True:
        neighbor = runOffStart(board,copy.deepcopy(current))
        if(neighbor.cost >= current.cost):
            return current
        current = neighbor
        plt.append(current.cost)
    #Not used
    return current


    