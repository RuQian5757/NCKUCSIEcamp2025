alist = []
for i in range(1, 10):
    alist.append(i * 2)

for i in range(len(alist)):
    print(f"alist[{i}]: {alist[i]}")

print("----------我是分割線----------")

blist = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(j * i)
    blist.append(temp)

for i in range(len(blist)):
    for j in range(len(blist[i])):
        print(f"{blist[i][j]:<2} ", end="")
    print()
    
