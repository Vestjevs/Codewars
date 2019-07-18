import random


class Board:

    def __init__(self):
        self.board = [' ' for i in range(9)]

    def show(self):
        print("-------------")
        for i in range(3):
            print("| {} | {} | {} |".format(self.board[0 + i * 3], self.board[1 + i * 3], self.board[2 + i * 3]))
            print("-------------")

    def set_value_in_cell_variantA(self, player):
        cell_index = player.read_value_variantB(self)
        self.board[cell_index] = player.type

    def set_value_in_cell_variantB(self, player):
        valid = False
        while not valid:
            value = player.read_value_variantB(self)
            if self.is_the_cell_empty(value):
                self.board[value] = player.type
                valid = True
            else:
                print("This cell is engaged")

    def is_the_cell_empty(self, i):
        return self.board[i] == ' '

    def are_there_empty_cells(self):
        aux = False
        for item in self.board:
            aux = aux or item == ' '
        return aux

    def show_what_in_cell(self, i):
        return self.board[i]

    def check_critical_situation(self, player, i, j, k):
        b = self.board[i] != player.type and self.board[i] != ' ' \
            and self.board[j] != player.type and self.board[j] != ' ' \
            and self.board[k] == ' '
        return b

    def check_for_winning_position_with_one_empty_cell(self, player, i, j, k):
        b = self.board[i] == player.type and self.board[j] == player.type \
            and self.board[k] == ' '
        return b

    def check_for_winning_position_with_two_empty_cells(self, player, i, j, k):
        b = self.board[i] == player.type and self.board[j] == ' ' and self.board[k] == ' '
        return b

    def are_diagonal_cells_empty(self):
        b = False
        for index in range(3):
            b = self.board[4 * index] == ' '
        return b


class Game:

    def __init__(self):
        self.win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    # variant a
    def find_winner(self, board):
        for item in self.win_coord:
            if board.show_what_in_cell(item[0]) == 'X' and board.show_what_in_cell(item[1]) == 'X' \
                    and board.show_what_in_cell(item[2]) == 'X':
                return 'X'
            elif board.show_what_in_cell(item[0]) == 'O' and board.show_what_in_cell(item[1]) == 'O' \
                    and board.show_what_in_cell(item[2]) == 'O':
                return 'O'
        return None

    # # variant b
    # def check_win(self, table):
    #     for item in self.win_coord:
    #         if table.board[item[0]] != ' ' and table.board[item[1]] != ' ' and table.board[item[2]] != ' ':
    #             return True
    #     return False
    #
    # def find_name_of_winner(self, table):
    #     for item in self.win_coord:
    #         if table.board[item[0]] == 'X' and table.board[item[1]] == 'X' and table.board[item[2]] == 'X':
    #             return 'X'
    #         else:
    #             return 'O'
    #     return None

    def start_to_play(self, player1, player2, board):
        counter = 0
        while not self.find_winner(board):
            board.show()
            if counter % 2 == 0:
                board.set_value_in_cell_variantB(player1)
                # player1.read_and_insert_the_value(table)
            else:
                board.set_value_in_cell_variantB(player2)
                # player2.read_and_insert_the_value(table)
            counter += 1
            if counter > 4 and self.find_winner(board):
                print("End game, " + self.find_winner(board) + " is winner")
                break
            if not board.are_there_empty_cells():
                print("Draw, friendship won")
                break

        board.show()


class Player:

    def __init__(self, ch, name):
        self.type = str(ch)
        self.name = str(name)

    def read_and_insert_the_value(self, table):
        valid = False
        while not valid:
            value = int(input()) - 1
            if table.is_the_cell_empty(value):
                table.set_value_in_cell_variantA(value, self)
                valid = True
            else:
                print("This cell is engaged")

    @staticmethod
    def read_value_variantB(self):
        value = int(input()) - 1
        return value


class OrdinaryMachine:

    def __init__(self, ch, name):
        self.type = str(ch)
        self.name = str(name)

    @staticmethod
    def read_value_variantB(self):
        value = random.randint(0, 8)
        return value


