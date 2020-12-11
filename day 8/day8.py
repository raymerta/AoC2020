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
  
  if (ins[i] == 'jmp'):
    if(vali[i] == '+'):
      i = i + int(valv[i])
    else:
      i = i - int(valv[i])
  
  if (ins[i] == 'nop'):
    i += 1

  if i not in icont:
    icont.append(i)
  else:
    i = len(ins)
  

print(acc)
  
