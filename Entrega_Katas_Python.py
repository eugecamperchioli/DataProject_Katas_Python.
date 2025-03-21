# PROYECTO LÓGICA: Katas de Python
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_letras(cadena):
#creamos el diccionario para almacenar    
    letras = {}
    
    for let in cadena:
#tomamos solo letras que no son espacios
        if let != ' ':
#si la letra ya existe que sume +1            
            if let in letras:
                letras[let] += 1
#si no existe antes cuenta solo 1            
            else:
                letras[let] = 1 
        
    return letras

cadena = "hola, me llamo eugenia"
resultado = contar_letras(cadena)
print(resultado)

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def multiplicar_por_dos(i):
    return i * 2

lista_numeros = [2,4,6,8,10,12,14]
resultado_map = map(multiplicar_por_dos,lista_numeros)
resultado_map = list(resultado_map)
resultado_map

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def lista_palabras(lista_palabras,palabra_objetivo):

    resultado = []

    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            resultado.append(palabra)
            
    return resultado

palabras = ['patata', 'leche', 'cebolla', 'huevos', 'tortilla']
objetivo = 'la'
resultado = lista_palabras(palabras,objetivo)
resultado

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencia_valores(x,y):
    return x - y

valor_1 = [1,2,3,4]
valor_2 = [5,6,1,2]

resul_diferencia = map(diferencia_valores,valor_1,valor_2)
resul_diferencia = list(resul_diferencia)
resul_diferencia

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def evaluar_nota(numeros, valor=5):

    media = sum(numeros) / len(numeros)

    if media >= valor:
        estado = 'aprobado'

    else:
        estado = 'suspenso'

    return(media, estado)

notas = [2,3,4,7,8]
resultado = evaluar_nota(notas)
resultado

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
resultado_factorial = factorial(5)
resultado_factorial

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
lista_tupla = ('huevos', 'patata', 'cebolla')
type(lista_tupla)

def tupla_a_string(tupla):
    return str(tupla)

tupla_a_string = map(tupla_a_string, lista_tupla)
tupla_a_string = str(tupla_a_string)
type(tupla_a_string)

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
def dividir_numeros():
    
    try:
        num_1 = int(input('Introduce el primer numero: '))
        num_2 = int(input('Introduce el segundo numero: '))
        
        resultado = num_1 / num_2

    except ValueError:
        print("Error. Debes ingresar un numero valido")

    except ZeroDivisionError:
        print("Error. No puedes dividir por 0")
    else:
        print(f"la division fue exitosa, el resultado es: {resultado}")

dividir_numeros()

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def mascotas_prohibidas(mascotas):
    mascotas_prohibidas = ['mapache','tigre', 'serpiente piton', 'cocodrilo', 'oso']
    return mascotas not in mascotas_prohibidas

def mascotas_permitidas(mascotas):
    return list(filter(mascotas_prohibidas, mascotas))

mascotas = ['gato','perro','loro','mapache','tigre']
filtrar_mascotas = mascotas_permitidas(mascotas)
filtrar_mascotas

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
def numeros_y_promedios(n):

    if not n:
        print('la lista está vacia, ingrese un numero')

    else:
        promedio = sum(n) / len(n)
        return promedio
    
lista_numeros3 = []
lista_numeros4 = [30,22,56,43,20]
resultado_1 = numeros_y_promedios(lista_numeros3)
resultado_2 = numeros_y_promedios(lista_numeros4)
resultado_1
resultado_2

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def introducir_edad():

    try:
        edad = int(input('Por favor, introduzca su edad'))

        if edad < 0 or edad > 120:
            print('Error. La edad indicada supera el rango esperado')
        else:
            print(f'Tu edad es de {edad} años')
       
    
    except ValueError:
        print("Error. Debes ingresar un numero valido")

introducir_edad()

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_frase(x):

    palabras = x.split()

    longitudes = list(map(len,palabras))

    return longitudes

frase = 'El día está nublado'
frase_len = longitud_frase(frase)
frase_len

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def lista_tuplas(caracteres):
    # con el set eliminamos los duplicados
    caracteres_unicos = set(caracteres)

    tuplas = list(map(lambda letra : (letra.lower(), letra.upper()), caracteres_unicos))

    return tuplas

conjunto_caracteres = 'abcdefgh'
resultado_tupla = lista_tuplas(conjunto_caracteres)
resultado_tupla

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def retorno_palabras(letra,lista_palabras):

    return list(filter(lambda palabra : palabra.lower().startswith(letra),lista_palabras))

