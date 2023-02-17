from sqlalchemy import func
import random
from datetime import datetime
from database.database import Retos, RetosEntregados
from configs.sqlalchemy_configs import Session

def random_reto_dif(dificultad):
    db = Session()
    id_max = db.query(func.max(Retos.id)).filter(Retos.dificultad == dificultad).scalar()
    while True:
        rand_id = random.randint(1, id_max)
        res = db.query(Retos).filter(Retos.id == rand_id, Retos.dificultad == dificultad).first()
        if res is not None:
            return res

def get_difficulty(month):
    if month < 6:
        return 'baja'
    elif month >= 6 and month <= 10:
        return 'media'
    else:
        return 'alta'
        
def get_random_challenge(difficulty):
    return random_reto_dif(difficulty)
        
def guardar_entrega(reto):
    db = Session()
    nueva_entrega = RetosEntregados(reto_id=reto.id, fecha_entrega=datetime.now())
    db.add(nueva_entrega)
    db.commit()