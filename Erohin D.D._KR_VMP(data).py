#!/usr/bin/python
# -*- coding: utf-8 -*-


def print_board(board):
    # вывод судоку

    boardString = ''
    for i in range(9):
        for j in range(9):
            boardString += str(board[i][j]) + ' '
            if (j + 1) % 3 == 0 and j != 0 and j + 1 != 9:
                boardString += '| '

            if j == 8:
                boardString += '\n'

            if j == 8 and (i + 1) % 3 == 0 and i + 1 != 9:
                boardString += '- - - - - - - - - - - \n'
    print(boardString)


def find_empty(board):
    '''Находит пустую ячейку и возвращает позицию в виде tuple'''
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def valid(board, pos, num):
    # проверка строки
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # проверка столбца
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(board):
    """Алгоритм по собиранию судоку"""
    empty = find_empty(board)
    if not empty:  # Если не найдено пустых ячеек - судоку решено
        return True
    else:
        row, col = empty
    for i in range(1, 10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):  # рекурсия
                return True
            board[row][col] = 0
    return False


if __name__ == '__main__':
    board = [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]
    ]
    print_board(board)
    solve(board)
    print_board(board)
