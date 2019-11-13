
def check_Number(x):
  if (0 <= x <= 100):
   return x 
  else:
    return -1 

a = input("Ingrese un numero:")
b = input("Ingrese un numero:")
c = input("Ingrese un numero:")
result = (check_Number(a) + check_Number(b) + check_Number(c))/3

if (check_Number(a) * check_Number(b) * check_Number(c) < 0):
    print "ERROR"
else:
    print result