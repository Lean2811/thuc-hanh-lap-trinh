print("le van an")
print("235752021610044")
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def tinh_dien_tich(self):
                 return self.chieu_dai * self.chieu_rong
hinh_chu_nhat = Hinhchunhat(2, 6)
dien_tich = hinh_chu_nhat.tinh_dien_tich()
print("Diện tích hình chữ nhật:", dien_tich)
