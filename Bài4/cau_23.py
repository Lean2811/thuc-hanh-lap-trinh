print("le van an")
print("235752021610044")
def count_letters_and_digits(text):
  count_letters = 0
  count_digits = 0
  for char in text:
    if char.isalpha():
      count_letters += 1
    elif char.isdigit():
      count_digits += 1
  return count_letters, count_digits
