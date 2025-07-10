"""
小高 Deadline 押成功了！但是教授說沒有顯示價格，學生菜菜當當！
小高慌了，趕快幫他補上顯示價格的功能吧！

所有操作代號與對應的功能：
a. 新增商品
b. 編輯商品價格
c. 刪除商品
d. 顯示所有商品
q. 離開系統


範例輸入輸出：

請選擇操作: d
目前沒有任何商品

請選擇操作: a
請輸入要新增的商品名稱: 牛奶
請輸入商品價格: 55
已新增商品: 牛奶

請選擇操作: d
名稱: 牛奶 / 價格: 55

請選擇操作: b
請輸入要編輯價格的商品: 牛奶
目前價格: 55
請輸入新價格: 60
已更新商品: 牛奶

請選擇操作: c
請輸入要刪除的商品名稱: 牛奶
已刪除商品: 牛奶

請選擇操作: q
離開系統
"""

product_dict = {}

while True:
    print("\n===== 商店貨架系統 =====")
    print("a. 新增商品")
    print("b. 編輯商品價格")
    print("c. 刪除商品")
    print("d. 顯示所有商品")
    print("q. 離開系統")

    operation = input("請選擇操作: ")

    if operation == 'q':
        print("離開系統")
        break

    elif operation == 'a':
        name = input("請輸入要新增的商品名稱: ")
        if name in product_dict:
            print("此商品已存在")
            continue
        price = int(input("請輸入商品價格: "))
        product_dict[name] = price
        print(f"已新增商品: {name}")

    elif operation == 'b':
        name = input("請輸入要編輯價格的商品: ")
        if name not in product_dict:
            print("查無此商品")
            continue
        print(f"目前價格: {product_dict[name]}")
        new_price = int(input("請輸入新價格: "))
        product_dict[name] = new_price
        print(f"已更新商品: {name}")

    elif operation == 'c':
        name = input("請輸入要刪除的商品名稱: ")
        if name not in product_dict:
            print("查無此商品")
            continue
        product_dict.pop(name)
        print(f"已刪除商品: {name}")

    elif operation == 'd':
        if not product_dict:
            print("目前沒有任何商品")
        else:
            for name, price in product_dict.items():
                print(f"名稱: {name} / 價格: {price}")

