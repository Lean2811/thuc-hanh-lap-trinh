print("Le Van An")
print("235752021610044")
def fibonacci_less_than_n(n):
    fibonacci_list = []
    a, b = 0, 1
    while a < n:
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list
n = int(input("Nhập số nguyên n: "))
print(fibonacci_less_than_n(n))
