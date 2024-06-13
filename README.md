# Đánh cờ caro đơn giản với 2 người chơi và chơi với máy

## Giới thiệu
Đây là demo về pygame đơn giản. Định hướng phát triển là tạo 1 con bot tự động đánh caro với người chơi.<br>
Import các thư viện:

import subprocess: Thư viện này cho phép bạn tương tác với hệ thống máy tính từ Python, bao gồm chạy các tiến trình và lệnh bên ngoài.
import pygame: Thư viện để phát triển trò chơi hoặc ứng dụng đa phương tiện với Python.
import sys: Thư viện hệ thống trong Python, hỗ trợ quản lý các thông tin và thao tác hệ thống.
Khởi tạo Pygame:

pygame.init(): Khởi tạo thư viện Pygame để sử dụng các chức năng của nó.
Cài đặt màu sắc và font chữ:

BG_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR: Định nghĩa các màu sắc được sử dụng trong trò chơi.
font: Định nghĩa font chữ và kích thước của nó, sử dụng font Arial với kích thước 24.
Khởi tạo màn hình Pygame:

screen: Thiết lập màn hình với kích thước 600x400 pixels để hiển thị trò chơi.
pygame.display.set_caption("Cờ caro"): Đặt tiêu đề cho cửa sổ trò chơi là "Cờ caro".
Hàm để vẽ nút "Chơi với bạn" và "Chơi với bot":

draw_play_with_friend_button(): Vẽ và trả về hình chữ nhật (nút) "Chơi với bạn" trên màn hình.
draw_play_with_bot_button(): Vẽ và trả về hình chữ nhật (nút) "Chơi với bot" trên màn hình.
Hàm để kiểm tra sự kiện nhấn chuột vào nút:

check_button_click(pos, button_rect): Kiểm tra xem vị trí chuột (pos) có nằm trong hình chữ nhật của nút (button_rect) hay không.
Vòng lặp trò chơi:

while running:: Vòng lặp chính của trò chơi, sẽ tiếp tục chạy cho đến khi biến running được đặt là False.
Vòng lặp xử lý các sự kiện từ người dùng (nhấn nút thoát hoặc nhấn vào các nút chơi game).
Xử lý sự kiện nhấn nút và chạy script:

Khi người dùng nhấn nút "Chơi với bạn": subprocess.run(["python", "1vs1/game.py"]) sẽ thực thi lệnh để chạy script game.py trong thư mục 1vs1.
Khi người dùng nhấn nút "Chơi với bot": subprocess.run(["python", "1vsmay/bot.py"]) sẽ thực thi lệnh để chạy script bot.py trong thư mục 1vsmay.
Cập nhật màn hình Pygame:

screen.fill(BG_COLOR): Xóa màn hình với màu nền BG_COLOR.
draw_play_with_friend_button() và draw_play_with_bot_button(): Vẽ lại các nút trên màn hình.
pygame.display.flip(): Cập nhật màn hình để hiển thị các thay đổi đã vẽ.
Kết thúc trò chơi:

pygame.quit(): Đóng thư viện Pygame.
sys.exit(): Thoát khỏi chương trình Python.
Đoạn code này cho phép bạn tạo một giao diện đơn giản để người dùng có thể chọn chơi với người bạn hoặc với bot trong trò chơi Cờ Caro. Khi nhấn vào nút tương ứng, nó sẽ mở một cửa sổ mới để chạy game với người bạn hoặc bot.







![Ảnh nhận dạng số 1](https://github.com/nhut-share-code/Co_caro/blob/main/img/so1.jpg)
![Ảnh nhận dạng số 1](https://github.com/nhut-share-code/Co_caro/blob/main/img/so3.jpg)
![Ảnh nhận dạng số 1](https://github.com/nhut-share-code/Co_caro/blob/main/img/so2.jpg)

