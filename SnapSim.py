#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:04:30 2017

@author: user
"""
import Player
import Deck
import random
import time

class SnapSim:
    
    turnsPerSecond = 50
    
    def __init__(self, Nplayers, Nvals, Ncolors):
        
        self.players = [Player.Player() for ii in range(Nplayers)]
        self.deck = Deck.Deck(Nvals, Ncolors)
        
    def deal(self):
        self.deck.shuffle()
        playerInd = 0
        for card in self.deck.cards:
            self.players[playerInd].hand.append(card)
            playerInd = (playerInd+1)%len(self.players)
    
    def run(self):
        self.deal()
        finished = False
        turn = 0
        Nsnaps = 0;
        while not finished:
            turn += 1
            for player in self.players:
                player.play()
                
                print('Turn %d' % turn)
                print(self)
                if self.checkSnaps(player):
                    Nsnaps +=1
                time.sleep(1/self.turnsPerSecond)
            finished = not self.anyoneCanPlay()
        print(Nsnaps)
    def anyoneCanPlay(self):
        return any([p.canPlay() for p in self.players])
            
    def checkSnaps(self, lastPlayer):
        #player who just played against all other piles 
        didSnap = False
        for player in self.players:
            if player is not lastPlayer:
                val1 = player.pile[-1].value if len(player.pile) >0 else None
                val2 = lastPlayer.pile[-1].value #player has just played, so pile is not empty
                if val1 == val2:
                    self.snap(player, lastPlayer)
                    didSnap = True
                    break
        return didSnap
        
        
    def snap(self, player1, player2):
        print('SNAP!')
        winner = random.choice(self.players)
        winnerNo = self.players.index(winner)+1
        print('Winner was player %d' % winnerNo)
        #TODO switch cards
        winner.hand.insert(0, player1.pile.pop(-1))
        winner.hand.insert(0, player2.pile.pop(-1))
        
    def show(self):
        print(self)
        
    def __str__(self):
        string = '';
        for ii in range(len(self.players[0].status())):
            string += ''.join([player.status()[ii] for player in self.players])
            string += '\n'
        return string
                
        
def main():
    sim = SnapSim(2,8,4)
   
    sim.run()
    
    
if __name__ == '__main__':
    main()