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

