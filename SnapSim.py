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
    
    turnsPerSecond = 500
    
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
        handFinished = False
        hand = 0
        snapList = [];
        while not handFinished:
            hand += 1
            turn = 0
            Nsnaps = 0
            roundFinished = False
            while not roundFinished:
                turn += 1
                for player in self.players:
                    player.play()
                    
                    print('Turn %d' % turn)
                    print(self)
                    if self.checkSnaps(player):
                        Nsnaps +=1
                    time.sleep(1/self.turnsPerSecond)
                roundFinished = not self.anyoneCanPlay()
            snapList.append(Nsnaps)
            handFinished = all([n == 0 for n in snapList[-1:]])
            self.newHand()
            print('Hand %d' % hand)
        print(snapList)
        
    def newHand(self):
        for player in self.players:
            player.pickupPile()
        
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