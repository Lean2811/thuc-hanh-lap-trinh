print("le van an")
print("235752021610044")
a, b = 1, 2
total = 0

while a < 4000000:
  if a % 2 == 0:
    total += a
  print(a, end=" ")
  a, b = b, a + b

print(f"\nTổng các số chẵn trong dãy Fibonacci: {total}")
      
