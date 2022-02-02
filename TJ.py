# IDEAS***************************************************************************************
# make a main menue to select diffuculty or play a friend
# *********************************************************************************************

# IMPORTS
import pygame
import sys
import numpy as np

# CONSTANTS***************
CYAN = (28, 170, 154)
RED = (255, 0, 0)
WIDTH = 600
HEIGHT = 600
LINE_RGB = (23, 145, 135)
LINE_W = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 80
CIRCLE_WIDTH = 18
CIRCLE_RGB = (239, 231, 200)
SHAPEX_WIDTH = 25
SPACE = 36
RGB_X = (66, 66, 66)

pygame.init()

scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
scr.fill(CYAN)


board = np.zeros((BOARD_ROWS, BOARD_COLS))  #


player = 1
gameover = False



def draw_lines():
    # first horozontal
    pygame.draw.line(scr, LINE_RGB, (0, 200), (600, 200), LINE_W)

    # second horozontal
    pygame.draw.line(scr, LINE_RGB, (0, 400), (600, 400), LINE_W)

    # first vertical
    pygame.draw.line(scr, LINE_RGB, (200, 0), (200, 600), LINE_W)

    # second vertical
    pygame.draw.line(scr, LINE_RGB, (400, 0), (400, 600), LINE_W)


def draw_figs():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 2:
                pygame.draw.circle(scr, CIRCLE_RGB, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 1:
                pygame.draw.line(scr, RGB_X, (col * 200 + SPACE, row * 200 + 200 - SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + SPACE), SHAPEX_WIDTH)
                pygame.draw.line(scr, RGB_X, (col * 200 + SPACE, row * 200 + SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), SHAPEX_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
            else:
                return True



def check_win(player):
    # vert
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vert_win_line(col, player)
            return True
    # horzontal
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horz_win_line(row, player)
            return True
    # up daig
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_diag_up(player)
        return True

    # down daig
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diag_down(player)
        return True

    else:
        return False


def draw_vert_win_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = RGB_X
    elif player == 2:
        color = CIRCLE_RGB

    pygame.draw.line(scr, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horz_win_line(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = RGB_X
    elif player == 2:
        color = CIRCLE_RGB

    pygame.draw.line(scr, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_diag_up(player):
    if player == 1:
        color = RGB_X
    elif player == 2:
        color = CIRCLE_RGB

    pygame.draw.line(scr, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_diag_down(player):
    if player == 1:
        color = RGB_X
    elif player == 2:
        color = CIRCLE_RGB

    pygame.draw.line(scr, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    scr.fill(CYAN)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

draw_lines()
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # 1

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        gameover = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        gameover = True
                    player = 1
                draw_figs()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r or event.key == pygame.K_SPACE:
                restart()
                gameover = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                sys.exit()
    pygame.display.update()