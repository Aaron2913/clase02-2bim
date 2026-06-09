import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Pais

Session = sessionmaker(bind=engine)
session = Session()

with open('../data/paises.csv', encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)

    for fila in lector:
        pais = Pais(
            id=int(fila[0]),
            nombre=fila[1],
            continente=fila[2]
        )

        session.add(pais)

session.commit()
session.close()

print("Países agregados correctamente")