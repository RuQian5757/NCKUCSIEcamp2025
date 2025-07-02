alist = [1, 5, 4, 8, 9, 8, 10]

print("len(alist):", len(alist))

alist.append(0) #將 0 新增到alist尾部
print("append(0):", alist)

alist.insert(1, "hi") #在1號位置插入 "hi"
print('insert(1, "hi")', alist)

print("pop()回傳:", alist.pop()) #取出尾部資料
print("pop():", alist)

print("pop(1)回傳:", alist.pop(1)) #取出1號位置資料
print("pop(1):", alist)

print("max(alist):", max(alist))
print("min(alist):", min(alist))

print("count(8)回傳:", alist.count(8)) #回傳資料8在alist中有幾個

alist.remove(8) #刪除資料8
print("remove(8):", alist)

print("index(4)回傳:", alist.index(4)) #回傳資料4的位置，找不到時報錯

alist.reverse() #也可以 alist = alist[::-1]
print("reverse():", alist)

alist.sort() #排序(預設升冪)
print("sort():", alist)

alist.sort(reverse=True) #排序(降冪)
print("sort(reverse=True):", alist)

