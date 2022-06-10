def odd_to_20(n):
  for odd in range(1, n+1, 2):
    yield odd

gen = odd_to_20(20)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))