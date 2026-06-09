import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Plataforma, Pais

Session = sessionmaker(bind=engine)
session = Session()

with open('../data/plataformas.csv', encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)

    for fila in lector:
        pais = session.query(Pais).filter_by(nombre=fila[2]).first()

        plataforma = Plataforma(
            id=int(fila[0]),
            nombre=fila[1],
            pais=pais,
            suscriptores_millones=int(float(fila[3]))
        )

        session.add(plataforma)

session.commit()
session.close()

print("Plataformas agregadas correctamente")