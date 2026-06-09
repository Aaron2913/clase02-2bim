import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie, Plataforma, Pais

Session = sessionmaker(bind=engine)
session = Session()

with open('../data/series.csv', encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)

    for fila in lector:
        plataforma = session.query(Plataforma).filter_by(nombre=fila[5]).first()
        pais = session.query(Pais).filter_by(nombre=fila[6]).first()

        serie = Serie(
            id=int(fila[0]),
            titulo=fila[1],
            genero=fila[2],
            anio_estreno=int(fila[3]),
            temporadas=int(fila[4]),
            plataforma=plataforma,
            pais=pais
        )

        session.add(serie)

session.commit()
session.close()

print("Series agregadas correctamente")