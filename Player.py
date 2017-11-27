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
        if self.canPlay():
            self.pile.append(self.hand.pop(0))
            
    def canPlay(self):
        return len(self.hand) > 0
    
    
    
    def status(self):
        try:
            topcard = str(self.pile[-1])
        except IndexError:
            topcard = '     '
            
        return      ('%3d  ' % len(self.hand),
                     '     ',
                     ' %s  '  % topcard,
                     '%3d  ' % len(self.pile))
    
    def __str__(self):
        return '\n'.join(self.status)