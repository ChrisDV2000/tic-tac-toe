import PySimpleGUI as psg
from UI.board import Board

class Main_Win(object):
    def __init__(self, game):
        self.window = self.main_win()
        while True:
            self.event, self.values = self.window.read()
            if self.event == psg.WINDOW_CLOSED:
                break
            if self.event == 'Start Game':
                X, O = game.players(self.values['P1'], self.values['P2'])
                self.board = Board(game, X, O)
                break
        self.window.close()



    def main_win(self):
        return psg.Window(title='Tic-Tac-Toe', layout=self.layout())

    def layout(self):
        return [
            [psg.Text('Welcome to the best game of Tic-Tac-Toe of your lifeeeee!!!!!')],
            [
                psg.Text("Player 1:"),
                psg.In(size=(25, 1), enable_events=True, key="P1")
            ],
            [
                psg.Text("Player 2:"),
                psg.In(size=(25, 1), enable_events=True, key="P2")
            ],
            [psg.Button('Start Game')]
        ]

    def popup():
        layout = [
            [psg.Text('You can\'t go here this place is already taken!!')],
            [psg.Button('OK')]
        ]
        while True:
            msg = psg.Window(title='Stop', layout=layout)
            event = msg.read()
            if event == 'OK' or event == psg.WINDOW_CLOSED:
                break
        msg.close()


if __name__ == '__main__':
    a = Main_Win()