f = open("day12.txt", "r")

drc = []
val = []

for x in f: 
  cln = x.strip()
  drc.append(cln[0:1])
  val.append(int(cln[1:len(cln)]))

wps = "E"

wpx = 10
wpy = 1

xpos = 0
ypos = 0

for i in range(0,len(drc)):
  if (drc[i] == "N"):
    wpy = wpy + val[i]
  elif (drc[i] == "S"):
    wpy = wpy - val[i]
  elif (drc[i] == "E"):
    wpx = wpx + val[i]
  elif (drc[i] == "W"):
    wpx = wpx - val[i]
  elif (drc[i] == "L"):
    if (val[i]/90) == 2:
      wpx = wpx * -1
      wpy = wpy * -1
    elif (val[i]/90 == 1): 
      owpx = wpx
      wpx = wpy * -1
      wpy = owpx
    elif (val[i]/90 == 3):
      owpx = wpx
      wpx = wpy
      wpy = owpx * -1
  elif (drc[i] == "R"):
    if (val[i]/90) == 2:
      wpx = wpx * -1
      wpy = wpy * -1
    elif (val[i]/90 == 3): 
      owpx = wpx
      wpx = wpy * -1
      wpy = owpx
    elif (val[i]/90 == 1):
      owpx = wpx
      wpx = wpy
      wpy = owpx * -1
  else:
    xpos = xpos + wpx * val[i]
    ypos = ypos + wpy * val[i]
  print ("wps:"+ str(wpx) + ":" + str(wpy))
  print ("pos:" + str(xpos) + ":" + str(ypos))
  print ("---")

print(xpos)
print(ypos) 

final = abs(xpos) + abs(ypos)
print(final)


