
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def higher_num(lst):
  new_lst = [second for first, second in zip(lst, lst[1:]) if second > first]
  return new_lst


print(higher_num(src))