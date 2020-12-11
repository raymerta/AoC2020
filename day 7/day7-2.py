f = open("day7.txt", "r")
ref = []
cont = []

for x in f:
  cln = x.strip()
  spl = cln.split(":")
  ref.append(spl[0])
  cont.append(spl[1].split(","))

init = []

sgi = ref.index("shiny-gold")
sgc = cont[sgi]

for c in sgc:
  print(c)
  obj = c.split("+")
  qty = obj[0]
  clr = obj[1]
  if (clr in ref):
    idx = ref.index(clr)
    for d in cont[idx]:
      o = d.split("+")
      q = o[0]
      cl = o[1]
      if(cl != "-"):
      	sgc.append(qty + "*"+ q + "+" + cl)
  
for num in sgc 

#print(sgi)
#print(sgc)

  
