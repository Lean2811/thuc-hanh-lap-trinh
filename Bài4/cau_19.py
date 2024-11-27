print("le van an")
print("235752021610044")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tạo tuple chứa các số nguyên tố nhỏ hơn 1 triệu
P = tuple(i for i in range(1_000_000) if is_prime(i))

# Kiểm tra kết quả
print(P[:10])  # In ra 10 số đầu tiên trong tuple
print(f"Số lượng số nguyên tố nhỏ hơn 1 triệu: {len(P)}")
