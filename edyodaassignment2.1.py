def last(n): return n[-1]

def sortlistlast(tuples):
  return sorted(tuples, key=last)

print(sortlistlast([(100 , 200), (191 , 201), (104, 204), (123, 321), (192, 100)]))