print("le van an")
print("235752021610044")
def dem_chu_hoa_thuong(cau):
  so_chu_hoa = 0
  so_chu_thuong = 0
  for ky_tu in cau:
    if ky_tu.isupper():
      so_chu_hoa += 1
    elif ky_tu.islower():
      so_chu_thuong += 1
  return so_chu_hoa, so_chu_thuong
cau = input("Nhập câu: ")
so_hoa, so_thuong = dem_chu_hoa_thuong(cau)
print("Chữ hoa:", so_hoa)
print("Chữ thường:", so_thuong)
