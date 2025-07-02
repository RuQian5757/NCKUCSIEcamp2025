"""
dict 操作

len(容器) 回傳容器的長度

＊設定 key & value
    dict[key] = value

＊依鍵取值
    print(dict.get(key)) #若沒有該key，回傳 None
    print(dict[key]) #若沒有該key，報錯

＊字典 dict 
    - items() 回傳字典所有資料，架構為 [(key,value),(key,value),(key,value)]
    - keys() 回傳字典所有的鍵
    - values() 回傳字典所有的值
    - clear() 清空字典
    - pop(key) 從字典取出指定 key 的 value
    - get(key) 回傳字典指定 key 的value，若沒有該 key 則回傳 None
"""

adict = {
    "A":"Hi",
    "B":"Hello",
    "C":"World",
}

print(len(adict))
print(adict.items())
print(adict.keys())
print(adict.values())

print("----------我是分割線----------")

adict["D"] = "Python"
print(adict) #新增 key:"D"，對應value:"Python"

adict["A"] = "HiHiHi"
print(adict) #更新 key:"A"，更新value:"HiHiHi"

print("----------我是分割線----------")

print("adict['A']:", adict['A']) #依 key:"A"，取value
print("adict.get('A'):", adict.get('A')) #依 key:"A"，取value

# print("adict['P']:", adict['P']) #找不到 key，報錯 KeyError
print("adict.get('P'):", adict.get('P')) #找不到 lek，回傳 None

print("----------我是分割線----------")

#可利用.pop(key)將資料從字典刪除
print("adict.pop('A'):", adict.pop('A')) #取出 key:A 的值
print(adict)

# print("adict.pop('P'):", adict.pop('P')) #找不到 key，報錯 KeyError
print("adict.pop('P'):", adict.pop('P', None)) #找不到 key，回傳 None
print(adict)

print("----------我是分割線----------")

adict.clear()
print(adict)

