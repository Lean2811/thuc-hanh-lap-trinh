print("le van an")
print("235752021610044")
def tinh_so_du(nhat_ky_giao_dich):
  so_du = 0
  for giao_dich in nhat_ky_giao_dich.split():
    loai_giao_dich, so_tien = giao_dich[0], int(giao_dich[1:])
    if loai_giao_dich == 'D':
      so_du += so_tien
    elif loai_giao_dich == 'W':
      so_du -= so_tien
    else:
      print("Loại giao dịch không hợp lệ!")
  return so_du
nhat_ky = input("Nhập nhật ký giao dịch (ví dụ: D 300 D 300 W 200 D 100): ")
so_du_cuoi = tinh_so_du(nhat_ky)
print("Số dư cuối cùng:", so_du_cuoi)
