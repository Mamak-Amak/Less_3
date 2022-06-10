tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def gen_students():
        for i, t in enumerate(tutors):
            if i<len(klasses):
                yield t, klasses[i]
            else:
                yield (t, None)

print(type(gen_students()))
gen=gen_students()
for g in gen:
    print(g)