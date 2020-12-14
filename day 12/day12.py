f = open("day12.txt", "r")

drc = []
val = []

for x in f: 
  cln = x.strip()
  drc.append(cln[0:1])
  val.append(int(cln[1:len(cln)]))

sail = "E"

xpos = 0
ypos = 0

for i in range(0,len(drc)):
  if (drc[i] == "N"):
    ypos = ypos + val[i]
  elif (drc[i] == "S"):
    ypos = ypos - val[i]
  elif (drc[i] == "E"):
    xpos = xpos + val[i]
  elif (drc[i] == "W"):
    xpos = xpos - val[i]
  elif (drc[i] == "L"):
    for i in range(0, (val[i] / 90)):
      if sail == "E":
        sail = "N"
      elif sail == "N":
        sail = "W"
      elif sail == "W":
        sail = "S"
      else:
        sail = "E"
  elif (drc[i] == "R"):
    for i in range(0, (val[i] / 90)):
      if sail == "E":
        sail = "S"
      elif sail == "S":
        sail = "W"
      elif sail == "W":
        sail = "N"
      else:
        sail = "E"
  else:
    if sail == "E":
      xpos = xpos + val[i]
    elif sail == "S":
      ypos = ypos - val[i]
    elif sail == "W":
      xpos = xpos - val[i]
    else:
      ypos = ypos + val[i]
  print (sail + ":" + str(xpos) + ":" + str(ypos))

print(xpos)
print(ypos) 

final = abs(xpos) + abs(ypos)
print(final)


