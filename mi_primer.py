print("Hola mundo")
print(2-1)

# Python como calculadora
print(7 + 5)     # suma
print(7 * 5)     # multiplicación
print(7 / 5)     # división (siempre devuelve decimal)
print(7 ** 2)    # potencia: 7 al cuadrado

# Variables: nombres que guardan valores
matriculados = 25
aprobados = 21
tasa_aprobacion = aprobados / matriculados

print("Tasa de aprobación:", tasa_aprobacion)
print(f"Número de matriculados: {matriculados}")

# Ejercicio 2.1
pib_ec = 120_000_000_000
poblacion_ec = 18_000_000

# print(f"PIB per capita:", {(pib_ec / poblacion_ec):,.2f}) --> esto es un error de syntax
print(f"PIB per capita: {(pib_ec / poblacion_ec):,.2f}") # Todo dentro del mismo f"xyz". Al separar por una coma, trata el resultado como un objeto aparte.

## TEORIA DE CONJUNTOS ##

#Un conjunto se define con llaves
A = {1, 2, 3, 4}
print("A=", A)
print("Cardinalidad=", len(A)) 

#Pertinencia: el operador "in" devuelve "True" o "False"
print("¿2 ∈ A?", 2 in A)
print("¿7 ∈ A?", 7 in A)
print("¿7 ∉ A?", 7 not in A)

#Propiedad: los duplicados se eliminan solos
votos = {"Ana" , "Luis" , "Ana" , "Maria" , "Luis"}
print("Personas que votaron:", votos) 
print("Numero de votantes:", len(votos))

#Propiedad: un conjunto NO tiene orden interno. "sorted()" devuelve una lista ordenada
print("Pres. ordenada:", sorted(votos))

#"set()" crea un conjunto vacio
vacio = set()
print("Conjunto vacio:", vacio, "| cardinalidad", len(vacio))

#Ejercicio 3.1

paises_visitados = {"Colombia" , "EEUU" , "Espana" , "Mexico" , "Chile" , "Belgica"}

#Imprime el conjunto de paises visitados. Imprime su cardinalidad. Verifica con "in" si Ecuador pertenece
print("Paises visitados:", paises_visitados)
print("Cardinalidad pv:", len(paises_visitados))
print("¿Ecuador esta en paises visitados?", "Ecuador" in paises_visitados)

## OPERACIONES ENTRE CONJUNTOS: union, interseccion, diferencia, dif.simetrica y subconjunto
#Los conectores se pueden buscar en ASCII Character

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

print("A ∪ B =", A | B)      #union: elementos en A o en B (o en ambos)
print("A ∩ B =", A & B)      #interseccion: elementos en A y en B que se repiten
print("A \\ B =", A - B)     #diferencia: elementos en A pero no en B
print("B \\ A =", B - A)     #la diferencia no es conmutativa!!
print("A △ B =", A ^ B)      #dif.simetrica: en uno u otro, pero no en ambos

#Contencion
print("{1, 2} ⊆ A?", {1, 2} <= A)       # "<=" 1 y 2 son subconjunto de A --> True
print("A ⊆ B?", A <= B)

#Ejercicio 4.2 
# Conjunto de paises andinos (cordillera) y conjunto de paises amazonicos (miembros OTCA)
andinos = {"Venezuela", "Colombia", "Ecuador", "Perú", "Bolivia", "Chile", "Argentina"}
amazonicos = {"Brasil", "Bolivia", "Colombia", "Ecuador", "Guyana", "Perú", "Surinam", "Venezuela"}

print("Andinos y amazónicos a la vez:", sorted(andinos & amazonicos))       #Paises andinos y amazonicos a la vez, "sorted()" para ordenarlos alfabeticamente
print("Andinos que no son amazónicos:", sorted(andinos - amazonicos))       #Andinos no amazonicos
print("Amazónicos que no son andinos:", sorted(amazonicos - andinos))       #Amazonicos no andinos
print("Total de países mencionados:", len(andinos | amazonicos))            #Total paises andinos y amazonicos

# M es el grupo de estudiantes aprobados Mate y E, Estadistica
M = {"Ana", "Luis", "María", "Pedro", "Sofía"}
E = {"Luis", "Carmen", "Sofía", "Jorge"}

