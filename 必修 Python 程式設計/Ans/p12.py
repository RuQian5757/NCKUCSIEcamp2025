"""
輸入一個 n，輸出 n 層星號沙漏


範例一輸入：
3

範例一輸出：
***
 *
***

範例二輸入：
5

範例二輸出：
*****
 ***
  *
 ***
*****
"""

n = int(input())

half = n // 2  # 一半的行數

# 上半部（含中間）
for i in range(half + 1):
    stars = n - 2 * i
    spaces = i
    print(' ' * spaces + '*' * stars)

# 下半部
for i in range(half - 1, -1, -1):
    stars = n - 2 * i
    spaces = i
    print(' ' * spaces + '*' * stars)