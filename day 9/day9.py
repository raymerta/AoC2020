f = open("day9.txt", "r")

cont = []
found = False

for x in f: 
  if (not found):
    if (len(cont) < 25):
      cont.append(int(x))
    else:
      print(cont)
      for c in cont:
        i = int(x) - c
        if ((i in cont) and i != c):
          del cont[0]
          cont.append(int(x))
          break
        else:
	  if (cont.index(c) == 24):
            print(x)
            found = True
  else:
    break
