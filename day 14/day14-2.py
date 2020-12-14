def bincleaner(val, space):
  bn = bin(val)
  lnf = len(bn[2:len(bn)])
  final = "" 
  for i in range(0,space-lnf):
    final = final + "0"
  final = final + bn[2:len(bn)]
  return final

def maskpatt(mask, num):
  result = ''
  fn = 0
  idxs = []
  for i in range(0,len(num)):
    if (mask[i:i+1] != "0"):
      if (mask[i:i+1] == "X"):
        fn = fn + 1
        idxs.append(i)
      result = result + mask[i:i+1]
    else:
      result = result + num[i:i+1]

  patt = createpatt(fn, idxs, result)
  return patt

def createpatt(n, idxs, tmpl):
  bs = ""
  for i in range(0,n):
    bs = bs + "1"

  itert = '0b' + bs
  itert = int(itert,2)

  ptts = []
  for i in range(0,itert+1):
    patt = bincleaner(i, n)
    ptts.append(int('0b' + minpatt(patt, idxs, tmpl),2))

  
  return ptts  

def minpatt(patt, idxs, tmpl):
  output = ''
  pointer = 0
  for i in range(0,len(idxs)):
    output = output + tmpl[pointer:idxs[i]] + patt[i]
    pointer = idxs[i] + 1
  
  return output

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
    addr = int(split[0][4:len(split[0]) - 1])
    tloc.append(addr)
    tval.append(int(split[1]))
    tbin.append(bincleaner(addr,len(masks[0])))
cont.append([tloc,tval,tbin])

addr = []
vals = []

for i in range(0,len(masks)):
  for j in range(0,len(cont[i][2])):
    result = maskpatt(masks[i], cont[i][2][j])
    for r in result:
      if (r not in addr):
        print(r)
        addr.append(r)
        vals.append(cont[i][1][j])
      else:
        idx = addr.index(r)
        vals[idx] = cont[i][1][j]
    
#print(addr)
#print(vals)
print(sum(vals))




