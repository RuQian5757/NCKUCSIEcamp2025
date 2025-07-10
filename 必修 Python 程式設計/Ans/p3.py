"""
輸入一個年份 year，若為閏年輸出 yes，不是則輸出 no

1. 被4整除 但 不被100整除
2. 被400 整除

範例一：
< 2023
> no

範例二：
< 2020
> yes
"""

year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print('yes')
elif year % 400 == 0:
    print('yes')
else:
    print('no')
    
