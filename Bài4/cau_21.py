print("le van an")
print("235752021610044")
def find_binary_numbers_divisible_by_5(binary_string):
  binary_numbers = binary_string.split(',')
  divisible_by_5 = [num for num in binary_numbers if num[-1] == '1']
  return ','.join(divisible_by_5)
