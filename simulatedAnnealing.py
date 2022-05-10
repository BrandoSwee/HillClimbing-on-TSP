# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:42:20 2021

@author: Brandon
"""
from hillclimbing import makeStart, generateCost
from Node import Node
import random
import math
import copy

# Performs simulated Annealing
def Anneal(board, schedule, plt):
    current = 0
    nextNode = 0
    t = 0
    current = makeStart(board)
    plt.append(current.cost)
    while True:
        T = schedule[t]
        if(T == 0):
            return current
        nextNode = randomSuccessor(board, copy.deepcopy(current))
        deltaE = nextNode.cost - current.cost
        if(deltaE < 0):
            current = nextNode
            plt.append(current.cost)
        else:
            ## Was getting an overflow error. So I
            ## assume it's giving me an incredibly 
            ## small number that python floats can't hold.
            try:
                num = (1/(math.exp(deltaE/T))) * 100
            except OverflowError:
                num = 0
            # I decide to round
            # This could be seen as bad. I don't really know.
            num = round(num)
            randNum = random.randint(1, 100)
            if(num >= randNum):
                current = nextNode
                plt.append(current.cost)
        t += 1

# randomSuccessor takes the board and the current state
# With these it generates a random move.
def randomSuccessor(board, current):
    size = board.shape[0]
    # This should never get touched.
    # But it sort of popped into my mind.
    if(size == 2):
        return current
    ######################################
    arr = []
    ### I don't want to pop my starting location.
    for i in range(1, size):
        arr.append(i)
    val1 = arr.pop(random.randint(0, size - 2))
    val2 = arr.pop(random.randint(0, size - 3))
    newPath = current.path
    temp = newPath[val1]
    newPath[val1] = newPath[val2]
    newPath[val2] = temp
    cost = generateCost(board, newPath)
    returnNode = Node(newPath, cost)
    return returnNode
    