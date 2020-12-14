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

seed = (101049994908320 / rbus[0]) * rbus[0]
#seed = 1068774
#seed = 1068785 - (2*rbus[0])
found = False
ndif = rdif[0]


while not found:
  print(seed)
  for i in range(1,len(rbus)):
    check = seed + (rdif[i] - ndif) 
    if(check % rbus[i] != 0):
      print(i)
      found = False
      break
    found = True
  seed = seed + rbus[0]

print("result")
print(seed - rbus[0] - ndif)
