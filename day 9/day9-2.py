f = open("day9.txt", "r")

data = []
result = []

for x in f: 
  data.append(int(x))

while len(data) > 1:
  sum = 0
  cont = []
  for d in data:
    sum = sum +  d
    cont.append(d)
    if (sum == 756008079 and len(cont) > 1):
      print("hurray!")
      print(cont)
      result = cont
      break
    if (sum > 756008079):
      break
  del data[0]

min = result[0]
max = result[0]

for r in result:
  print(r)
  if (r < min): 
    min = r
  if (r > max):
    max = r
print('end')
print min
print max
print(min+max)
