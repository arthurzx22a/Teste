import euclidesex
num_inv = [] 
equa = []
sys = []
mod_total = 1
t=0
k=0
equa.append(1)
equa.append(1)
equa.append(1)

num_equa = int(input('Digite o número de equações:'))
for i in range(0,num_equa):
  equa[0] = int(input('Digite o coeficiente do x:'))
  equa[1] = int(input('Digite o valor congruente a x:'))
  equa[2] = int(input('Digite o valor do mod:'))
  sys.append(equa[:])
  if(sys[i][0]!=1):
    inv = euclidesex.diofantina(sys[i][0],sys[i][2]);
    inv = inv % sys[i][2]
    sys[i][1] = sys[i][1] * inv
    print("inverso de {} numero multiplicado={} !!{}!! ".format(i, inv, sys[i][2]))
    sys[i][1] = sys[i][1] % sys[i][2] 
    sys[i][0] = 1
 

for i in range(0,num_equa):
    mod_total = mod_total*sys[i][2]
    
print(mod_total)

num_inv = []
numinv = []
numinv.append(1)

for i in range(0,num_equa):
  k = int(mod_total/sys[i][2])
  numinv[0] = euclidesex.diofantina(k, sys[i][2])
  numinv[0] = numinv[0] % sys[i][2]
  print("numinv={}".format(numinv))
  num_inv.append(numinv[:])


for i in range(0,num_equa): 
  t += (mod_total/sys[i][2]) * sys[i][1] * (num_inv[i][0])

r = t%mod_total
print("resposta={}".format(r))