import os

# 讀取檔案
def read_product(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
    return products
    
# 輸入檔案
def keyin(products):
    while True:
        name = input('請輸入產品名稱:')
        if name == 'q':
            break
        price = input('請輸入產品價格:')
        products.append([name, price])
    print(products)
    return products

# 列印資料
def print_product(products):
    for p in products:
        print(p[0], '價錢是: ', p[1], '元' )

# 寫入檔案
def write_product(filename_write, products):
    with open(filename_write, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('找到檔案了!')
        products = read_product(filename)
    else:
        print('找不到檔案!!!')
    
    products = keyin(products)
    print_product(products)
    write_product('products.csv', products)
main()