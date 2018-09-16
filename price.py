products = []

#讀取檔案
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

while True:
	name = input('請輸入產品名稱:')
	if name == 'q':
		break
	price = input('請輸入產品價格:')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '價錢是: ', p[1], '元' )


with open('products.csv', 'w', encoding='utf-8') as f:
	if products[0][0] != '商品':
		f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')