#Quienes aprobaron ambos cursos?
print("Est. aprobados ambos cursos:", M & E)
#Quienes aprobaron solo matematicas
print("Est. aprobados mate:", M - E)
#Quienes aprobaron al menos una materia
print("Numero de Est. aprobados al menos una materia:", len(M | E))
#Quienes aprobaron exactamente una materia
print("Est. aprobados exactamente una materia:", M ^ E)

## PRODUCTO CARTESIANO ##

A = {1, 2, 3}
B = {"do", "re"}

# Producto cartesiano por comprensión
AxB = {(a, b) for a in A for b in B}        #El conjunto de las parejas (a,b), para cada a en A y cada b en B

print("A × B =", sorted(AxB))
print("|A| =", len(A), " |B| =", len(B), " |A × B| =", len(AxB))    # len - cardinalidad 
print("¿Se cumple |A × B| == |A| · |B|?", len(AxB) == len(A) * len(B))

# La Conmutatividad entre conjuntos
from itertools import product       #Product calcula el producto cartesiano entre 2 o mas combinaciones

BxA = set(product(B,A))             #Genera un conjunto (set()) de todas las tuplas entre B y A
print("B x A =", sorted(BxA))       
print("A x B == B x A?", AxB == BxA)    #False: el producto cartesiano no es conmutativo

# Grafico
import matplotlib.pyplot as plt     #matplotlib es la biblio para graficos

A = {1, 2, 3}
B = {1, 2}
AxB = {(a, b) for a in A for b in B}        #Doble bluque para crear la tupla (a, b) y se agrega al set AxB
                                            #Hace lo mismo que "set(product(A, B)) usando itertools. Se usa sintaxis de Python

xs = [par[0] for par in AxB]                #Coord. Horizontales, par[0] accede al primer elemento de la tupla (indice 0)
ys = [par[1] for par in AxB]                #Coord. Verticales, par[1] accede al segundo elemento de la tupla (indice 1)

plt.figure(figsize=(5, 3.2))                    #Tamanio del graph: ancho x alto, en pulgadas
plt.scatter(xs, ys, s=80, color="darkblue")     #Scatter -> grafico de dispersion: s=80 es el tamanio de cada punto azul (darkblue)
plt.title("A × B con A = {1, 2, 3} y B = {1, 2}") #Titulos del grafico
plt.xlabel("A (primera coordenada)")    
plt.ylabel("B (segunda coordenada)")
plt.xticks([1, 2, 3])                       #Fuerzas a que las marcas de X sean exacto los elem. de A
plt.yticks([1, 2])
plt.grid(True, linestyle=":")               #Cuadrícula de fondo, con líneas punteadas (:)
plt.show()

# Ejercicio 5.1: Diseno muestral de una encuesta

sexo = {"Hombre", "Mujer"}
region = {"Costa", "Sierra", "Amazonia", "Insular"}

#Numero de perfiles muestrales 
perfiles = set(product(sexo, region))
print("Total perf. muestrales:", len(perfiles))
#Conjunto perfiles muestrales = sexo x region 
print("Perfiles =", sorted(perfiles))     

# Ejercicio 5.2 

A = {0, 1, 2}

#Cardinalidad de A
A2 = set(product(A,A))
print("Total AxA=", len(A2))
plt.figure(figsize=(5, 3.2))                    
plt.scatter(xs, ys, s=80, color="darkblue")     
plt.title("A × A con A = {0, 1, 2}") 
plt.xlabel("A (primera coordenada)")    
plt.ylabel("A (segunda coordenada)")
plt.xticks([0, 1, 2])                       
plt.yticks([0, 1, 2])
plt.grid(True, linestyle=":")               
plt.show()

AxA = {(a, b) for a in A for b in A}
xs = [par[0] for par in AxA]
ys = [par[1] for par in AxA]

plt.figure(figsize=(4, 4))
plt.scatter(xs, ys, s=90, color="darkred")
plt.title("A × A con A = {0, 1, 2}")
plt.xticks([0, 1, 2])
plt.yticks([0, 1, 2])
plt.grid(True, linestyle=":")
plt.show()