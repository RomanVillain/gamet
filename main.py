import random

def create_board(rows, cols):
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(' ')
        board.append(row)
    return board

level_sizes = {'легкий': 5, 'середній': 10, 'складний': 20}

while True:
    name = input("Введіть cвій нікнейм: ")
    if name.strip() != "":
        break

while True:
    level = input("Виберіть рівень складності легкий, середній, складний: ")
    if level in level_sizes:
        rows = cols = level_sizes[level]
        break

treasure_row = random.randint(0, rows-1)
treasure_col = random.randint(0, cols-1)

board = create_board(rows, cols)
board[treasure_row][treasure_col] = 'X'

print("Карта згенерована. Скарб знаходиться в клітинці із заданими координатами ({}, {}).".format(treasure_row, treasure_col))
for i in range(rows):
    print(" " + "___" * cols)
    row_str = "|"
    for j in range(cols):
        row_str += " {} |".format(board[i][j])
    print(row_str)
print(" " + "___" * cols)

print("Гра почалася, {}! Ваше завдання - знайти скарб розташований на карті.".format(name))


