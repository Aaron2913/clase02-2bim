from sqlalchemy.orm import Session
from modelo import engine, Serie

with Session(engine) as session:

    for serie in session.query(Serie).all():
        print(f"{serie.titulo} - {serie.obtener_edad_actore()} años")
