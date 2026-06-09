import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Actor, Pais, Serie

Session = sessionmaker(bind=engine)
session = Session()

with open('../data/actores.csv', encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)

    for fila in lector:
        pais = session.query(Pais).filter_by(nombre=fila[3]).first()
        serie = session.query(Serie).filter_by(titulo=fila[4]).first()

        actor = Actor(
            id=int(fila[0]),
            nombre=fila[1],
            edad=int(fila[2]),
            pais=pais,
            serie=serie
        )

        session.add(actor)

session.commit()
session.close()

print("Actores agregados correctamente")