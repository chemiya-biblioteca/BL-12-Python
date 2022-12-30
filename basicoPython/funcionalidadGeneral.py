
#@@@###$$$----------conversion y entrada teclado--------------@@@###$$$
print("holaaa")
texto = "chema"
edad = 21
print(texto+"  -  "+str(edad))#conversion de un int
print(f"{texto}-{str(edad)}")#otra forma de imprimir
entrada = input("dime")#entrada de texto
print("ha metido "+entrada)#salida imprimo


altura = 198

altura = int(input("dime altura  "))#convertir a int




#@@@###$$$----------funcion--------------@@@###$$$
def mostrarAltura(altura):
    resultado=""

    if altura >= 100:
        resultado="eres alto"

    else:
        resultado="no eres alto"

    return resultado


print(mostrarAltura(altura))



#@@@###$$$----------operaciones sobre listas--------------@@@###$$$
personas=["paco","pepe"]
print(len(personas))#longitud
listavariada=["sss",334,False]#pueden ser de diferentes tipos
listavariada.append("chema")#anado al final
listavariada.insert(2,"meto")#pongo en la posicion 2
personas.extend(listavariada)#a personas al final le pongo la otra
personas.remove("paco")#elimino un elemento
personas.pop(3)#elimino en posicion
del personas[4]#elimino en posicion
print(personas[1])#saco lo de la posicion
print(listavariada[1:])#saco de 1 al final



#@@@###$$$----------recorrer listas--------------@@@###$$$
for persona in personas:
    print("-"+str(persona))#recorro con los elementos

for i in range(len(personas)):
    print(personas[i])#recorro de manera normal

while i<len(personas):
    print(personas[i])#recorro normal
    i=i+1



#@@@###$$$----------if de una linea--------------@@@###$$$
nombre=["sss","ffggh","sskdoof"]
[print(x) for x in nombre ]#imprimo con expresion reducida
nueva=[x for x in nombre if "f" in x]
#recorro el de nombre, si tiene una f la pongo en nueva
print(nueva)



#@@@###$$$----------ordenar lista--------------@@@###$$$
listnumeros=[23,33,21,234,52,1,2]
listnumeros.sort()#ordeno lista de numeros

def numabs(n):
    return abs(n-50)

listnumeros.sort(key=numabs)#ordeno segun funcion
print(listnumeros)



#@@@###$$$----------copiar lista y juntar--------------@@@###$$$
listnumeros.reverse()#la pongo al reves
copia=listnumeros.copy()
copia1=list(listnumeros)
#para copiar lista de dos maneras

copia=copia+copia1
for x in copia1:
    copia.append(x)

copia.extend(copia1)
#para juntar listas: sumando, append, extend


#@@@###$$$----------tupla--------------@@@###$$$
tuplade1=("sss",)#tupla de 1

if "sss" in nombre:
    print("si esta")#comprobar si un elemnto esta en una lista


tupla1=("sss","ssdf","ffg","dddfg")
lista1=list(tupla1)#convierto a lista
lista1[3]="sssddfg"#cambio elemento
lista1.append("ssksk")#anado elemento
lista1.remove("sss")# elimino
tupla1=tuple(lista1)# la reconvierto
tupla2=("sssd","sssdf")
tupla1+=tupla2#juntar tuplas


frutas=("sss","ddd","444","dder","eedff")
(uno,dos,*tres)=frutas#asignar a cada variable un elemento
#si hay mas y sobran, *
print(uno)

tuplamult=tupla1*2#dos veces una tupla



#@@@###$$$----------conjunto--------------@@@###$$$
conjunto={"sssd","sss","ssdg"}#conjunto entre llaves
conjunto.add("skslsl")#anado
conjunto2={"slspd","fhfjg"}
conjunto.update(conjunto2)#anado otro conjunto
conjunto.remove("sssd")#elimino uno
conjunto.pop()#eelimino ultimo
conjunto3=conjunto.union(conjunto2)#union de conjuntos
"""
comentarios alrgos

"""


#@@@###$$$----------diccionario--------------@@@###$$$
dictnuevo={"narca":"bmw","modelo":"m3","fecha":2021,"colores":["verde","amarillo"]}
#{"algo":"valor","algo":["array","array1"]}
print(dictnuevo["modelo"])
print(dictnuevo.keys())#las claves
dictnuevo["modelo"]="m4"# un elemento cambio valor
dictnuevo.update({"puertas":3})#acutalizo anadiendo
dictnuevo.pop("narca")#borra un elemento
del dictnuevo["modelo"]

