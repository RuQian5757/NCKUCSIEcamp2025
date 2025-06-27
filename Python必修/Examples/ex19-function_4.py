x = 10
y = 100
alist = [1, 2, 3]
adict = {'a': "apple", 'b': "banana"}

def f(x = 5):
    y = 5
    print(f"func x: {x}, y: {y}")
    print(alist)
    print(adict)
    alist[0] = 5
    adict['b'] = "berry"

f(20)
print(f"global x: {x}, y: {y}")
print(alist)
print(adict)