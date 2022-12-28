# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

from decimal import Decimal, ROUND_HALF_EVEN

n = Decimal(input("Enter a real number: "))
d = input("Enter the required accuracy '0.0001': ")
print(n.quantize(Decimal(d), ROUND_HALF_EVEN))


