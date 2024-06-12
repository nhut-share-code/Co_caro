import pygame
import sys
import numpy as np

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
# font = pygame.font.Font(None, 36)
font = pygame.font.Font('font/arial.ttf', 20)

# Màn hình
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Cờ caro")


# Bảng động
board_size = 15  # Kích thước ban đầu của bảng
board = np.zeros((board_size, board_size))

# Tên của mỗi người chơi
player_names = {1: "", 2: ""}

# Thời gian tối đa cho mỗi người chơi (giây)
MAX_TIME = 30
MAX_TIME = 30
# Thời gian của mỗi người chơi
start_time = 0
# Tổng thời gian đã trôi qua cho mỗi người chơi
player1_time = MAX_TIME
player2_time = MAX_TIME

def input_player_names():
    global player_names
    input_boxes = [pygame.Rect(200, 150 + i * 100, 200, 50) for i in range(2)]
    input_values = ["", ""]

    done = False
    active_box = 0  # Thiết lập hộp nhập dữ liệu đầu tiên là hoạt động
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  
                # Kiểm tra xem hộp nào được nhấp và đặt hộp đó thành hộp đang hoạt động
                for i, box in enumerate(input_boxes):
                    if box.collidepoint(event.pos):
                        active_box = i

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_values[active_box] = input_values[active_box][:-1]
                else:
                    input_values[active_box] += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:
                    for i, box in enumerate(input_boxes):
                        if box.collidepoint(event.pos):
                            pass  

                    ok_button = pygame.Rect(250, 400, 100, 50)
                    if ok_button.collidepoint(event.pos):
                        done = True
                        for i in range(2):
                            player_names[i+1] = input_values[i]

        screen.fill(BG_COLOR)
        for i, box in enumerate(input_boxes):
            # Vẽ hộp nhập dữ liệu
            pygame.draw.rect(screen, (0, 0, 0), box, 2)
            # Hiển thị văn bản trong hộp khi có dữ liệu
            if input_values[i]:
                text_surface = font.render(input_values[i], True, TEXT_COLOR)
                screen.blit(text_surface, (box.x + 5, box.y + 5))
            # Hiển thị văn bản mặc định "Nhập tên" khi không có dữ liệu
            else:
                default_text = font.render("Nhập tên người chơi", True, (128, 128, 128))
                screen.blit(default_text, (box.x + 5, box.y + 5))

            # Thay đổi màu sắc của hộp khi được chọn
            if i == active_box:
                pygame.draw.rect(screen, (255, 255, 255), box, 2)

        # Hiển thị nút "OK"
        ok_button = pygame.Rect(250, 400, 100, 50)
        pygame.draw.rect(screen, BUTTON_COLOR, ok_button)
        ok_text = font.render("OK", True, BUTTON_TEXT_COLOR)
        screen.blit(ok_text, (ok_button.centerx - ok_text.get_width() // 2, ok_button.centery - ok_text.get_height() // 2))

        pygame.display.flip()

# Hàm để hiển thị văn bản
def draw_text(text, size, color, position):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

# Hàm để vẽ đường lưới
def draw_lines():
    for row in range(board_size):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (board_size * SQUARE_SIZE, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(board_size):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, board_size * SQUARE_SIZE), LINE_WIDTH)

# Hàm để vẽ các quân cờ
def draw_figures():
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
 
 
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

# Hàm để cập nhật thời gian của mỗi người chơi
def update_time(current_player):
    global player1_time, player2_time, last_update_time
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - last_update_time) // 1000  # Đổi từ milliseconds sang giây
    if current_player == 1:
        player1_time = max(player1_time - elapsed_time, 0)
    else:
        player2_time = max(player2_time - elapsed_time, 0)
    last_update_time = current_time  # Cập nhật thời gian của lần cuối cùng được cập nhật

