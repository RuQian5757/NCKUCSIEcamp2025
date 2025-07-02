# 基本資料型態
print("123", "is", type("123"))
print(123, "is", type(123))
print(123.0, "is", type(123.0))
print(True, type(True))

print("----------我是分割線----------")

# 資料型態轉換
print(type(float(123)), end=" : ") 
print(float(123))# 123.0

print(type(int(123.5)), end=" : ") 
print(int(123.5)) # 123

print(type(float(True)), end=" : ") 
print(float(True)) # 1.0

print(type(bool(0.5)), end=" : ") 
print(bool(0.5)) # True


print("----------我是分割線----------")

# 字串轉數值
print(type(int("123")), end=" : ")
print(int("123")) # 123

print(type(float(123.45)), end=" : ")
print(float("123.45")) # 123.45

print(type(float("123")), end=" : ")
print(float("123")) # 123.0

print(type(bool("123.45")), end=" : ")
print(bool("123.45")) # True

print(type(bool("")), end= " : ")
print(bool("")) # False

print(int("123.45")) # error
print(int("A0")) # error
