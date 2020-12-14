import copy

f = open("day11.txt", "r")

seats = []
old = ""

for x in f: 
  cln = x.strip()
  old = old + cln
  row = []
  for i in range(0, len(cln)):
    row.append(cln[i])
  seats.append(row)

col = len(seats)
row = len(seats[0])

def adj(r,c):
  if (r > -1 and r < row and c > -1 and c < col):
    return seats[r][c]
  else:
    return ""

def empty(adjs):
  for a in adjs:
    if (a == "#"):
      return False
  return True

def occupied(adjs):
  sum = 0
  for a in adjs:
    ##print(a + " - " + str(sum))
    if (a == "#"):
      sum = sum + 1

  if (sum > 4):
    return True
  else:
    return False

def create_adjs(mi,mj,row,col): 
  adjs = []

  for i in range(1,row):
    vadj = adj(mi-i,mj-i)
    if (vadj == "#" or vadj == "L"):
      adjs.append(vadj)
      break

  for i in range(1,row):
    vadj = adj(mi-i,mj) 
    if (vadj == "#" or vadj == "L"):
      adjs.append(vadj)
      break
  
  for i in range(1,row): 
    vadj = adj(mi-i,mj+i)
    if (vadj == "#" or vadj == "L"):
      adjs.append(vadj)
      break

  for i in range(1,row):  
    vadj = adj(mi,mj-i)
    if (vadj == "#" or vadj == "L"):
      adjs.append(vadj)
      break

  for i in range(1,row):  
    vadj = adj(mi,mj+i)
    if (vadj == "#" or vadj == "L"):
      adjs.append(vadj)
      break

  for i in range(1,row):  
    vadj = adj(mi+i,mj-i)
    if (vadj == "#" or vadj == "L"):
      adjs.append(vadj)
      break

  for i in range(1,row): 
    vadj = adj(mi+i,mj) 
    if (vadj == "#" or vadj == "L"):
      adjs.append(vadj)
      break

  for i in range(1,row):  
    vadj = adj(mi+i,mj+i)
    if (vadj == "#" or vadj == "L"):
      adjs.append(vadj)
      break
      
  return adjs

cycle = 0
new = ""
nseats = []

while old != new:
  cycle += 1
  print(cycle)
  old = new
  new = ""

  nseats = []
  for i in range(0,row):
    nrow = []
    for j in range(0,col):
      pos = seats[i][j]
      if (pos == "."):
        nrow.append(seats[i][j])
        new = new + seats[i][j]
      else:        
        adjs = create_adjs(i,j,row,col)
        #print(adjs)
      
        if(pos == "L"):
          if (empty(adjs)):
            nrow.append("#")
            new = new + "#"
          else: 
            nrow.append(seats[i][j])
            new = new + seats[i][j]
        elif(pos == "#"):
          if (occupied(adjs)):
            nrow.append("L")
            new = new + "L"
          else:
            nrow.append(seats[i][j])
            new = new + seats[i][j]
 
    nseats.append(nrow)

  #for n in nseats:
  #  print(n)
  seats = copy.deepcopy(nseats)
 
total = 0 
for s in seats:
  for d in s: 
    if (d == "#"):
      total = total + 1

print(total)
#print(seats)
