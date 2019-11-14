import json

body = '{ "Nombre":"Ignacio" , "Apellido":"Cetkovich", "Datos" : {"Edad": 38} }'

print (type(body))
print (body)

data = json.loads(body)

print (type(data))

print (data)
print (data["Nombre"])
print (data["Datos"]["Edad"])

body =''
print (body)
body = json.dumps(data, sort_keys=True , indent=2)
print (body)
print (type(body))


data = '{ "Nombre":"Ignacio" , "Apellido":"Cetkovich", "Datos" : {"Edad": 38} }'

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open('data.txt') as json_file:
    data = json.load(json_file)
    print (data)



