"""
小高成功完成教授的要求，但是教授又開始刁難小高了......
教授表示這支程式不優雅，要求小高根據教授提供的架構完成這支程式
並且教授還要求小高設計一個函式，輸入商品和數量後，回傳總價格
"""

def add_product():
    pass

def edit_product():
    pass

def delete_product():
    pass

def show_product():
    pass

def get_total_price(product, quantity):
    pass

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
    
    if operation == 'e':
        product = input("欲購買商品: ")
        quantity = input("欲購買數量: ")
        print(f"據估總價: {get_total_price(product, quantity)}")
