f = open("day7.txt", "r")
ref = []
cont = []

for x in f:
  cln = x.strip()
  spl = cln.split(":")
  ref.append(spl[0])
  cont.append(spl[1].split(","))

init = []

for c in cont:
  for d in c: 
    obj = d.split("+")
    qty = obj[0]
    clr = obj[1]
    if (clr == "shiny-gold"):
      init.append(cont.index(c))

print(init)

for i in init:
  for c in cont:
    for d in c:
      obj = d.split("+")
      qty = obj[0]
      clr = obj[1]
      if (clr == ref[i]):
        init.append(cont.index(c))

san = []

for i in init:
  if(i not in san):
    san.append(i) 

print(init)
print(len(init))
print(len(san))

  
