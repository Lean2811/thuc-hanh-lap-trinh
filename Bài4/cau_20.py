print("le van an")
print("235752021610044")
def pascal_triangle(n):
  triangle = []
  for i in range(n):
    row = [1] * (i+1)
    for j in range(1, i):
      row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)
  for row in triangle:
    print(' '.join(map(str, row)))
n = int(input("Nhập số lượng hàng của tam giác Pascal: "))
pascal_triangle(n)
