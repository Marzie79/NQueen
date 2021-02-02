from datetime import datetime
import random
import math
import decimal


class Board:
    def __init__(self, queen_count=8):
        self.queen_count = queen_count
        self.reset()

    def reset(self):
        self.queens = [-1 for i in range(0, self.queen_count)]

        for i in range(0, self.queen_count):
            self.queens[i] = random.randint(0, self.queen_count - 1)

    @staticmethod
    def calculate_cost_with_queens(queens):
        threat = 0
        queen_count = len(queens)

        for queen in range(0, queen_count):
            for next_queen in range(queen + 1, queen_count):
                if queens[queen] == queens[next_queen] or abs(queen - next_queen) == abs(
                        queens[queen] - queens[next_queen]):
                    threat += 1

        return threat

    @staticmethod
    def to_string(queens):
        board_string = ""

        for row, col in enumerate(queens):
            board_string += "(%s, %s)\n" % (row, col)

        return board_string

    def __str__(self):
        board_string = ""

        for row, col in enumerate(self.queens):
            board_string += "(%s, %s)\n" % (row, col)

        return board_string


class SimulatedAnnealing:
    def __init__(self, board):
        self.board = board
        self.temperature = int(datetime.now().second)

    def run(self):
        board = self.board
        board_queens = self.board.queens[:]
        solution_found = False

        while not solution_found:
            board.reset()
            successor_queens = board.queens[:]
            dw = Board.calculate_cost_with_queens(successor_queens) - Board.calculate_cost_with_queens(board_queens)
            exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(-dw) * decimal.Decimal(self.temperature)))
            print(exp)
            if dw > 0 or random.uniform(0, 1) < exp:
                board_queens = successor_queens[:]

            if Board.calculate_cost_with_queens(board_queens) == 0:
                print("Solution:")
                print(Board.to_string(board_queens))
                solution_found = True

        return True


if __name__ == '__main__':
    board = Board()
    print("First Board:")
    print(board)
    SimulatedAnnealing(board).run()
