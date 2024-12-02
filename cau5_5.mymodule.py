print("le van an")
print("235752021610044")
n = int(input("Nhập số lượng phần tử trong danh sách: "))
danh_sach = []

for i in range(n):  # Dùng vòng lặp để nhập từng phần tử
    gia_tri = int(input(f"Nhập phần tử thứ {i + 1}: "))
    danh_sach.append(gia_tri)  # Thêm phần tử vào danh sách

def tim_lon_nhat_va_nho_nhat(danh_sach):
    lon_nhat = max(danh_sach)  # Hàm max() tìm giá trị lớn nhất
    nho_nhat = min(danh_sach)  # Hàm min() tìm giá trị nhỏ nhất
    return lon_nhat, nho_nhat

lon_nhat, nho_nhat = tim_lon_nhat_va_nho_nhat(danh_sach)
print("Danh sách đã nhập:", danh_sach)
print("Phần tử lớn nhất:", lon_nhat)
print("Phần tử nhỏ nhất:", nho_nhat)
