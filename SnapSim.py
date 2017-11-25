#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:04:30 2017

@author: user
"""
import Player
import Deck

class SnapSim:
    
    def __init__(self, Nplayers, Ncolors, Nvals):
        
        self.players = [Player.Player() for ii in range(Nplayers)]
        self.deck = Deck.Deck(Ncolors, Nvals)
        
    def deal(self):
        self.deck.shuffle()
        playerInd = 0
        for card in self.deck.cards:
            self.players[playerInd].hand.append(card)
            playerInd = (playerInd+1)%len(self.players)
    
    def run(self):
        self.deal()
        finished = False
        while not finished:
            for player in self.players:
                player.play()
                
            finished = True
                

def main():
    sim = SnapSim(2,8,4)
    print(SnapSim)
    
    sim.run()
    
    
if __name__ == '__main__':
    main()