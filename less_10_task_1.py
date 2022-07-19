class Matrix:
  def __init__(self, data):
    self.data = data

  def __str__(self):
    return '\n'.join('\t'.join([f"{itm:03}" for itm in line]) for line in self.data)

  def __add__(self, other):
    try:
      m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
           for line in range(len(self.data))]
      return Matrix(m)
    except IndexError:
      return f'bending the dimensions of matrices'

m_1 = [[5, 4, 1,], [6, 3, 4,], [5, 0, 7,]]
m_2 = [['3', '4', '3'], ['1', '1','0'], ['3', '9', '3',]]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_matrx = mtrx_1 + mtrx_2






    