# for迴圈
print("range(5):")
for i in range(5):
    print(i)

print("\nrange(1,5):")
for i in range(1,5):
    print(i)

print("\nrange(0,5,2):")  
for i in range(0,5,2):
    print(i)
    
print("\nrange(4,-1,-1):")  
for i in range(4,-1,-1):
    print(i)

print("----------我是分割線----------")
# while 迴圈

i = 0
while i < 5:
    print(i)
    i += 1

print()

i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break

print("----------我是分割線----------")

# 迴圈控制
for i in range(1, 5):
    if i == 2:
        continue
    if i == 4 :
        break
    print(i)

print()

i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    if i == 4 :
        break
    print(i)



