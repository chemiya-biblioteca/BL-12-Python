
#@@@###$$$----------funcion--------------@@@###$$$
x = 300#global

def myfunc():
  x = 200#para esta zona nueva
  #si lo quito sacaria 300
  print(x)

myfunc()

print(x)


#@@@###$$$----------datetime--------------@@@###$$$
import datetime

x = datetime.datetime.now()#fecha y hora actual
print(x)

print(x.day)#solo dia
x = datetime.datetime(2020, 5, 17)
print(x.strftime("%B"))#en un formato


#@@@###$$$----------funciones matematicas--------------@@@###$$$
num=pow(3,4)
print(num)

import math
numero=4.3
numero=math.ceil(numero)
print(numero)



#@@@###$$$----------json--------------@@@###$$$
import json
varjson =  '{ "name":"John", "age":30, "city":"New York"}'#string con tod el json
y = json.loads(varjson)#lo cargo
print(y["age"])#imprimo un campo


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)#vuelco todo
print(y)



#@@@###$$$----------expresiones regulares--------------@@@###$$$
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)#buscan que empiecen por the y terminen spain
print(x)
x = re.findall("ai", txt)#encuentra todos ai
print(x)
x = re.search("\s", txt)#encuentra donde esta el primer espacion
print("The first white-space character is located in position:", x.start())
x = re.split("\s", txt)#separa por espacios
print(x)
x = re.sub("\s", "9", txt)#sustituye espacios por 9
print(x)
x = re.search(r"\bS\w+", txt)#busca que empiecen por S y saca su posicion
print(x.span())
x = re.search(r"\bS\w+", txt)
print(x.string)#saca la cadena de entrada
x = re.search(r"\bS\w+", txt)
print(x.group())#saca donde se cumple

#pip install camelcase
#pip list