lista_palabras = ['arbol', 'tierra', 'viento', 'amigo', 'arena']
letra = 'a'
resultado = retorno_palabras(letra,lista_palabras)
resultado

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
numeros = [2,4,6]
suma_lambda = [(lambda x:x + 3) (x) for x in numeros]
print(suma_lambda)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def filtrar_cadena(n,cadena_texto):

    palabras = cadena_texto.split()

    resultado = list(filter(lambda x : len(x) > n, palabras))

    return resultado

cadena_texto = 'el dia esta muy nublado'
n = 4
resultado = filtrar_cadena(n,cadena_texto)
print(resultado)

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()
from functools import reduce

lista_digitos = (4,3,7,8)

resultado = reduce(lambda x,y : str(x) + str(y), lista_digitos)

print(resultado)

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
def extraer_estudiantes(estudiante):

    return estudiante['calificacion'] >= 90

dicc_estudiantes = [
    {'nombre': 'Ana', 'edad': 20, 'calificacion': 85},
    {'nombre': 'Juan', 'edad': 25, 'calificacion': 101},
    {'nombre': 'Maria', 'edad': 24, 'calificacion': 100},
    {'nombre': 'Lucas', 'edad': 20, 'calificacion': 90}
]

estudiantes_destacados = list(filter(extraer_estudiantes,dicc_estudiantes))
estudiantes_destacados

# 19. Crea una función lambda que filtre los números impares de una lista dada.
numeros = [2,4,6,1,3,7,9]
impares_lambda = [(lambda x : x % 2 != 0) (x) for x in numeros]
print(impares_lambda)

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
def filtrar_int(lista):
    
    resultado = list(filter(lambda x : type(x) == int,lista))

    return resultado

lista = ['hola', 23, 2021, 'cielo']
resultado = filtrar_int(lista)
resultado

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda
numero = [3]
cubo_lamba = [(lambda x:x ** 3) (x) for x in numero]
print(cubo_lamba)

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
from functools import reduce

lista_numerica = [1,2,3,5,6,7,8]

resultado = reduce(lambda x, y : x * y, lista_numerica)

print(resultado)

# 23. Concatena una lista de palabras.Usa la función reduce() .
from functools import reduce

lista_palabras2 = ['hola', 'mi','nombre','es','Eugenia']

resultado = reduce(lambda x,y : x + y, lista_palabras2)

resultado

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
from functools import reduce

lista_num = [300, 210, 230, 10]

resultado = reduce(lambda x,y : x - y, lista_num)

resultado

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
from functools import reduce

cadena_texto2 = 'Hola, como estas'

resultado = reduce(lambda x,y : len(cadena_texto2), cadena_texto2)

resultado

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
numeros2 = [10,2]
division_numeros = lambda x,y : x/y
resultado = division_numeros(numeros2[0], numeros2[1])
resultado

# 27. Crea una función que calcule el promedio de una lista de números.
def promedio_num(x):

    return sum(x) / len(x)

lista_numeros5 = [100,200,300,400]
resultado = promedio_num(lista_numeros5)
resultado

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def elemento_duplicado(lista):

    elementos_unicos = set()

    for elemento in lista:
        if elemento in elementos_unicos:
           return elemento 
        else:
            elementos_unicos.add(elemento)

lista = [1,1,3,4,5,3,4]
elemento_duplicado(lista)

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def variable_a_cadena(variable):
    
    caracter = str(variable)
# condicionamos a que la variable tenga mas de 4 numeros
    if len(caracter) <= 4:
            return caracter
#restamos 4 a la longitud de la cadena para que 6 veces multiplique # y por ultimo indexamos para que nos muestre los ultimos 4 numeros         
    enmascarado = '#' * (len(caracter) - 4) + caracter[-4:]
    
    return enmascarado

variable = '12345678910'
print(variable_a_cadena(variable))

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def palabras_anagramas(palabra_1,palabra_2):
# eliminamos los espacios de las palabras
    palabra_1 = palabra_1.replace(' ','')
    palabra_2 = palabra_2.replace(' ','')
# ordenamos las listas para que compare si son exactamente iguales
    return sorted(palabra_1) == sorted(palabra_2)
# solicitamos al usuario que ingrese la palabra
palabra_1 = input('ingresa la primera palabra:')
palabra_2 = input('ingresa la segunda palabra: ')
# llamamos a la funcion y si son anagramas que printee el mensaje
if palabras_anagramas(palabra_1,palabra_2):
    print(f'las palabras {palabra_1} & {palabra_2} son anagramas')
else:
    print(f'las palabras {palabra_1} & {palabra_2} no son anagramas')

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
# definimos la funcion 
def filtrar_nombres(lista_nombres,nombre_solicitado):

# que busque en la lista de nombres 
    for nombre in lista_nombres:
