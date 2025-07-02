# 邏輯運算
a = 7
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(not(a > b))

print("----------我是分割線----------")

print(True and True)
print(False and False)
print(True and False)

print(True or True)
print(False or False)
print(True or False)

print("----------我是分割線----------")
# 流程控制 - 判斷

deadline = 1

if deadline >= 24*7 :
    print("Play LOL")
elif (deadline < 24*7 and deadline > 24) :
    print("Chill ...")
else :
    print("copy paste")

