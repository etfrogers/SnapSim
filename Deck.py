#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:22:04 2017

@author: user
"""
import random

class Card:
    def __init__(self, val, col):
        self.value = val
        self.color = col
    
class Deck:
    
    def __init__(self,Ncolors,Nvals):
        self.cards = []
        self.Ncolors = Ncolors;
        self.Nvals = Nvals;
        self.fill()
        
    def fill(self):
        for val in range(self.Nvals):
            for col in range(self.Ncolors):
                self.cards.append(Card(val,col))
                
    def shuffle(self):
        random.shuffle(self.cards)