for x in dictnuevo.values():#imprimo los valores
    print(x)


for x in dictnuevo.keys():#imprimo las claves
    print(x)

for x,y in dictnuevo.items():#imprimo todo
    print(x,y)

dictotro=dictnuevo.copy()#copiar dict de 2 maneras
dictotro2=dict(dictnuevo)


familia={"hijo1":{"nombre":"chema","edad":23},"hijo2":{"nombre":"chema1","edad":22}}
hijo1={"nombre":"chema","edad":23}
hijo2={"nombre":"chem1","edad":25}

familia1={
    "primero":hijo1,
    "segundo":hijo2
}
#dictionario a partir de elementos

print(hijo1.get("nombre"))#obtener campo

print(type(personas))#obtener su tipo




#@@@###$$$----------elif--------------@@@###$$$
x=34
if x>44:
    print("grande")
elif x>23:#elif
    print("mediano")



#@@@###$$$----------if de una linea otro--------------@@@###$$$
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# si a>b imprimes a , si iguales =
if a>b and a>23:#and en letra
    print("muy grande")



#@@@###$$$----------while con break y continue--------------@@@###$$$
i=3
while i<6:
    print(i)
    if i==3:
        break#cuando sea 3 sal del bucle
    i+=1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue#cuando sea 3 salta a siguiente iteracion
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:#cuando acabe while
  print("i is no longer less than 6")



#@@@###$$$----------for--------------@@@###$$$
for x in "banana":
    print(x)

frutas=["sjsks","sss","ffff"]
for x in frutas:
    print(x)
    if x=="sss":
        break#si el que leo es sss sal del bucle


for x in frutas:
    
    if x=="sss":
        continue#lo siguiente no lo hagas
    print(x)

for x in range(4):
    print(x)


for x in range(6):# en el rango
  print(x)
else:
  print("Finally finished!")#cuando termines 


#@@@###$$$----------diferentes argumentos funciones--------------@@@###$$$
def functionotra(nom):
    print("hola "+nom)

functionotra("sdjsks")    


def my_function1(*kids):#si pasas varios elementos
  print("The youngest child is " + kids[2])

my_function1("Emil", "Tobias", "Linus")



def my_function2(child3, child2, child1):
  print("The youngest child is " + child3)
#pasar los elementos con nombre
my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function3(x):
  return 5 * x

print(my_function3(3))


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


print(personas)
personas.clear()#vaciar
x="hola"

def func():
    print("esto "+x)


func()

y="verde"

def func1():
    global y
    y="rojo"

func1()
print("color "+y)#variable global la cambio    



#@@@###$$$----------conversiones--------------@@@###$$$
tuplas=("hola","adios")

dict223={"chema":23,"javier":234}

num=int(20)
dict1=dict(name="jon",edad=23)#constructores
tupla1=tuple(("sssd","dd"))

numF=float(num)#conversiones
print(type(numF))

st=str(num)
print(type(st))#su tipo


#@@@###$$$----------operaciones strings--------------@@@###$$$
st1="shsajsjajdf"

print(st1[3:7])#entre 3 y 7
print(st1[:7])#hasta 7
print(st1[3:])# de 3 al final
print(st1[-3:-1])# de atras hacia adelante

print(st1.replace("j","W"))#cambio
print(st1.split("a"))#separo

st1=st1+"  "+st


#@@@###$$$----------imprimir otra forma--------------@@@###$$$
cant=3
item=234
precio=199
order="el prod {1} he pagado {2} y he comprado {0}"
print(order.format(cant,item,precio))#imprimir cada uno con formato

txt = "Hello \n World!"
print(txt) #imprimir salto linea

print(len(txt))

#imprimir
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))# se da nombre a cada atributo


#@@@###$$$----------try except--------------@@@###$$$
#try y except
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


#@@@###$$$----------type error--------------@@@###$$$
#raise excepcion
x = 1

if not type(x) is int:
  raise TypeError("Only integers are allowed")#lanza excepcion




#@@@###$$$----------lista coger con :--------------@@@###$$$
personas=["cero","uno","dos","tres","cuatro","cinco","seis"]
print(personas[2:5])#dos a cuatro
print(personas[:3])#cero a dos
print(personas[3:])#tres a seis
print(personas[-4:-1])#tres a cinco
#el primero si que lo coge, el ulitmo no

