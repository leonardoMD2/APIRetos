from fastapi import FastAPI
from fastapi.responses import JSONResponse
from configs.sqlalchemy_configs import Session, Base, engine
from database.database import Retos, RetosEntregados
from datetime import datetime, timedelta
from utils.utils import  get_difficulty, random_reto_dif,guardar_entrega

Base.metadata.create_all(engine)
app = FastAPI()

@app.get('/')
def bienvenida():
    return JSONResponse(status_code=200, content={'mensaje':'Bienvenido a la API de retos de Programación I'})

@app.get('/nuevoreto')
def entrega_reto():
    intervalo_semanal = timedelta(days=7)
    db = Session()
    #obtenemos el último reto
    ultimo_reto = db.query(RetosEntregados).order_by(RetosEntregados.fecha_entrega.desc()).first()
    if ultimo_reto is None or datetime.now() - datetime.strptime(ultimo_reto.fecha_entrega,'%Y-%m-%d %H:%M:%S.%f') >= intervalo_semanal:
      dificultad = get_difficulty(datetime.now().month)
      reto = random_reto_dif(dificultad)
      guardar_entrega(reto)
      return JSONResponse(content={'Reto':reto.reto, 'dificultad':reto.dificultad})
    else:
        reto_entregado = db.query(RetosEntregados).order_by(RetosEntregados.id.desc()).first()
        reto = db.query(Retos).filter(Retos.id==reto_entregado.id).first()
        return JSONResponse(content={'Reto':reto.reto, 'dificultad':reto.dificultad})