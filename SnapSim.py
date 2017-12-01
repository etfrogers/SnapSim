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
import matplotlib.pyplot as plt

class SnapSim:
    
    turnsPerSecond = 200
    
    def __init__(self, Nplayers, Nvals, Ncolors):
        
        self.players = [Player.Player() for ii in range(Nplayers)]
        self.deck = Deck.Deck(Nvals, Ncolors)
        self.nSnaps = []
        self.showOutput = False
        
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
                    if self.showOutput:
                        print('Turn %d' % turn)
                        self.show()
                    if self.checkSnaps(player):
                        Nsnaps +=1
                    if self.turnsPerSecond<100:
                        time.sleep(1/self.turnsPerSecond)
                roundFinished = not self.anyoneCanPlay()
            snapList.append(Nsnaps)
            handFinished = all([n == 0 for n in snapList[-1:]])
            self.newHand()
            if self.showOutput:
                print('Hand %d' % hand)
        self.nSnaps = snapList
        if self.showOutput:
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
                val2 = lastPlayer.pile[-1].value if len(lastPlayer.pile) >0 else None
                col1 = player.pile[-1].color if len(player.pile) >0 else None
                col2 = lastPlayer.pile[-1].color if len(lastPlayer.pile) >0 else None

                if (val1 is not None) and ((val1 == val2) or (col1 == col2)):
                    self.snap(player, lastPlayer)
                    didSnap = True
                    break
        return didSnap
        
        
    def snap(self, player1, player2):
        winner = random.choice(self.players)
        winnerNo = self.players.index(winner)+1
        if self.showOutput:
            print('SNAP!')
            print('Winner was player %d' % winnerNo)
        winner.hand.insert(0, player1.pile.pop(-1))
        winner.hand.insert(0, player2.pile.pop(-1))
        
    def show(self):
        if self.showOutput:
            print(self) 
        
    def __str__(self):
        string = '';
        for ii in range(len(self.players[0].status())):
            string += ''.join([player.status()[ii] for player in self.players])
            string += '\n'
        return string
                
        
def main():
    nSims = 100
    sim = SnapSim(2,8,4)
    snaps = []
    for i in range(nSims):
        sim.run()
        snaps.append(sim.nSnaps)
    print(snaps)
    
    for snapList in snaps:
        plt.plot(snapList)
    #plt.legend()
    plt.show()
    
if __name__ == '__main__':
    main()