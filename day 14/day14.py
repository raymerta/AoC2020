def bincleaner(val):
  bn = bin(val)
  lnf = len(bn[2:len(bn)])
  final = "" 
  for i in range(0,36-lnf):
    final = final + "0"
  final = final + bn[2:len(bn)]
  return final

def maskcalc(mask, num):
  result = ''
  for i in range(0,len(num)):
    if (mask[i:i+1] != "X"):
      result = result + mask[i:i+1]
    else:
      result = result + num[i:i+1]
  result = '0b' + result
  result = int(result,2)

  return result

f = open("day14.txt", "r")

##parse the input

masks = []
cont = []

tloc = []
tval = []
tbin = []
for x in f:
  cln = x.strip()
  split = cln.split(" = ")
  if (split[0] == "mask"):
    masks.append(split[1])
    if (len(tloc) > 0):
      cont.append([tloc, tval, tbin])
      tloc = []
      tval = []
      tbin = []
  else:
    tloc.append(int(split[0][4:len(split[0]) - 1]))
    tval.append(int(split[1]))
    tbin.append(bincleaner(int(split[1])))
cont.append([tloc,tval,tbin])

##find duplicate
def finddup():
  dloc = []
  for i in range(0,len(cont)):
    rev = len(cont) - i -1
    locs = cont[rev][0]
    vals = cont[rev][1]
    bins = cont[rev][2]

    dupl = []
    for j in range(0,len(locs)):
      if locs[len(locs) - j - 1] in dloc:
        dupl.append(len(locs) - j - 1)
      else:
        dloc.append(locs[j])
    if (len(dupl) > 0): 
      for d in dupl:
        locs.pop(d)
        vals.pop(d)
        bins.pop(d)
  
##calculate with masking
addr = []
vals = []

for i in range(0,len(masks)):
  for j in range(0,len(cont[i][2])):
    if (cont[i][0][j] not in addr):
      addr.append(cont[i][0][j])
      vals.append(maskcalc(masks[i], cont[i][2][j]))
    else:
      idx = addr.index(cont[i][0][j])
      vals[idx] = maskcalc(masks[i], cont[i][2][j])



print(addr)
print(vals)
print(sum(vals))

def binconvert(val):
  return bin(val)


