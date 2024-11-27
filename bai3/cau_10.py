print("Le Van An")
print("235752021610044")
import math

def tinh_hinh_tron(r):
  if r <= 0:
    return "Bán kính phải lớn hơn 0"
  return 2*math.pi*r, math.pi*r**2

ban_kinh = float(input("Nhập bán kính: "))
chu_vi, dien_tich = tinh_hinh_tron(ban_kinh)
print("Chu vi:", chu_vi)
print("Diện tích:", dien_tich)
