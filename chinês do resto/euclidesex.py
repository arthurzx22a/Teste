def diofantina(a,b):
  mdc=1
  m1=1
  m2=0
  n1=0
  n2=1
  k=0
  if(a>b):
    copy = a
    a = b
    b = copy
    k=1

  while(mdc!=0 and a!=0):
    q = b//a;
    mdc = b%a
    b = a
    a = mdc
    mc = m2
    m2 = m1 - (m2*q)
    m1 = mc
    nc = n2
    n2 = n1 - (n2*q)
    n1 = nc
    
  if(k==0):
    inv=n1
  else:
    inv= m1
  
  return inv