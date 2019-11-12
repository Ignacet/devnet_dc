
print (6+7+9+10)
print ("Hola Mundo")
print (8**3)
x=3
x += x-x
print(x)
print(x+1)

print min(2,3,4)
print max(2,-3,4,7,-5)

def tripled_function(x):
  return 3 * x

print(tripled_function(5))

def my_abs_substract(x1, x2):
  return abs(x1)-abs(x2)

print(my_abs_substract(-7, -3))

def km_to_miles(x):
  return x / 1.6
i = input("Ingrese los km:")
print(km_to_miles(i))