# si el nombre solicitado coincide con la lista de nombres nos printea la frase
        if nombre == nombre_solicitado:
            return(f'el nombre {nombre_solicitado} ha sido encontrado en la lista')
# se lo contrario imprime el error de que no encuentra el nombre
    return(f'error. el nombre {nombre_solicitado} no se encuentra en la lista')

nombre_solicitado = input('Por favor, ingresa el nombre a buscar.')
lista_nombres = ['Maria', 'Luis', 'Carlos', 'Rocio']
print(filtrar_nombres(lista_nombres, nombre_solicitado))

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
# definimos la funcion con los parametros nombre completo y lista de empleados
def filtrar_empleado(nombre_completo,lista_empleados):
# que busque en la lista de empleados
    for empleado in lista_empleados:
# si encuentra el nombre dado en la lista de empleados nos printea la frase que le indicamos
        if empleado['nombre'] == nombre_completo:
            return f"el empleado {nombre_completo} trabaja como {empleado['puesto']}"
# si no encuentra el nombre dado devuelve el mensaje indicando que la persona no trabaja en la empresa
    else:
        return f"el empleado {nombre_completo} no trabaja aqui"
    
empleados = [{'nombre' : 'Juan Perez', 'puesto': 'desarrollador'},
          {'nombre' : 'Maria', 'puesto': 'comercial'}]
print(filtrar_empleado('Juan Perez',empleados))
print(filtrar_empleado('Ana Gomez', empleados))

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# generamos las dos listas de numeros
lista_1 = [2,4,6,8,9,10]
lista_2 = [1,2,3,4,6,8]
# creamos la funcion lamda con map para indicar las dos variables y convertimos a lista para que nos muestre el resultado
fun_lambda = list(map(lambda x,y : x + y, lista_1, lista_2))
print(fun_lambda)

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

# definimos la clase
class Arbol:
# definimos el metodo constructor, 2 atributos: tronco y rama
    def __init__(self, tronco, ramas):
        self.tronco = tronco
        self.ramas = ramas

# método crecer_tronco para aumentar la longitud del tronco en una unidad.
    def crecer_tronco(self):
        self.tronco += 1

# método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    def nueva_rama(self):
        self.ramas.append(1)

# método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

# método quitar_rama para eliminar una rama en una posición específica.
    def quitar_rama(self,posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print('no hay ramas para eliminar')

# método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
    def info_arbol(self):
        return f'tronco: {self.tronco} unidades de longitud, ramas: {len(self.ramas)} de longitud y {sum(self.ramas)} de unidades'
    
# caso de uso 
# Crear un árbol.
mi_arbol = Arbol(1,[0])

# Hacer crecer el tronco del árbol una unidad.
mi_arbol.crecer_tronco()

# Añadir una nueva rama al árbol.
mi_arbol.nueva_rama()

# Hacer crecer todas las ramas del árbol una unidad.
mi_arbol.crecer_ramas()

# Añadir dos nuevas ramas al árbol.
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# Retirar la rama situada en la posición 2.
mi_arbol.quitar_rama(2)

# obtener información sobre el árbol.
print(mi_arbol.info_arbol())

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corrien
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".

class Usuario_Banco():
    def __init__(self,nombre, saldo, cuenta_corriente):
        self.nombre = nombre 
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self,monto):
        if monto <= 0:
            raise ValueError ('el monto debe ser positivo')
        if monto > self.saldo:
            raise ValueError ('no tienes suficiente dinero en la cuenta')
        self.saldo -= monto
        print(f'has retirado {monto} de tu cuenta. Tu saldo actual es de {self.saldo}')

    def transferir_dinero(self,monto,usuario_destino):
        if monto <= 0:
            raise ValueError ('el monto debe ser positivo')
        if monto > self.saldo:
            raise ValueError ('no tienes suficiente dinero en la cuenta')
            
        self.saldo -= monto
        usuario_destino.saldo += monto
        print(f'has transferido el monto de {monto} al usuario {usuario_destino.nombre}')
        print(f'tu saldo actual es de {self.saldo}')
        print(f'el saldo de {usuario_destino.nombre} es de {usuario_destino.saldo}')

    def agregar_dinero(self,monto):
        if monto <= 0:
            raise ValueError ('el monto debe ser positivo')    
        self.saldo += monto
        print(f'has acreditado el monto de {monto} a tu cuenta. saldo actual: {self.saldo}')

    def mostrar_info(self):
        print(f'usuario:{self.nombre}')
        print(f'saldo:{self.saldo}')
        print(f'cuenta corriente: {self.cuenta_corriente}')

usuario_1 = Usuario_Banco('Alicia', 100, True)
usuario_2 = Usuario_Banco('Bob', 50, True)

