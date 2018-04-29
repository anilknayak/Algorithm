import numpy as np


class Load:
    def __init__(self, f_i, f_o):
        self.file_name_out = f_o
        self.file_name = f_i
        self.debug = False

    def load_input(self):
        with open(self.file_name_out, 'w') as file_out:
            with open(self.file_name, 'r') as file:
                self.test_cases = int(file.readline())
                for test_case_no in range(self.test_cases):
                    if self.debug:
                        print("========= Test Case: ", test_case_no, "=========")
                    N, move = file.readline().rstrip("\n\r").split(" ")

                    if self.debug:
                        print("Board Size", N)
                        print("Move ", move)

                    matrix = [[-1 for x in range(int(N))] for y in range(int(N))]
                    for i in range(int(N)):
                        board_row = file.readline().rstrip("\n\r").split(" ")
                        for j in range(len(board_row)):
                            matrix[i][j] = int(board_row[j])

                    if self.debug:
                        print("Board", matrix)

                    solved = self.solve(matrix, move, N)

                    print("Case #%d:" % (test_case_no + 1))
                    file_out.write("Case #%d:" % (test_case_no + 1))
                    file_out.write("\n")
                    for row in solved:
                        str1 = ''
                        for ele in row:
                            if self.debug:
                                print(int(ele), end='', flush=True)
                                print(" ", end='', flush=True)
                            str1 = str1 + str(ele) + " "

                        file_out.write(str1.strip("\s") + "\n")
                        if self.debug:
                            print("")

                    if self.debug:
                        print("Solved ", solved)

    def solve(self, board, move, N):

        if move == "up":
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
            self.solve_left_up(board)
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
            return board
        elif move == "down":
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
            self.solve_right_down(board)
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
            return board
        elif move == "left":
            self.solve_left_up(board)
            return board

        elif move == "right":
            self.solve_right_down(board)
            return board

        return None

    def solve_right_down(self, board):
        for board_row in board:
            len_b_r = len(board_row)

            for i in range(len_b_r - 1, -1, -1):
                ele = int(board_row[i])
                if ele == 0 and not i - 1 == -1:
                    for j in range(i - 1, -1,-1):
                        ele1 = int(board_row[j])
                        if ele1 > 0:
                            board_row[i] = board_row[j]
                            board_row[j] = 0
                            break

            s = len_b_r - 1
            for i in range(len_b_r - 1):
                n0 = int(board_row[s])
                n1 = int(board_row[s - 1])
                if n0 == n1 and (not n0 == 0 or not n1 == 0):
                    board_row[s - 1] = '-1'
                    board_row[s] = str(n0 + n1)

                    if s + 1 <= len_b_r - 1 and board_row[s + 1] == '-1':
                        board_row[s + 1] = board_row[s]
                        board_row[s] = 0
                    s = s - 2
                elif n0 == 0:
                    board_row[s] = board_row[s - 1]
                    board_row[s - 1] = 0
                else:
                    s = s - 1

                if s - 1 <= -1:
                    break

            for ele in range(len_b_r):
                if int(board_row[ele]) == -1:
                    board_row[ele] = 0

            for i in range(len_b_r - 1, -1, -1):
                ele = int(board_row[i])
                if ele == 0 and not i - 1 == -1:
                    for j in range(i - 1, -1,-1):
                        ele1 = int(board_row[j])
                        if ele1 > 0:

                            board_row[i] = board_row[j]
                            board_row[j] = 0
                            break


    def solve_left_up(self, board):
        for board_row in board:
            len_b_r = len(board_row)

            for i in range(0,len_b_r):
                ele = int(board_row[i])
                if ele == 0 and not i + 1 == len_b_r:
                    for j in range(i+1, len_b_r):
                        ele1 = int(board_row[j])
                        if ele1 > 0:
                            board_row[i] = board_row[j]
                            board_row[j] = 0
                            break

            s = 0
            for i in range(len_b_r - 1):
                n0 = int(board_row[s])
                n1 = int(board_row[s + 1])
                if n0 == n1 and (not n0 == 0 or not n1 == 0):
                    board_row[s + 1] = '-1'
                    board_row[s] = str(n0 + n1)

                    if s - 1 >= 0 and board_row[s - 1] == '-1':
                        board_row[s - 1] = board_row[s]
                        board_row[s] = '0'
                    s = s + 2
                else:
                    s = s + 1

                if s + 1 >= len_b_r:
                    break

            for ele in range(len_b_r):
                if int(board_row[ele]) == -1:
                    board_row[ele] = '0'

            for i in range(0,len_b_r):
                ele = int(board_row[i])
                if ele == 0 and not i + 1 == len_b_r:
                    for j in range(i+1, len_b_r):
                        ele1 = int(board_row[j])
                        if ele1 > 0:
                            board_row[i] = board_row[j]
                            board_row[j] = 0
                            break

# l = Load('B-small-practice.in', 'B-small-practice.out')
l = Load('B-large-practice.in','B-large-practice.out')
l.load_input()
