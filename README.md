# Đánh Cờ Caro Đơn Giản với Pygame

## Giới thiệu

Đây là một demo đơn giản về trò chơi Đánh Cờ Caro được thực hiện bằng Python với sử dụng thư viện Pygame. Dự án nhằm cung cấp một cấu trúc cơ bản để chơi Đánh Cờ Caro với bạn bè hoặc với máy tính.

## Cấu Trúc và Tập Tin

### main.py

#### Các Thư Viện Sử Dụng:
- `pygame`: Được sử dụng để phát triển trò chơi và ứng dụng đa phương tiện trong Python.
- `sys`: Thư viện hệ thống cung cấp các thông tin và chức năng hệ thống.

#### Khởi Tạo:
- `pygame.init()`: Khởi tạo thư viện Pygame để sử dụng các chức năng của nó.

#### Màu Sắc và Font Chữ:
- `BG_COLOR`, `BUTTON_COLOR`, `BUTTON_TEXT_COLOR`: Định nghĩa các màu sắc cho giao diện trò chơi.
- `font`: Định nghĩa font chữ và kích thước sử dụng cho văn bản.

#### Thiết Lập Màn Hình:
- `screen`: Thiết lập cửa sổ trò chơi với kích thước 600x400 pixels.
- `pygame.display.set_caption("Đánh Cờ Caro")`: Đặt tiêu đề cho cửa sổ trò chơi.

#### Hàm Vẽ Nút "Chơi với Bạn" và "Chơi với Máy":
- `draw_play_with_friend_button()`: Vẽ và trả về nút "Chơi với Bạn".
- `draw_play_with_bot_button()`: Vẽ và trả về nút "Chơi với Máy".

#### Xử Lý Sự Kiện Click Chuột:
- `check_button_click(pos, button_rect)`: Kiểm tra xem vị trí click chuột (`pos`) có nằm trong vùng của nút (`button_rect`) hay không.

#### Vòng Lặp Chính của Trò Chơi:
- Liên tục kiểm tra các sự kiện từ người dùng (nhấn nút, click chuột).
- Thực thi các script tương ứng (`game.py` cho chế độ 1vs1, `bot.py` cho chế độ 1vsMáy) bằng `subprocess.run()` khi người dùng nhấn nút.

#### Cập Nhật Màn Hình:
- Cập nhật màn hình Pygame để phản ánh các thay đổi (vẽ nút, v.v.).
- Xử lý thoát khỏi trò chơi (`pygame.quit()` và `sys.exit()`).

## Cách Sử Dụng

1. Đảm bảo bạn đã cài đặt Python và Pygame trên máy tính của mình.
2. Chạy tập tin `main.py` để bắt đầu chơi trò chơi.
3. Click vào "Chơi với Bạn" hoặc "Chơi với Máy" để bắt đầu chơi.

## Phát Triển Tương Lai

Dự án có thể được mở rộng bằng cách:
- Phát triển trí tuệ nhân tạo phức tạp hơn cho bot.
- Cải thiện giao diện trò chơi với hiệu ứng hoặc âm thanh.
- Thêm các tùy chọn khác như kích thước bàn cờ hoặc chế độ chơi.

## Liên Hệ

Nếu bạn có câu hỏi hoặc gặp vấn đề với code trong các tập tin khác, vui lòng liên hệ qua Zalo: 0394915710.

![Ảnh 1](https://github.com/nhut-share-code/Co_caro/blob/main/img/so1.jpg)
![Ảnh 2](https://github.com/nhut-share-code/Co_caro/blob/main/img/so2.jpg)
![Ảnh 3](https://github.com/nhut-share-code/Co_caro/blob/main/img/so3.jpg)
