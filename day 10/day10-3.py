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
treep = []
treev = []
tree = []

pattern = []

def tree(start, tp):
  while start < max:
    for i in [1,2,3]
      if (start + i in input):
        start = start + i
        if (tp == ""):
          tp = str(i)
        else:
          tp = tp + "-" + str(i)
        treep.append(tp)
        treev.append(start)
        break

  pattern.append(tp)
  if (len(pattern) % 1000 == 0):
    ##print(len(treep))
    print(len(pattern))
  ##if (tp in pattern):
    ##print(tp)

if len(treep) == 0:
  tree(0,"")

counter = 0
for tr in treep:
  counter += 1
  ##print(len(pattern))
  ##if (counter > 100):
    ##break
  trs = tr.split("-")
  lval = int(trs[len(trs)-1])

  if lval > 1:
    start = 0
    tp = ""
    if len(trs) > 1:
      while lval > 1: 
        tp = tr[0:len(tr)-1] + str(lval-1)
        tidx = treep.index(tr[0:len(tr)-2])
        start = treev[tidx] + (lval - 1)
        if (start in input and tp not in treep):
          treep.append(tp)
          treev.append(start)
          tree(start,tp)
        lval = lval - 1    
    else:
      start = lval - 1
      if (start in input):
        tp = str(start)
        treep.append(tp)
        treev.append(start)

        tree(start,tp)

    
#print(treep)
#t(treev)
print(len(sectreep))
print(len(treep))
print(len(pattern))

##for t in treep:
##  print("#" + t)
