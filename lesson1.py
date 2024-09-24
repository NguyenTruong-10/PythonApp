# a = int(input("Chieu cao cua a"))
# b   = int(input("Chieu cao cua b"))
# c = int(input("Chieu cao cua c"))
# if a > b and b < c:
#     print("a lon nhat")
# elif a<b and b > c and a >c:
#     print(" b lon hon")
# elif a <b and c >a and b < c:
#     print("c lon nhat")
n = 5
arrays = []
for i in range(n):
    a = int(input(f"Nhap so thu {i+1}:"))
    arrays.append(a)

for i in arrays:
    if i % 2 != 0:
        arrays.remove(i)
print(arrays)
import math