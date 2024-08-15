#Problema: Filtrar los números pares de una lista.
#Solución Declarativa:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)  # Salida: [2, 4, 6, 8, 10]

#Uso de la Función filter()
#Problema: Filtrar una lista de palabras para obtener solo aquellas que tienen más de 3 letras.
#Solución Declarativa:

palabras = ["gato", "perro", "ratón", "pez"]
palabras_largas = list(filter(lambda palabra: len(palabra) > 3, palabras))
print(palabras_largas)  # Salida: ['gato', 'perro', 'ratón']

#Uso de map()
#Problema: Convertir todos los elementos de una lista a mayúsculas.
#Solución Declarativa:
palabras = ["hola", "mundo", "python", "es", "genial"]
palabras_mayus = list(map(str.upper, palabras))
print(palabras_mayus)

#Uso de Expresiones Generadoras
#Problema: Calcular la suma de los cuadrados de los números pares de una lista.
#Solución Declarativa:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_cuadrados_pares = sum(numero**2 for numero in numeros if numero % 2 == 0)
print(suma_cuadrados_pares)  # Salida: 220

#Uso de Pandas para Manipulación de Datos
#Problema: Filtrar filas de un DataFrame donde una columna específica tiene valores mayores que un umbral.
#Solución Declarativa:
import pandas as pd

datos = {'Nombre': ['A', 'B', 'C', 'D'],
         'Puntuación': [10, 20, 15, 25]}

df = pd.DataFrame(datos)

df_filtrado = df[df['Puntuación'] > 15]
print(df_filtrado)

#Uso de SQLAlchemy para Consultas a Bases de Datos
#Problema: Obtener todos los registros donde la edad es mayor de 30 años.
#Solución Declarativa:
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

