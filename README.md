## Problema: Filtrar los números pares de una lista.
### Solución Declarativa:
```
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)  
```
### Solución Imperativa

```
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)  
```

## Uso de la Función filter()
### Problema: Filtrar una lista de palabras para obtener solo aquellas que tienen más de 3 letras.

### Solución Declarativa:
```
palabras = ["gato", "perro", "ratón", "pez"]
palabras_largas = list(filter(lambda palabra: len(palabra) > 3, palabras))
print(palabras_largas)  # Salida: ['gato', 'perro', 'ratón']
```

### Solución Imperativa
```
palabras = ["gato", "perro", "ratón", "pez"]
palabras_largas = []

for palabra in palabras:
    if len(palabra) > 3:
        palabras_largas.append(palabra)

print(palabras_largas)  # Salida: ['gato', 'perro', 'ratón']
```

## Uso de map()
### Problema: Convertir todos los elementos de una lista a mayúsculas.
### Solución Declarativa:
```
palabras = ["hola", "mundo", "python", "es", "genial"]
palabras_mayus = list(map(str.upper, palabras))
print(palabras_mayus)
```
### Solución imperativa:
```
palabras = ["hola", "mundo", "python", "es", "genial"]
palabras_mayus = []

for palabra in palabras:
    palabras_mayus.append(palabra.upper())

print(palabras_mayus)  
```

## Uso de Expresiones Generadoras
### Problema: Calcular la suma de los cuadrados de los números pares de una lista.
### Solución Declarativa:
```
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_cuadrados_pares = sum(numero**2 for numero in numeros if numero % 2 == 0)
print(suma_cuadrados_pares)  # Salida: 220
```
### Solución imperativa

```
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_cuadrados_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        suma_cuadrados_pares += numero**2

print(suma_cuadrados_pares)  # Salida: 220
```

## Uso de Pandas para Manipulación de Datos
### Problema: Filtrar filas de un DataFrame donde una columna específica tiene valores mayores que un umbral.
### Solución Declarativa:
```
import pandas as pd

datos = {'Nombre': ['A', 'B', 'C', 'D'],
         'Puntuación': [10, 20, 15, 25]}

df = pd.DataFrame(datos)

df_filtrado = df[df['Puntuación'] > 15]
print(df_filtrado)
```

### Solución imperativa:
```
import pandas as pd

datos = {'Nombre': ['A', 'B', 'C', 'D'],
         'Puntuación': [10, 20, 15, 25]}

df = pd.DataFrame(datos)

# Inicializar una lista vacía para almacenar los índices de las filas que cumplen la condición
filas_a_incluir = []

# Iterar sobre el DataFrame usando la función `iterrows` para acceder a cada fila
for index, fila in df.iterrows():
    # Verificar si la condición se cumple
    if fila['Puntuación'] > 15:
        filas_a_incluir.append(index)

# Crear un nuevo DataFrame solo con las filas que cumplen la condición
df_filtrado = df.loc[filas_a_incluir]

print(df_filtrado)
```

## Uso de SQLAlchemy para Consultas a Bases de Datos
### Problema: Obtener todos los registros donde la edad es mayor de 30 años.
### Solución Declarativa:
```
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)

engine = create_engine('sqlite:///:memory:', echo=False)
Base.metadata.create_all(engine)

session = Session(engine)
session.add_all([Persona(nombre='Juan', edad=25), Persona(nombre='Ana', edad=35)])
session.commit()

consulta = select(Persona).where(Persona.edad > 30)
resultado = session.execute(consulta).scalars().all()

for persona in resultado:
    print(persona.nombre, persona.edad)  # Salida: Ana 35

```

### Solución Imperativa
```
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)

# Crear una base de datos en memoria
engine = create_engine('sqlite:///:memory:', echo=False)
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
session = Session(engine)

# Agregar registros a la base de datos
session.add_all([Persona(nombre='Juan', edad=25), Persona(nombre='Ana', edad=35)])
session.commit()

# Recuperar todos los registros de la tabla `personas`
resultados = session.query(Persona).all()

# Filtrar los registros manualmente
personas_mayores_de_30 = []

for persona in resultados:
    if persona.edad > 30:
        personas_mayores_de_30.append(persona)

# Mostrar los resultados
for persona in personas_mayores_de_30:
    print(persona.nombre, persona.edad)  # Salida: Ana 35

# Cerrar la sesión
session.close()
```
