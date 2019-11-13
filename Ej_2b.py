
def check_Number(x):
    if (0 <= x <= 100):
        return x 
    else:
        return -1 

def avgNumber (a1,a2,a3):
    return (a1+a2+a3)/3

a = input("Ingrese un numero:")
b = input("Ingrese un numero:")
c = input("Ingrese un numero:")

if (check_Number(a) * check_Number(b) * check_Number(c) < 0):
    print "ERROR"
else:
    print avgNumber(check_Number(a),check_Number(b),check_Number(c))
