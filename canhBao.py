from gpiozero import DistanceSensor, RotaryEncoder
from datetime import datetime
import time

# Cấu hình chân phần cứng (có thể đổi lại theo thực tế)
# Cảm biến siêu âm
sensor = DistanceSensor(echo=24, trigger=23, max_distance=2.0)
# Nút xoay Encoder
encoder = RotaryEncoder(a=5, b=6)

# Thông số mặc định
nguong_goc_cm = 3.0 
dang_co_vat_can = False 

def ghi_log(khoang_cach, nguong):
    thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    noi_dung = f"[{thoi_gian}] Co vat can! Khoang cach: {khoang_cach:.1f}cm (Nguong: {nguong}cm)\n"

    # Ghi vào file log theo đúng đường dẫn thư mục mới
    with open("/home/nhom1/bai3-ngay2thang7-canhBao/log_canhbao.txt", "a") as file_log:
        file_log.write(noi_dung)
    print(noi_dung, end="")

if __name__ == "__main__":
    print("He thong canh bao dang chay ngam...")

    while True:
        # Đọc số nấc xoay của encoder để thay đổi ngưỡng
        nguong_hien_tai = nguong_goc_cm + encoder.steps
        if nguong_hien_tai < 1.0:
            nguong_hien_tai = 1.0

        # Đọc khoảng cách thực tế (quy đổi ra cm)
        khoang_cach_cm = sensor.distance * 100

        # Xử lý cảnh báo và ghi file log
        if khoang_cach_cm < nguong_hien_tai:
            if not dang_co_vat_can:
                ghi_log(khoang_cach_cm, nguong_hien_tai)
                dang_co_vat_can = True
        else:
            dang_co_vat_can = False

        time.sleep(0.1)
