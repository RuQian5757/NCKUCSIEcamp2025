"""
字典 dict
    - 可依 key 取 value
    - key 不可重複

架構：
{
    key:value,
    key:value,
    key:value
}
"""

adict = {
    "a":1,
    "c":[1, 2, 3],
    "d":{
        "a":3,
        "b":4
    },
    123:"num"
}

print(adict)
print(adict['a'])
print(adict['d']['b'])

print("----------我是分割線----------")

bdict = {}

bdict['a'] = "apple"
bdict['b'] = "banana"
bdict['c'] = "coconut"
print(bdict)

bdict['a'] = 'avocado'
print(bdict)

