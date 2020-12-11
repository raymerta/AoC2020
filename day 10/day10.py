f = open("day10.txt", "r")

input = []


for x in f: 
  cln = x.strip()
  input.append(int(cln))

input.sort()

min = 0
max = 0

for i in input:
  if (i > max):
    max = i

def pattgen(prevpath, nc, seed):
  #print("pattgen")
  #print(prevpath)
  start = 0
  c = "0"
  p = "0"
  
  if (len(prevpath) > 0 and nc > 1):
    ppl = len(prevpath)
    for pv in prevpath:
      if (int(pv) > 0):
        start = start + int(pv)
        p = p + "-" + str(pv)
        c = c + "-" + str(start)

    #print(nc)
    red = nc - 1
    while red > 0:  
      if (start + red in input):
        start = start + red
        c = c + "-" + str(start)
        p = p + "-" + str(red)
        break
      else:
        red = red - 1

    if (nc == 1):
      start = start + nc
      c = c + "-" + str(start)
      p = p + "-" + str(nc)

  while start < seed:
    i = 3
    while i > 0: 
      if (start + i in input):
        start = start + i
        c = c + "-" + str(start)
        p = p + "-" + str(i)
        break
      i = i - 1

  #print(c)
  #print(p)
  return(c,p)

cont = []
patt = []

if len(patt) == 0:
  (c,p) = pattgen([],0,max)
  cont.append(c)
  patt.append(p)

counter = 0
for pt in patt:
  ptsplit = pt.split("-")
  i = 0
  counter += 1
  print(counter)
  while i < len(ptsplit):
    if (i + 1 < len(ptsplit)):
      (c,p) = pattgen(ptsplit[0:i+1], int(ptsplit[i+1]), max)
      if c not in cont: 
        cont.append(c)

      if p not in patt:  
        patt.append(p)
    i += 1
  #if (counter == 1):
    #break

print(len(cont))
print(len(patt))
