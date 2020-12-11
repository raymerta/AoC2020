f = open("day8.txt", "r")

vali = []
valv = []
ins = []

for x in f: 
  cln = x.strip()
  spl = cln.split(" ")
  ins.append(spl[0])
  vali.append(spl[1][0:1])
  valv.append(spl[1][1:len(spl[1])])

chn = []

i = 0
while i < len(ins):
  if (ins[i] == 'jmp' or ins[i] == 'nop'):
    chn.append(i)
  i += 1

print(len(chn))

for c in chn:
  i = 0
  acc = 0
  icont = []
  while i < len(ins):
    if (ins[i] == 'acc'):
      if(vali[i] == '+'):
        acc = acc + int(valv[i])
      else:
        acc = acc - int(valv[i])
      i+=1
    else:
      if (i == c):
        if (ins[i] == 'jmp'):
          i += 1
        else:
          if(vali[i] == '+'):
            i = i + int(valv[i])
          else:
            i = i - int(valv[i]) 
      else:
        if (ins[i] == 'jmp'):
          if(vali[i] == '+'):
            i = i + int(valv[i])
          else:
            i = i - int(valv[i]) 
        else:
          i += 1     

    if (i == len(ins)):
      print("hurray!")
      print(acc)

    if i not in icont:
      icont.append(i)
    else:
      i = len(ins)
  

print(icont)
  
