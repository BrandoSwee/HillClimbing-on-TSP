# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:33:53 2021

@author: Brandon
"""
# A node to hold states
class Node(object):
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost