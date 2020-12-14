f = open("day13.txt", "r")
input = []

for x in f: 
  input.append(x.strip())

start = int(input[0])
sched = input[1].split(",")

bus = []
bdif = []

sbdif = 0 
for s in sched:
  if (s != "x"):
    bus.append(int(s))
    bdif.append(sbdif)
  sbdif += 1

#rearrange
rbus = sorted(bus, reverse=True)
rdif = []
for b in rbus:
  rdif.append(bdif[bus.index(b)])

print(bus)
print(bdif)
print(rbus)
print(rdif)

#seed = (101049994908320 / rbus[0]) * rbus[0]
#seed = 1068774
#seed = 1068785 - (2*rbus[0])
base = 1
seed = rbus[0]
ndif = rdif[0]

first = 0
result = []

current = 1
while current < len(rbus):
  #print("SEED:" + str(seed))
  check = seed + (rdif[current] - ndif)
  if (check % rbus[current] == 0): 
    if first == 0:
      if current == (len(rbus) - 1):
        print('hurray!')
        print(seed)
        result.append(seed)
        break
      first = seed
      seed = seed + (base * rbus[0])
    else:
      dist = seed - first
      base = dist / rbus[0]
      first = 0 
      current += 1
      seed = seed + (base * rbus[0])
      print("DIST:" + str(dist))
  else:
    seed = seed + (base * rbus[0])

for i in range(1,len(rbus)):
  result.append(result[0] + (rdif[i] - ndif))

print(result)
print(min(result))
