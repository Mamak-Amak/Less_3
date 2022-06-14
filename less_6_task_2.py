from json import dump
from itertools import zip_longest

with open("Users.csv", 'r', encoding='utf-8') as us:
    with open("Hobby.csv", 'r', encoding='utf-8') as h:
        end_result = zip_longest((" ".join(names.split(",")) for names in us), h, fillvalue=None)
        slovar = {str(i[0]).strip(): (str(i[1]).strip()) if i[0] else exit(1) for i in end_result}

        with open("Conc_Users_Hobby_dict.txt", 'w', encoding='utf-8') as new_d:
            dump(slovar, new_d, ensure_ascii=False, indent=0)

            print(slovar)