print('informacion de Alicia antes de las operaciones: ')
usuario_1.mostrar_info()
print('informacion de Bob antes de las operaciones: ')
usuario_2.mostrar_info()

# agregar 20 unidades de saldo de Bob
usuario_2.agregar_dinero(20)
# hacer una transferencia de 80 unidades de Bob a Alicia
usuario_2.transferir_dinero(80,usuario_1)
# retirar 50 unidades del saldo de Alicia
usuario_1.retirar_dinero(50)

print('informacion de Alicia despues de las operaciones: ')
usuario_1.mostrar_info()
print('informacion de Bob despues de las operaciones: ')
usuario_2.mostrar_info()

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    contador = {}
    palabras = texto.split()

    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador

def reemplazar_palabra(texto, palabra_orig,palabra_nueva):
    return texto.replace(palabra_orig,palabra_nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras_filtradas = []

    for p in palabras:
        if p != palabra:
            palabras_filtradas.append(p)
            
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion,*args):

    if opcion == 'contar':
        return contar_palabras(texto)
    elif opcion == 'reemplazar':
        if len(args) !=2 :
            raise ValueError('se deben proporcionar dos argumentos')
        palabra_orig,palabra_nueva = args
        return reemplazar_palabra(texto,palabra_orig,palabra_nueva)
    elif opcion == 'eliminar':
        if len(args) != 1:
            raise ValueError('se debe proporcionar un argumento para eliminar')
        palabra = args[0]
        return eliminar_palabra(texto,palabra)
    else:
        raise ValueError('la accion solicitada, no es una opcion valida')
    
texto = 'hola mundo, estoy feliz'
print('contar palabras:', procesar_texto(texto,'contar'))
print('reemplazar palabra:', procesar_texto(texto,'reemplazar','hola','Hello'))
print('eliminar palabra:', procesar_texto(texto,'eliminar','feliz'))

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
# DIA = 06:00 A 11:59
# TARDE = 12:00 A 19:00
# NOCHE = 19:01 A 5:59

def momento_dia(hora):
    if hora < 0 or hora >= 24:
        return('la hora es invalida')
    
    if hora > 6 and hora < 12:
        return('es de dia')
    elif hora > 12 and hora <= 19:
        return('es de tarde')
    else:
        return('es de noche')
    
hora_usuario = int(input('ingresa una hora de 0-23: '))
resultado_hora = momento_dia(hora_usuario)
print(resultado_hora)

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
#- 0 - 69 insuficiente
#- 70 - 79 bien
#- 80 - 89 muy bien
#- 90 - 100 excelente

def calificacion_alumno(nota):

    if nota < 0 or nota > 100:
        return('la hora es invalida. ingrese un numero del 0 al 100')
    
    if nota >= 0 and nota <= 69:
        return(f'la calificacion del alumno es {nota}, insuficiente')
    elif nota >= 70 and nota <= 79:
        return(f'la calificacion del alumno es {nota}, bien')
    elif nota >= 80 and nota <=89:
        return(f'la calificacion del alumno es {nota}, muy bien')
    else:
        return(f'la calificacion del alumno es {nota}, excelente')
    
nota_alumno = int(input('Porfavor ingrese la nota del usuario: '))
resultado_nota = calificacion_alumno(nota_alumno)
print(resultado_nota)

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math

def calcular_area(figura,datos):
    if figura == 'rectangulo':
        base, altura = datos
        return base * altura
    
    if figura == 'circulo':
        radio = datos
        return math.pi * radio**2
    
    if figura == 'triangulo':
        base,altura = datos
        return (base * altura) / 2
    
    else:
        print('la figurada solicitada no es valida')

print(calcular_area('rectangulo',(5,10)))
print(round(calcular_area('circulo',(5)),2))
print(calcular_area('triangulo',(5,10)))


# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
#1. Solicita al usuario que ingrese el precio original de un artículo.
#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

def monto_compra():
    precio_articulo = float(input('por favor, ingrese el precio del articulo'))
    cupon_descuento = input('cuenta con cupon de descuento? Responda con SI o NO')
    monto_final = precio_articulo
        
    if cupon_descuento == 'si':
        valor_cupon = int(input('ingrese el valor del cupon'))

        if valor_cupon > 0:
            monto_final = precio_articulo - valor_cupon
            print(f'se ha aplicado un descuento de {valor_cupon} EUR. el monto final es de {monto_final} EUR.')
        else:
            print('el valor del cupon debe ser mayor a 0')

    else:
        print(f'no se ha aplicado ningn descuento, el monto final es de {precio_articulo}')


#llamamos a la funcion:
monto_compra()