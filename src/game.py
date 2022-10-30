import PySimpleGUI as psg
import random
from UI.board import Board

from UI.main_win import Main_Win

class Game(object):
    def __init__(self) -> None:
        self.spaces = [
            'r1c1', 'r1c2', 'r1c3',
            'r2c1', 'r2c2', 'r2c3',
            'r3c1', 'r3c2', 'r3c3',
        ]
    
    @staticmethod
    def move(self):
        if self.event not in self.game.spaces:
            Main_Win.popup()
        else:
            self.game.spaces.remove(self.event)
            self.game.num_turns += 1
            Board.update_tile(self)
            if self.game.turn == 'X' and self.game.num_turns != 0:
                self.game.turn = 'O'
            elif self.game.turn == 'O':
                self.game.turn = 'X'

    def players(self, p1='Player 1', p2='Player 2'):       
        players = [p1, p2]
        if any(x for x in players if x.lower() == 'olivia'):
            for item in players:
                if item.lower() == 'olivia':
                    O = 'Olivia is O'
                elif item == '':
                    X = 'Player 1 is X'
                else:
                    X = item + ' is X'
            return X, O
        new_list = [x for x in players if x == '']
        if len(new_list) > 1:
            players.clear()
        if new_list != []:
            try:  
                players.remove('')
            except:
                pass
            for idx, _ in enumerate(new_list):
                players.append('Player ' + str(idx + 1))
        X = random.choice(players)
        players.remove(X)
        X = str(X) + ' is X'
        O = players[0] + ' is O'
        return X, O

    
        