# Hàm để hiển thị thời gian còn lại của mỗi người chơi
def draw_time():
    text_surface = font.render(f'{player_names[1]} thời gian: {player1_time}', True, TEXT_COLOR)
    screen.blit(text_surface, (10, 10))
    text_surface = font.render(f'{player_names[2]} thời gian: {player2_time}', True, TEXT_COLOR)
    screen.blit(text_surface, (10, 40))

# Hàm để kiểm tra và cập nhật trạng thái thời gian của mỗi người chơi
def check_time():
    global game_over
    if player1_time <= 0 or player2_time <= 0:
        game_over = True

# Hàm để đánh dấu ô
def mark_square(row, col, current_player):
    board[row][col] = current_player

# Hàm để kiểm tra ô trống
def available_square(row, col):
    return board[row][col] == 0
# Hàm để kiểm tra chiến thắng
def check_win(player):
    for row in range(board_size):
        for col in range(board_size):
            # Kiểm tra chiến thắng theo chiều ngang
            if col <= board_size - WIN_CONDITION and all(board[row][col + i] == player for i in range(WIN_CONDITION)):
                return True
            # Kiểm tra chiến thắng theo chiều dọc
            if row <= board_size - WIN_CONDITION and all(board[row + i][col] == player for i in range(WIN_CONDITION)):
                return True
            # Kiểm tra chiến thắng theo đường chéo chính
            if row <= board_size - WIN_CONDITION and col <= board_size - WIN_CONDITION and all(board[row + i][col + i] == player for i in range(WIN_CONDITION)):
                return True
            # Kiểm tra chiến thắng theo đường chéo phụ
            if row >= WIN_CONDITION - 1 and col <= board_size - WIN_CONDITION and all(board[row - i][col + i] == player for i in range(WIN_CONDITION)):
                return True
    return False

# Hàm để hiển thị dòng chúc mừng khi có người chiến thắng
def display_winner(player):
    winner_text = font.render(f'{player_names[player]} Chiến hắng!', True, TEXT_COLOR)
    screen.blit(winner_text, (WINDOW_SIZE // 2 - winner_text.get_width() // 2, WINDOW_SIZE // 2 - winner_text.get_height() // 2))


# Hàm để làm mới trò chơi
def restart_game():
    global board, player1_time, player2_time, game_over, start_time
    board = np.zeros((board_size, board_size))
    player1_time = MAX_TIME
    player2_time = MAX_TIME
    game_over = False
    start_time = pygame.time.get_ticks()  # Cập nhật thời gian bắt đầu

FPS = 30  # Số khung hình mỗi giây bạn muốn hiển thị

# Vòng lặp trò chơi
def game_loop():
    global game_over, last_update_time
    input_player_names()  # Người chơi nhập tên trước khi bắt đầu trò chơi
    current_player = 1
    game_over = False

    last_update_time = pygame.time.get_ticks()  # Thời điểm cuối cùng cập nhật thời gian

    while True:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]  # X
                mouseY = event.pos[1]  # Y

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, current_player)
                    if check_win(current_player):
                        game_over = True

                    current_player = 2 if current_player == 1 else 1
                    last_update_time = current_time  # Cập nhật thời gian cho lượt đánh mới

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_game()

        # Tính toán thời gian đã trôi qua kể từ lần cập nhật trước đó
        elapsed_time = current_time - last_update_time
        if elapsed_time >= 1000:  # Kiểm tra nếu đã trôi qua ít nhất 1 giây
            # Giảm thời gian của người chơi hiện tại
            update_time(current_player)
            # Cập nhật thời gian cho lần cập nhật tiếp theo
            last_update_time = current_time

        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()
        draw_time()

        if game_over:
            winner = 1 if check_win(1) else 2
            display_winner(winner)

        pygame.display.flip()

        # Đợi một khoảng thời gian trước khi bắt đầu lượt lặp tiếp theo
        pygame.time.delay(1000 // FPS)

# Chạy trò chơi
game_loop()
