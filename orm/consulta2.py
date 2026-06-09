from sqlalchemy.orm import Session
from modelo import engine, Serie

with Session(engine) as session:

    # Recorrer todas las series
    for serie in session.query(Serie).all():
        print(
            f"{serie.titulo} - "
            f"Promedio edad: {round(serie.obtener_edad_actore())} años "
            f"| Premios: {serie.obtener_total_premios()}"
        )