print("le van an")
print("235752021610044")
def sap_xep_tu_theo_tu_dien(cau):
  cac_tu = cau.split()
  cac_tu_sap_xep = sorted(cac_tu)
  cau_moi = ' '.join(cac_tu_sap_xep)
  return cau_moi
cau_nhap_vao = input("Nhập vào một câu tiếng Anh: ")
cau_sap_xep = sap_xep_tu_theo_tu_dien(cau_nhap_vao)
print("Các từ sau khi sắp xếp:", cau_sap_xep)
