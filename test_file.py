def gen():
  yield 1
  yield 2
  yield 3
for x in gen():
  print(x)
#print(next(x))
