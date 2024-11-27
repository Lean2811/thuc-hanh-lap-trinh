print("le van an")
print("235752021610044")
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

n = int(input("Nhập n: "))
list_fibonacci = list(fibonacci(n))
print(list_fibonacci)
