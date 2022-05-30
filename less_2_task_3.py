items = [45.5, 234.2, 450,
         118.3, 374.7, 290,
         782.7, 550.3, 621.5,
         703.4, 854.7, 945,
         143.6, 666.6, 332]

d_id = id(items)

endding = ','

for i, goods in enumerate(items):
    price = str(f'{(goods):.2f}').split('.')
    if i == len(items)-1:
        ending = '\n'
        print(f'{price[0]} руб {price[1]} коп')

print(id(items))
items.sort()
if id(items) == d_id:
    print('ID одинаковые: ', d_id, id(items))




