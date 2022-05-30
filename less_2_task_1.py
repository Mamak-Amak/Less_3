#1-е задание

print(type(5 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))
#2-е задание

name = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
'была', '+5', 'градусов']

for hs in name:
    hs = 5
for min in name:
    min = 17
for tp in name:
    tp = '"+5"'

name = f'в "{hs:.2f}" часов "{min:.2f}" минут температура воздуха была {tp} градусов.'

print(name)


