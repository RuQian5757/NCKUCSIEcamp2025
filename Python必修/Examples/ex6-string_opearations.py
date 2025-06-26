a_str = "abc, 123, hi"
print(len(a_str))
print(f"astr.split(','): {a_str.split(',')}")
print(f"astr.split(', '): {a_str.split(', ')}")
print(f"astr.replace(', ', '-'): {a_str.replace(', ', '-')}")

print("----------我是分割線----------")

b_str = "|||hello|||"
print(f"bstr.strip('|'): {b_str.strip('|')}")
print(f"bstr.lstrip('|'): {b_str.lstrip('|')}")
print(f"bstr.rstrip('|'): {b_str.rstrip('|')}")
print(f"bstr.count('|'): {b_str.count('|')}")

print("----------我是分割線----------")

c_str = "abCdEFg"
print(f"cstr.title(): {c_str.title()}")
print(f"cstr.upper(): {c_str.upper()}")
print(f"cstr.lower(): {c_str.lower()}")

print("----------我是分割線----------")

d_str = "ABCabc"
print(f"d_str.index('c'): {d_str.index('c')}")
print(f"d_str.find('C'): {d_str.find('C')}")
print(f"d_str.find('e'): {d_str.find('e')}")
print(f"d_str.index('e'): {d_str.index('e')}") # error