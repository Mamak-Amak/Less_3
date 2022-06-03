
key_num = {"one":"один",
           "two":"два",
           "three":"три",
           "four":"четыре",
           "five":"пять",
           "six":"шесть",
           "seven":"семь",
           "eight":"восемь",
           "nine":"девять",
           "ten":"десять"}

def num_translite(add):
    if key_num.get(f'{add}', None) == None:
        return None
    else:
        return key_num.get(f'{add}')

print(num_translite(input("Введите английскими буквами число от 1 до 10: ")))






#rus_trl = ("один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять")

#input('Введите цифру прописью на английском, от 1 до 10: ')

#Создание блока кода для перевода:

