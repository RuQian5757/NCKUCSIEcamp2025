# 字串格式化
# format
a = 10
b = 5
print("{} + {} = {}".format(a, b, a+b))
print("{} - {} = {}".format(a, b, a-b))
print("{0} * {1} = {2}".format(a, b, a*b))
print("{1} / {2} = {0}".format(a/b, a, b))

print("----------我是分割線----------")
# f-string

a = 10
b = 5
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")