class ShrewdMachine:

    def __init__(self, ch, name):
        self.type = str(ch)
        self.name = str(name)

    # def check_for_winning_position_with_one_empty_cell(self, table, i, j, k):
    #     b = table.show_what_in_cell(i) == self.type and table.show_what_in_cell(j) == self.type \
    #         and table.is_the_cell_empty(k)
    #     return b
    #
    # def check_for_winning_position_with_two_empty_cells(self, table, i, j, k):
    #     b = table.show_what_in_cell(i) == self.type and table.is_the_cell_empty(j) and table.is_the_cell_empty(k)
    #     return b

    def read_value_variantB(self, board):
        if board.check_for_winning_position_with_one_empty_cell(self, 0, 1, 2) \
                or board.check_for_winning_position_with_one_empty_cell(self, 8, 5, 2) \
                or board.check_for_winning_position_with_one_empty_cell(self, 6, 4, 2):
            value = 2
            return value
        elif board.check_for_winning_position_with_one_empty_cell(self, 0, 2, 1) \
                or board.check_for_winning_position_with_one_empty_cell(self, 7, 4, 1):
            value = 1
            return value
        elif board.check_for_winning_position_with_one_empty_cell(self, 1, 2, 0) \
                or board.check_for_winning_position_with_one_empty_cell(self, 6, 3, 0) \
                or board.check_for_winning_position_with_one_empty_cell(self, 8, 4, 0):
            value = 0
            return value
        elif board.check_for_winning_position_with_one_empty_cell(self, 3, 4, 5) \
                or board.check_for_winning_position_with_one_empty_cell(self, 2, 8, 5):
            value = 5
            return value
        elif board.check_for_winning_position_with_one_empty_cell(self, 3, 5, 4) \
                or board.check_for_winning_position_with_one_empty_cell(self, 1, 7, 4) \
                or board.check_for_winning_position_with_one_empty_cell(self, 0, 8, 4) \
                or board.check_for_winning_position_with_one_empty_cell(self, 2, 6, 4):
            value = 4
            return value
        elif board.check_for_winning_position_with_one_empty_cell(self, 5, 4, 3) \
                or board.check_for_winning_position_with_one_empty_cell(self, 0, 6, 3):
            value = 3
            return value
        elif board.check_for_winning_position_with_one_empty_cell(self, 6, 7, 8) \
                or board.check_for_winning_position_with_one_empty_cell(self, 2, 5, 8) \
                or board.check_for_winning_position_with_one_empty_cell(self, 0, 4, 8):
            value = 8
            return value
        elif board.check_for_winning_position_with_one_empty_cell(self, 6, 8, 7) \
                or board.check_for_winning_position_with_one_empty_cell(self, 1, 4, 7):
            value = 7
            return value
        elif board.check_for_winning_position_with_one_empty_cell(self, 7, 8, 6) \
                or board.check_for_winning_position_with_one_empty_cell(self, 0, 3, 6) \
                or board.check_for_winning_position_with_one_empty_cell(self, 2, 4, 6):
            value = 6
            return value

        # ----

        if board.check_critical_situation(self, 0, 1, 2) \
                or board.check_critical_situation(self, 8, 5, 2) \
                or board.check_critical_situation(self, 6, 4, 2):
            value = 2
            return value
        elif board.check_critical_situation(self, 0, 2, 1) \
                or board.check_critical_situation(self, 7, 4, 1):
            value = 1
            return value
        elif board.check_critical_situation(self, 1, 2, 0) \
                or board.check_critical_situation(self, 6, 3, 0) \
                or board.check_critical_situation(self, 8, 4, 0):
            value = 0
            return value
        elif board.check_critical_situation(self, 3, 4, 5) \
                or board.check_critical_situation(self, 2, 8, 5):
            value = 5
            return value
        elif board.check_critical_situation(self, 3, 5, 4) \
                or board.check_critical_situation(self, 1, 7, 4) \
                or board.check_critical_situation(self, 0, 8, 4) \
                or board.check_critical_situation(self, 2, 6, 4):
            value = 4
            return value
        elif board.check_critical_situation(self, 5, 4, 3) \
                or board.check_critical_situation(self, 0, 6, 3):
            value = 3
            return value
        elif board.check_critical_situation(self, 6, 7, 8) \
                or board.check_critical_situation(self, 2, 5, 8) \
                or board.check_critical_situation(self, 0, 4, 8):
            value = 8
            return value
        elif board.check_critical_situation(self, 6, 8, 7) \
                or board.check_critical_situation(self, 1, 4, 7):
            value = 7
            return value
        elif board.check_critical_situation(self, 7, 8, 6) \
                or board.check_critical_situation(self, 0, 3, 6) \
                or board.check_critical_situation(self, 2, 4, 6):
            value = 6
            return value

        # ------
        if board.check_for_winning_position_with_two_empty_cells(self, 0, 1, 2) \
                or board.check_for_winning_position_with_two_empty_cells(self, 8, 5, 2) \
                or board.check_for_winning_position_with_two_empty_cells(self, 6, 4, 2):
            value = 2
            return value
        elif board.check_for_winning_position_with_two_empty_cells(self, 0, 2, 1) \
                or board.check_for_winning_position_with_two_empty_cells(self, 7, 4, 1):
            value = 1
            return value
        elif board.check_for_winning_position_with_two_empty_cells(self, 1, 2, 0) \
                or board.check_for_winning_position_with_two_empty_cells(self, 6, 3, 0) \
                or board.check_for_winning_position_with_two_empty_cells(self, 8, 4, 0):
            value = 0
            return value
        elif board.check_for_winning_position_with_two_empty_cells(self, 3, 4, 5) \
                or board.check_for_winning_position_with_two_empty_cells(self, 2, 8, 5):
            value = 5
            return value
        elif board.check_for_winning_position_with_two_empty_cells(self, 3, 5, 4) \
                or board.check_for_winning_position_with_two_empty_cells(self, 1, 7, 4) \
                or board.check_for_winning_position_with_two_empty_cells(self, 0, 8, 4) \
                or board.check_for_winning_position_with_two_empty_cells(self, 2, 6, 4):
            value = 4
            return value
        elif board.check_for_winning_position_with_two_empty_cells(self, 5, 4, 3) \
                or board.check_for_winning_position_with_two_empty_cells(self, 0, 6, 3):
            value = 3
            return value
        elif board.check_for_winning_position_with_two_empty_cells(self, 6, 7, 8) \
                or board.check_for_winning_position_with_two_empty_cells(self, 2, 5, 8) \
                or board.check_for_winning_position_with_two_empty_cells(self, 0, 4, 8):
            value = 8
            return value
        elif board.check_for_winning_position_with_two_empty_cells(self, 6, 8, 7) \
                or board.check_for_winning_position_with_two_empty_cells(self, 1, 4, 7):
            value = 7
            return value
        elif board.check_for_winning_position_with_two_empty_cells(self, 7, 8, 6) \
                or board.check_for_winning_position_with_two_empty_cells(self, 0, 3, 6) \
                or board.check_for_winning_position_with_two_empty_cells(self, 2, 4, 6):
            value = 6
            return value



        else:
            value = random.randint(0, 8)

        return value

    # @staticmethod
    # def choose_any_diagonal_cell():
    #     if random.randint(0, 1) == 0:
    #         valid = random.randint(0, 2) * 4
    #     else:
    #         valid = random.randint(1, 3) * 2
    #
    #     return valid


def play_game():
    board = Board()
    player1 = Player('X', '')
    player2 = Player('O', '')
    machine1 = OrdinaryMachine('X', '')
    machine2 = ShrewdMachine('O', '')
    game = Game()
    game.start_to_play(machine2, player1, board)


if __name__ == '__main__':
    play_game()
