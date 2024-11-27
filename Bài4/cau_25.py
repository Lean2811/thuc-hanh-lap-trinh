print("le van an")
print("235752021610044")
def loc_so_le(chuoi_so):
  list_so = chuoi_so.split(',')
  list_so = [int(so) for so in list_so]
  so_le = [so for so in list_so if so % 2 != 0]
  return so_le
chuoi_nhap = input("Nhập chuỗi các số nguyên (cách nhau bởi dấu phẩy): ")
ket_qua = loc_so_le(chuoi_nhap)
print("Các số lẻ là:", ket_qua)
