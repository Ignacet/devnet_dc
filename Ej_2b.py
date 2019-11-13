
def check_Number(_x):
    if (0 <= _x <= 100):
        return _x 
    else:
        return -1 

def avgNumber (_a1,_a2,_a3):
    return (_a1+_a2+_a3)/3

valores = []

a = input("Ingrese un numero:")
b = input("Ingrese un numero:")
c = input("Ingrese un numero:")
d = input("Ingrese un numero:")

valores.insert(0,check_Number(a))
valores.insert(0,check_Number(b))
valores.insert(0,check_Number(c))
valores.insert(0,check_Number(d))

print (valores)
valores.sort()

result = check_Number(valores[1]) * check_Number(valores[2]) * check_Number(valores[3])

if ( result < 0):
    print "ERROR"
else:
    print avgNumber(check_Number(valores[1]),check_Number(valores[2]),check_Number(valores[3]))
