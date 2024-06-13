import pygame
import sys
import numpy as np
import random
import json
import os

# Khởi tạo Pygame
pygame.init()

# Các hằng số
WINDOW_SIZE = 600
LINE_WIDTH = 5
SQUARE_SIZE = 40
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 5
CROSS_WIDTH = 5
SPACE = SQUARE_SIZE // 4
SCROLL_SPEED = 20
WIN_CONDITION = 5  # Số quân liên tiếp để thắng

# Màu sắc
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (0, 128, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Font chữ
font = pygame.font.Font('font/arial.ttf', 20)

# Màn hình
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Cờ caro")

# Bảng động
board_size = 15  # Kích thước ban đầu của bảng
board = np.zeros((board_size, board_size))

# Tên của mỗi người chơi
player_names = {1: "Người chơi", 2: "Bot"}

# Thời gian tối đa cho mỗi người chơi (giây)
MAX_TIME = 30

# Thời gian của mỗi người chơi
start_time = 0
player1_time = MAX_TIME
player2_time = MAX_TIME

# Dữ liệu học tập của bot
learning_data_file = "learning_data.json"
learning_data = {}

if os.path.exists(learning_data_file):
    with open(learning_data_file, 'r') as file:
        learning_data = json.load(file)

def input_player_names():
    global player_names
    input_boxes = [pygame.Rect(200, 150 + i * 100, 200, 50) for i in range(1)]  # Chỉ cho người chơi nhập tên
    input_values = [""]

    done = False
    active_box = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, box in enumerate(input_boxes):
                    if box.collidepoint(event.pos):
                        active_box = i

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_values[active_box] = input_values[active_box][:-1]
                else:
                    input_values[active_box] += event.unicode

                if event.key == pygame.K_RETURN:
                    player_names[1] = input_values[0]
                    done = True

        screen.fill(BG_COLOR)
        for i, box in enumerate(input_boxes):
            pygame.draw.rect(screen, (0, 0, 0), box, 2)
            if input_values[i]:
                text_surface = font.render(input_values[i], True, TEXT_COLOR)
                screen.blit(text_surface, (box.x + 5, box.y + 5))
            else:
                default_text = font.render("Nhập tên người chơi", True, (128, 128, 128))
                screen.blit(default_text, (box.x + 5, box.y + 5))

            if i == active_box:
                pygame.draw.rect(screen, (255, 255, 255), box, 2)

        ok_button = pygame.Rect(250, 400, 100, 50)
        pygame.draw.rect(screen, BUTTON_COLOR, ok_button)
        ok_text = font.render("OK", True, BUTTON_TEXT_COLOR)
        screen.blit(ok_text, (ok_button.centerx - ok_text.get_width() // 2, ok_button.centery - ok_text.get_height() // 2))

        pygame.display.flip()

def draw_text(text, size, color, position):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

def draw_lines():
    for row in range(board_size):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (board_size * SQUARE_SIZE, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(board_size):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, board_size * SQUARE_SIZE), LINE_WIDTH)

def draw_figures():
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def update_time(current_player):
    global player1_time, player2_time, last_update_time
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - last_update_time) // 1000
    if current_player == 1:
        player1_time = max(player1_time - elapsed_time, 0)
    else:
        player2_time = max(player2_time - elapsed_time, 0)
    last_update_time = current_time

def draw_time():
    text_surface = font.render(f'{player_names[1]} thời gian: {player1_time}', True, TEXT_COLOR)
    screen.blit(text_surface, (10, 10))
    text_surface = font.render(f'{player_names[2]} thời gian: {player2_time}', True, TEXT_COLOR)
    screen.blit(text_surface, (10, 40))

def check_time():
    global game_over
    if player1_time <= 0 or player2_time <= 0:
        game_over = True

def mark_square(row, col, current_player):
    board[row][col] = current_player

def available_square(row, col):
    return board[row][col] == 0

def check_win(player):
    for row in range(board_size):
        for col in range(board_size):
            if col <= board_size - WIN_CONDITION and all(board[row][col + i] == player for i in range(WIN_CONDITION)):
                return True
            if row <= board_size - WIN_CONDITION and all(board[row + i][col] == player for i in range(WIN_CONDITION)):
                return True
            if row <= board_size - WIN_CONDITION and col <= board_size - WIN_CONDITION and all(board[row + i][col + i] == player for i in range(WIN_CONDITION)):
                return True
            if row >= WIN_CONDITION - 1 and col <= board_size - WIN_CONDITION and all(board[row - i][col + i] == player for i in range(WIN_CONDITION)):
                return True
    return False

def display_winner(player):
    winner_text = font.render(f'{player_names[player]} Chiến thắng!', True, TEXT_COLOR)
    screen.blit(winner_text, (WINDOW_SIZE // 2 - winner_text.get_width() // 2, WINDOW_SIZE // 2 - winner_text.get_height() // 2))

def restart_game():
    global board, player1_time, player2_time, game_over, start_time
    board = np.zeros((board_size, board_size))
    player1_time = MAX_TIME
    player2_time = MAX_TIME
    game_over = False
    start_time = pygame.time.get_ticks()

def bot_move():
    empty_squares = [(row, col) for row in range(board_size) for col in range(board_size) if board[row][col] == 0]

    # Nếu không có nước đi trống, trả về None
    if not empty_squares:
        return None

    # Nếu là lượt đầu tiên, chọn ngẫu nhiên một ô trống
    if last_move_row == -1 and last_move_col == -1:
        return random.choice(empty_squares)

    # Tìm các ô xung quanh nước đi cuối cùng của người chơi
    around_last_move = []
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            nr, nc = last_move_row + dr, last_move_col + dc
            if 0 <= nr < board_size and 0 <= nc < board_size and board[nr][nc] == 0:
                around_last_move.append((nr, nc))

    # Lựa chọn một ô từ các ô xung quanh nếu có
    if around_last_move:
        return random.choice(around_last_move)
    else:
        # Nếu không có ô xung quanh, chọn ngẫu nhiên một ô trống
        return random.choice(empty_squares)
def save_bot_learning():
    # Lưu nước đi cuối cùng của bot vào dữ liệu học tập
    state = json.dumps(tuple(map(tuple, board)))
    if state not in learning_data:
        learning_data[state] = []
    last_move = (last_move_row, last_move_col)
    if last_move not in learning_data[state]:
        learning_data[state].append(last_move)

    with open(learning_data_file, 'w') as file:
        json.dump(learning_data, file)

FPS = 30
def game_loop():
    global game_over, last_update_time, last_move_row, last_move_col
    input_player_names()
    current_player = 1
    game_over = False
    last_update_time = pygame.time.get_ticks()
    last_move_row, last_move_col = -1, -1

    while True:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_bot_learning()  # Lưu dữ liệu học tập trước khi thoát
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and current_player == 1:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, current_player)
                    last_move_row, last_move_col = clicked_row, clicked_col
                    if check_win(current_player):
                        game_over = True
                    current_player = 2
                    last_update_time = current_time

        if current_player == 2 and not game_over:
            row, col = bot_move()
            if available_square(row, col):
                mark_square(row, col, current_player)
                last_move_row, last_move_col = row, col
                save_bot_learning()  # Lưu dữ liệu học tập sau mỗi lượt đi của bot
                if check_win(current_player):
                    game_over = True
                current_player = 1
                last_update_time = current_time

        elapsed_time = current_time - last_update_time
        if elapsed_time >= 1000:
            update_time(current_player)
            last_update_time = current_time

        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()
        draw_time()

        if game_over:
            winner = 1 if check_win(1) else 2
            display_winner(winner)

        pygame.display.flip()
        pygame.time.delay(1000 // FPS)

# Bắt đầu vòng lặp chính của trò chơi
game_loop()
