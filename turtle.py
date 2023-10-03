
class Board:
    def __init__(self):
        self.board = {}
        self.empty()

    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col + row] = ' '

    def set(self, pos, label):
        self.board[pos] = label

    def draw(self):

        def print_borders():
            print(' ', end='')
            for _ in range(8):
                print('+---', end='')
            print('+')

        # prints out the column labels
        def print_col_labels():
            print('   ', end='')
            for col in 'abcdefgh':
                print(f'{col}', end='   ')
            print()

        print_col_labels()

        # prints boarders 
        print_borders()

        # prints chess board 
        for row in '87654321':
            print(f'{row}', end='')
            for col in 'abcdefgh':
                print(f'| {self.board[col + row]} ', end='')
            print(f'|{row}')
            print_borders()

        print_col_labels()

#parent class
class ChessPieces:
    def __init__(self, board, pos, color='white'):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())

    def get_index(self, pos):
        return 'abcdefgh'.index(pos[0]), '12345678'.index(pos[1])

    def get_name(self):
        pass

    def moves(self, board):
        pass

#childclass
class King(ChessPieces):
    def get_name(self):
        return 'K'

    def moves(self, board):
        directions = [(-1, - 1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        col, row = self.position
        col_names = 'abcdefgh'
        row_names = '12345678'
        for col_inc, row_inc in directions:
            new_col = col + col_inc
            new_row = row + row_inc

            if 0 <= new_col < 8 and 0 <= new_row < 8:
                new_pos = f'{col_names[new_col]}{row_names[new_row]}'
                board.set(new_pos, 'x')

#childclass
class Rook(ChessPieces):
    def get_name(self):
        return 'R'

    def moves(self, board):
        col, row = self.position
        col_names = 'abcdefgh'
        row_names = '12345678'

        for idx in range(8):
            if idx != row:
                current_pos = f'{col_names[col]}{row_names[idx]}'
                board.set(current_pos, 'x')

        for idx in range(8):
            if idx != col:
                current_pos = f'{col_names[idx]}{row_names[row]}'
                board.set(current_pos, 'x')

#child class
class Bishop(ChessPieces):
    def get_name(self):
        return 'B'

    def moves(self, board):
        col, row = self.position
        col_names = 'abcdefgh'
        row_names = '12345678'
    
        current_col, current_row = col, row
        while current_col < 8 and current_row >= 0:
            if current_col != col or current_row != row:
                current_pos = f'{col_names[current_col]}{row_names[current_row]}'
                board.set(current_pos, 'x')
            current_col += 1
            current_row -= 1

        current_col, current_row = col, row
        while current_col < 8 and current_row < 8:
            if current_col != col or current_row != row:
                current_pos = f'{col_names[current_col]}{row_names[current_row]}'
            current_col += 1
            current_row += 1
            board.set(current_pos, 'x')

        current_col, current_row = col, row
        while current_col >= 0 and current_row < 8:
            if current_col != col or current_row != row:
                current_pos = f'{col_names[current_col]}{row_names[current_row]}'
                board.set(current_pos, 'x')
            current_col -= 1
            current_row += 1

        current_col, current_row = col, row
        while current_col >= 0 and current_row >= 0:
            if current_col != col or current_row != row:
                current_pos = f'{col_names[current_col]}{row_names[current_row]}'
                board.set(current_pos, 'x')
            current_col -= 1
            current_row -= 1

#childclass
class Queen(ChessPieces):
    def get_name(self):
        return 'Q'

    def moves(self, board):

        col, row = self.position
        col_names = 'abcdefgh'
        row_names = '12345678'
        current_col, current_row = col, row
        while current_col < 8 and current_row >= 0:
            if current_col != col or current_row != row:
                current_pos = f'{col_names[current_col]}{row_names[current_row]}'
                board.set(current_pos, 'x')
            current_col += 1
            current_row -= 1

        current_col, current_row = col, row
        while current_col < 8 and current_row < 8:
            if current_col != col or current_row != row:
                current_pos = f'{col_names[current_col]}{row_names[current_row]}'
            current_col += 1
            current_row += 1
            board.set(current_pos, 'x')

        current_col, current_row = col, row
        while current_col >= 0 and current_row < 8:
            if current_col != col or current_row != row:
                current_pos = f'{col_names[current_col]}{row_names[current_row]}'
                board.set(current_pos, 'x')
            current_col -= 1
            current_row += 1

        current_col, current_row = col, row
        while current_col >= 0 and current_row >= 0:
            if current_col != col or current_row != row:
                current_pos = f'{col_names[current_col]}{row_names[current_row]}'
                board.set(current_pos, 'x')
            current_col -= 1
            current_row -= 1

        for idx in range(8):
            if idx != row:
                current_pos = f'{col_names[col]}{row_names[idx]}'
                board.set(current_pos, 'x')

        for idx in range(8):
            if idx != col:
                current_pos = f'{col_names[idx]}{row_names[row]}'
                board.set(current_pos, 'x')

#childclass
class Knight(ChessPieces):
    def get_name(self):
        return 'N'

    def moves(self, board):
        directions = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        col, row = self.position
        col_names = 'abcdefgh'
        row_names = '12345678'
        for col_inc, row_inc in directions:
            new_col = col + col_inc
            new_row = row + row_inc

            if 0 <= new_col < 8 and 0 <= new_row < 8:
                new_pos = f'{col_names[new_col]}{row_names[new_row]}'
                board.set(new_pos, 'x')


if __name__ == '__main__':
    b = Board()
    print('Welcome to the Chess Game!')
    b.draw()

    while True:
        piece = input('Enter a chess piece and its position or type X to exit: ')

        #will end program if x is typed
        if piece.lower() == 'x':
            break

        if len(piece) == 3:
            initials, col, row = piece[0], piece[1], piece[2]
            if col in 'abcdefgh' and row in '12345678':
                new_board = Board()
                if initials == 'K':
                    chess_piece = King(new_board, col + row)
                    chess_piece.moves(new_board)
                    new_board.draw()
                elif initials == 'Q':
                    chess_piece = Queen(new_board, col + row)
                    chess_piece.moves(new_board)
                    new_board.draw()
                elif initials == 'R':
                    chess_piece = Rook(new_board, col + row)
                    chess_piece.moves(new_board)
                    new_board.draw()
                elif initials == 'N':
                    chess_piece = Knight(new_board, col + row)
                    chess_piece.moves(new_board)
                    new_board.draw()
                elif initials == 'B':
                    chess_piece = Bishop(new_board, col + row)
                    chess_piece.moves(new_board)
                    new_board.draw()
                    
    print('\n')
