print("le van an")
print("235752021610044")
def find_even_digit_numbers(start, end):
  even_numbers = []
  for num in range(start, end + 1):
    num_str = str(num)
    if all(int(digit) % 2 == 0 for digit in num_str):
      even_numbers.append(num)
  return ', '.join(map(str, even_numbers))
start = 1000
end = 3000
result = find_even_digit_numbers(start, end)
print(result)
