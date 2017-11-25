#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:12:35 2017

@author: user
"""

class Player:
    
    def __init__(self):
        self.hand = []
        self.pile = []
        
    def play(self):
        self.pile.append(self.hand.pop(0))