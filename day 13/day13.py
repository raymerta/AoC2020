f = open("day13.txt", "r")
input = []

for x in f: 
  input.append(x.strip())

start = int(input[0])
sched = input[1].split(",")

bus = []
for s in sched:
  if (s != "x"):
    bus.append(int(s))

nsched = []
for b in bus:
  mult = start / b
  cls = (mult+1) * b
  nsched.append(cls)

min = nsched[0]
for n in nsched:
  if (n < min):
    min = n

print(min)

result = (min-start) * bus[nsched.index(min)]
print(result)
