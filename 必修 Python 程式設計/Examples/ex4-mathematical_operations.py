a = int(input("輸入a:"))
b = int(input("輸入b:"))

# 基礎運算
print("a + b =", a+b)
print("a - b =", a-b)
print("a * b =", a*b)
print("a / b =", a/b)
print("a // b =", a//b)
print("a % b =", a%b)
print("a ** b =", a**b)

print("----------我是分割線----------")

# 四捨五入與絕對值
num = -0.123456
print(f"round({num}):", round(num))
print(f"round({num}, 2):", round(num, 2))
print(f"round({num}, 5):", round(num, 5))
print()
print("abs(5):", abs(5))
print("abs(-5):", abs(-5))
print("abs(num):", abs(num))

print("----------我是分割線----------")

# math 模組使用
import math
num = 123.456
print(f"math.floor({num}):", math.floor(num))
print(f"math.ceil({num}):", math.ceil(num))
print(f"round({num}):", round(num))
print()
print("math.pow(2, 2):", math.pow(2, 2))
print("math.pow(2, 3):", math.pow(2, 3))
print()
print("math.sqrt(9):", math.sqrt(9))
print("math.sqrt(100):", math.sqrt(100))
print("100**0.5:", 100**0.5)