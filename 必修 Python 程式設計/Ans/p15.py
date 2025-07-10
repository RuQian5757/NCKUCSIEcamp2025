"""
小高成功完成教授的要求，但是教授又開始刁難小高了......
教授表示這支程式不優雅，要求小高根據教授提供的架構完成這支程式
並且教授還要求小高設計一個函式，輸入商品和數量後，回傳總價格
"""

def add_product(name, price):
    if name in shopping_dict:
        print("此商品已存在")
        return
    shopping_dict[name] = price
    print(f"已新增商品: {name}")

def edit_product(name, new_price):
    if name not in shopping_dict:
        print("查無此商品")
        return
    print(f"目前價格: {shopping_dict[name]}")
    shopping_dict[name] = new_price
    print(f"已更新商品: {name}")

def delete_product(name):
    if name not in shopping_dict:
        print("查無此商品")
        return
    shopping_dict.pop(name)
    print(f"已刪除商品: {name}")

def show_product():
    if not shopping_dict:
        print("目前沒有任何商品")
    else:
        for name, price in shopping_dict.items():
            print(f"名稱: {name} / 價格: {price}")

def get_total_price(product, quantity):
    if product not in shopping_dict:
        return "查無此商品"
    return shopping_dict[product] * quantity

# 主程式區
shopping_dict = {}

while True:
    print("\n===== 商店貨架系統 =====")
    print("a. 新增商品")
    print("b. 編輯商品")
    print("c. 刪除商品")
    print("d. 顯示所有商品")
    print("e. 獲取估價")
    print("q. 離開系統")

    operation = input("請選擇操作: ")

    if operation == 'q':
        print("離開系統")
        break

    elif operation == 'a':
        name = input("請輸入要新增的商品名稱: ")
        price = int(input("請輸入商品價格: "))
        add_product(name, price)
    elif operation == 'b':
        name = input("請輸入要編輯價格的商品: ")
        if name not in shopping_dict:
            print("查無此商品")
            continue
        new_price = int(input("請輸入新價格: "))
        edit_product(name, new_price)

    elif operation == 'c':
        name = input("請輸入要刪除的商品名稱: ")
        delete_product(name)

    elif operation == 'd':
        show_product()

    elif operation == 'e':
        name = input("欲購買商品: ")
        quantity = int(input("欲購買數量: "))
        result = get_total_price(name, quantity)
        print(f"估算總價: {result}")

    else:
        print("無效的操作代號")
