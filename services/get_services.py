#servicios GET

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from database.database import Retos, RetosEntregados
from datetime import datetime, timedelta
from utils.utils import get_difficulty, random_reto_dif,guardar_entrega


class RetoGetServices():
    def __init__(self, db) -> None:
        self.db = db

    def get_new_reto(self):
        intervalo_semanal = timedelta(days=7)
        ultimo_reto = self.db.query(RetosEntregados).order_by(RetosEntregados.fecha_entrega.desc()).first()
        if ultimo_reto is None or datetime.now() - datetime.strptime(ultimo_reto.fecha_entrega,'%Y-%m-%d %H:%M:%S.%f') >= intervalo_semanal:
            dificultad = get_difficulty(datetime.now().month)
            reto = random_reto_dif(dificultad)
            guardar_entrega(reto)
            return JSONResponse(content={'Reto':reto.reto, 'dificultad':reto.dificultad})
        else:
            reto_entregado = self.db.query(RetosEntregados).order_by(RetosEntregados.id.desc()).first()
            reto = self.db.query(Retos).filter(Retos.id==reto_entregado.id).first()
            return JSONResponse(content={'Reto':reto.reto, 'dificultad':reto.dificultad})