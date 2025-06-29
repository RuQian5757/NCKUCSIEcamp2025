"""
小高的專題需要製作一個商店資訊顯示系統，小高表示：根本不慌，因為有小幫手幫他！
請幫他完成以下各操作代號的功能，讓他能夠在 Deadline 前交出作品。

所有操作代號與對應的功能：
a. 新增商品
b. 替換商品
c. 刪除商品
d. 顯示所有商品
q. 離開系統


範例輸入輸出：

請選擇操作: d
目前沒有任何商品

請選擇操作: a
請輸入要新增的商品名稱: 牛奶
已新增商品: 牛奶

請選擇操作: a
請輸入要新增的商品名稱: 吐司
已新增商品: 吐司

請選擇操作: a
請輸入要新增的商品名稱: 烤田螺
已新增商品: 烤田螺

請選擇操作: d
0 牛奶
1 吐司
2 烤田螺

請選擇操作: b
請輸入要替換的商品編號: 1
替換商品: 雞翅
已更新商品 吐司 -> 雞翅

請選擇操作: c
請輸入要刪除的商品編號: 0
已刪除商品: 牛奶

請選擇操作: c
請輸入要刪除的商品編號: 100
查無此商品

請選擇操作: q
離開系統
"""

product_list = []

while True:
    print("\n===== 商店貨架系統 =====")
    print("a. 新增商品")
    print("b. 編輯商品")
    print("c. 刪除商品")
    print("d. 顯示所有商品")
    print("q. 離開系統")

    operation = input("請選擇操作: ")

    if operation == 'q':
        print("離開系統")
        break