#!/bin/bash
# Chờ 10 giây để hệ điều hành tải xong giao diện màn hình chính
sleep 10

# Báo cho máy biết sẽ hiển thị cửa sổ ở màn hình mặc định
export DISPLAY=:0

# Di chuyển vào thư mục code
cd /home/nhom1/bai3-ngay2thang7-canhBao

# Gọi giao diện lxterminal và bắt nó chạy file Python
lxterminal -e "python3 canhBao.py"
