print("Le Van An")
print("235752021610044")
def tinh_tien_lai(von_goc, lai_suat, so_thang):
  """Tính số tiền nhận được sau khi gửi tiết kiệm

  Args:
    von_goc: Số tiền gửi ban đầu
    lai_suat: Lãi suất hàng tháng (%)
    so_thang: Số tháng gửi

  Returns:
    Số tiền nhận được sau khi gửi
  """

  lai_suat = lai_suat / 100
  tien_lai = von_goc * (1 + lai_suat) ** so_thang
  return tien_lai

# Nhập dữ liệu từ người dùng
von_goc = float(input("Nhập số tiền gửi ban đầu: "))
lai_suat = float(input("Nhập lãi suất hàng tháng (%): "))
so_thang = int(input("Nhập số tháng gửi: "))

# Tính và in kết quả
ket_qua = tinh_tien_lai(von_goc, lai_suat, so_thang)
print("Số tiền nhận được sau", so_thang, "tháng là:", ket_qua)
