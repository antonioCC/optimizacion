#programa 1: global
nombre()
nombre2()
def nombre():
  nom="Adolfo" #variable local   
  print(nom*2)  

def nombre2():
  nom="Adolfo" #variable local   
  print(nom*4) 

#optimizado
nom="adolfo"#variable global
nombre()
nombre2()
def nombre():   
  print(nom*2)  

def nombre2():   
  print(nom*4) 

#---------------------------
 #programa 2: ciclos
n="abcd"
z=""
for b in n:
  z=z+b
  print(z)


#optimizado
n="abcd"
z=""
for b in n:
  print(z+=b)

#----------------------------
# programa 3: mirilla
var=saludo()
var2=saludo()
var3=saludo()
print(var+var2+var3)

def saludo():
  return "hola"


#optimizado
var=saludo()
print(var*3)

def saludo():
  return "hola"
        
#------------------
#programa 4:global

print("cuenta letras de palabras")
print("---------------------------------")
var=input("Ingresar algo:")
print("")
print("Cantidad de letras:")
print(len(var))
print("---------------------------------")

#optimizado
var=input("Ingresar algo")
print("Cantidad de letras:")
print(len(var))


#------------------
#programa 5:local

def sum():
  print ("Ingresa un primer valor:")
  N1 = int (input(""))
  print ("************************")
  print ("Ingresa un segundo valor:")
  N2 = int (input(""))
  suma=0 
  suma=N1+N2
  print ("Suma de Valores ingresados:")
  print (suma)


# optimizado
def sum(n1,n2):
  return n1+n2

#---------------------
#programa 6:global

var = 2
def fun(var):
    var2 = var
    print(var2)
f()  


#optimizado
var = 2
print(var)
 
 #---------------------
#programa 7: ciclo
a=1
while (a <= 10):
    print(a)
    a = a + 1


# optimizado
a=1
while (a<=10):
    print(a)
    a++

#----------------
#programa 8: mirilla
a=2
if(a%2==0):
  print("el")
  print("numero")
  print("es par")
else:
  print("el")
  print("numero")
  print("es impar")


a=2 
if (a%2==0):
  print("par")
else:
  print("impar")

#----------------------------------
#programa 9:global
print("edades")
edad1=20
print(edad1)
edad2=30
print(edad2)
edad3=25
print(edad3)
edad4=40
print(edad4)

#optimizado
lista=[20,30,25,40]
print(lista)

#-----------------------------------
#programa 10: global
var = 'que haces' 
print(var)

#optimizado
print("que haces")
  
