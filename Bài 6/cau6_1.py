print("le van an")
print("235752021610044")
class Circle(object):
    def __init__(self, r):
        self.radius = r  # Lưu trữ bán kính vào thuộc tính của đối tượng
    def area(self):
        return self.radius**2 * 3.14  # Tính diện tích hình tròn
# Tạo một đối tượng hình tròn với bán kính 2
circle = Circle(2)
# Tính và in diện tích của hình tròn
print(circle.area()
