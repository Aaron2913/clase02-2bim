import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Premio, Serie

Session = sessionmaker(bind=engine)
session = Session()

with open('../data/premios.csv', encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)

    for fila in lector:
        serie = session.query(Serie).filter_by(titulo=fila[4]).first()

        premio = Premio(
            id=int(fila[0]),
            nombre_premio=fila[1],
            categoria=fila[2],
            anio=int(fila[3]),
            serie=serie
        )

        session.add(premio)

session.commit()
session.close()

print("Premios agregados correctamente")