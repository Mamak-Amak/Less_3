
def val_checker(callback):

   def lam(*args):

      try:
         for i in lam(args):
            if i > 0 in args:
               print(f'callback value: {type(args)}: {args > 0}')
            res = callback(args)

         return res


      except ValueError:
         i <= 0
      return print(f'invalid Value: {type(args)}')


@val_checker(lambda x: x > 0)

def calc_cube(x):
   return x ** 3

print(calc_cube(2))
