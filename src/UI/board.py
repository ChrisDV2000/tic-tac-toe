import PySimpleGUI as psg

class Board(object):
    def __init__(self, game, X, O) -> None:
        self.board = self.window(X, O)
        self.game = game
        self.game.num_turns = 0
        self.game.turn = 'X'
        while True:
            # if self.game.num_turns == 9:
            #     break
            self.event, self.values = self.board.read()
            if self.event == psg.WINDOW_CLOSED:
                break
            if self.event == 'r1c1':
                self.game.move(self)
                result = self.game.check_win(self)
            elif self.event == 'r2c1':
                self.game.move(self)
                result = self.game.check_win(self)
            elif self.event == 'r3c1':
                self.game.move(self)
                result = self.game.check_win(self)
            elif self.event == 'r1c2':
                self.game.move(self)
                result = self.game.check_win(self)
            elif self.event == 'r2c2':
                self.game.move(self)
                result = self.game.check_win(self)
            elif self.event == 'r3c2':
                self.game.move(self)
                result = self.game.check_win(self)
            elif self.event == 'r1c3':
                self.game.move(self)
                result = self.game.check_win(self)
            elif self.event == 'r2c3':
                self.game.move(self)
                result = self.game.check_win(self)
            elif self.event == 'r3c3':
                self.game.move(self)
                result = self.game.check_win(self)
            if result != 0:
                self.board.close()
                print(f'Player {result} is the winner')
                break

        self.board.close()

    def setup_layout(self, X, O):
        button_w = 10
        button_h = 4
        c1 = [
            [psg.Button(size=(button_w, button_h), key='r1c1')],
            [psg.Button(size=(button_w, button_h), key='r2c1')],
            [psg.Button(size=(button_w, button_h), key='r3c1')]
        ]
        c2 = [
            [psg.Button(size=(button_w, button_h), key='r1c2')],
            [psg.Button(size=(button_w, button_h), key='r2c2')],
            [psg.Button(size=(button_w, button_h), key='r3c2')]
        ]
        c3 = [
            [psg.Button(size=(button_w, button_h), key='r1c3')],
            [psg.Button(size=(button_w, button_h), key='r2c3')],
            [psg.Button(size=(button_w, button_h), key='r3c3')]
        ]
        self.layout = [
            [
                [psg.Text(' '.join([X, ', ', O]))],
                [psg.Text('X\'s go first')]
            ],
            [
                psg.Column(c1),
                psg.Column(c2),
                psg.Column(c3)
            ]
        ]
            

    def window(self, X, O):
        self.setup_layout(X, O)
        return psg.Window(title='Tic-Tac-Toe', layout=self.layout, margins=(100, 100))

    @staticmethod
    def update_tile(self):
        self.board[self.event].update(self.game.turn)
        

if __name__ == '__main__':
    board = Board()