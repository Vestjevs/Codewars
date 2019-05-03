import random


class Cell:
    def __init__(self, mined, is_visible=False, is_flagged=False):
        self.is_visible = is_visible
        self.mined = mined
        self.is_flagged = is_flagged

    def open(self):
        if not self.is_flagged:
            self.is_visible = True

    def flag(self):
        self.is_flagged = not self.is_flagged

    def place_mine(self):
        self.mined = True


class Controller:

    def get_move(self):
        move = input('Enter your move: ')
        return [int(move[0]), int(move[1]), True if move[-1] == 'f' else False]

    def start(self, board, mines):
        board.generate_mines(mines)
        while board.is_playing and not board.is_solved():
            print(board.show())
            (row_index, col_index, is_flag) = self.get_move()
            if is_flag:
                board.flag(row_index, col_index)
            else:
                board.open(row_index, col_index)
        if not board.is_playing:
            board.open_all_mines()
        print('U found mine \n' + board.show())


class Board:
    def __init__(self, size):
        self.board = [[Cell(False) for i in range(size)] for i in range(size)]
        self.is_playing = True

    def open_all_mines(self):
        for row in self.board:
            for element in row:
                if element.mined and not element.is_visible:
                    element.open()

    def count_surround(self, row_index, col_index):
        counter = 0
        for (row, col) in self.get_neighbours(row_index, col_index):
            if self.is_in_range(row, col) and self.board[row][col].mined:
                counter += 1
        return counter

    def is_in_range(self, row_index, col_index):
        return 0 <= row_index < len(self.board) and 0 <= col_index < len(self.board)

    def show(self):
        game_state = 'Mines:  ' + str(self.remaining_mines()) + '\n' + '  ' + ' '.join(
            '| {} |'.format(str(i)) for i in range(len(self.board)))
        for row_index in range(len(self.board)):
            game_state += '\n' + str(row_index) + ' '
            for col_index in range(len(self.board)):
                if self.board[row_index][col_index].is_visible:
                    if self.board[row_index][col_index].mined:
                        game_state += '[ M ] '
                    else:
                        game_state += '[ ' + str(self.count_surround(row_index, col_index)) + ' ] '
                elif self.board[row_index][col_index].is_flagged:
                    game_state += '[ F ] '
                else:
                    game_state += '[   ] '
            game_state += str(row_index)
        game_state += '\n' + '  ' + ' '.join('| {} |'.format(str(i)) for i in range(len(self.board)))
        return game_state

    def generate_mines(self, mines):
        valid_position = list(range((mines - 1) * (mines - 1)))
        for i in range(mines):
            new_pos = random.choice(valid_position)
            valid_position.remove(new_pos)
            row_index = new_pos // int(mines)
            col_index = new_pos % int(mines)
            self.place_mine(row_index, col_index)

    def place_mine(self, row_index, col_index):
        self.board[row_index][col_index].place_mine()

    def flag(self, row_index, col_index):
        if not self.board[row_index][col_index].is_visible:
            self.board[row_index][col_index].flag()
        else:
            print("U can't flag, it's visible")

    def remaining_mines(self):
        counter = 0
        for row in self.board:
            for element in row:
                if element.mined:
                    counter += 1
                elif element.is_flagged:
                    counter -= 1
        return counter

    def open(self, row_index, col_index):
        if not self.board[row_index][col_index].is_visible:
            self.board[row_index][col_index].open()

            if self.board[row_index][col_index].mined and not self.board[row_index][col_index].is_flagged:
                self.is_playing = False
            elif self.count_surround(row_index, col_index) == 0:
                [self.open(surround_row, surround_col) for (surround_row, surround_col) in
                 self.get_neighbours(row_index, col_index) if self.is_in_range(surround_row, surround_col)]

    @staticmethod
    def get_neighbours(row_index, col_index):
        surrounding = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        neighbours = []
        for (row, col) in surrounding:
            neighbours.append((row_index + row, col_index + col))
        return neighbours

    def is_solved(self):
        for row in self.board:
            for element in row:
                if not (element.is_visible or element.is_flagged):
                    return False
        return True


def main():
    size = 10
    mines = 9
    board = Board(size)
    controller = Controller()
    controller.start(board, mines)


if __name__ == '__main__':
    main()
