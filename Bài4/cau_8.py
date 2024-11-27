print("le van an")
print("235752021610044")
def tim_tu_dai_nhat(cau):
  """Hàm tìm các từ dài nhất trong một câu

  Args:
    cau: Chuỗi chứa các từ

  Returns:
    Một list chứa các từ dài nhất
  """

  # Tách chuỗi thành các từ
  cac_tu = cau.split()

  # Tìm độ dài lớn nhất của các từ
  do_dai_lon_nhat = len(max(cac_tu, key=len))

  # Tìm các từ có độ dài bằng độ dài lớn nhất
  cac_tu_dai_nhat = [tu for tu in cac_tu if len(tu) == do_dai_lon_nhat]

  return cac_tu_dai_nhat

# Nhập chuỗi từ người dùng
cau_nhap_vao = input("Nhập vào một câu: ")

# Gọi hàm tìm từ dài nhất và in kết quả
cac_tu_dai_nhat = tim_tu_dai_nhat(cau_nhap_vao)
print("Các từ dài nhất là:", cac_tu_dai_nhat)
