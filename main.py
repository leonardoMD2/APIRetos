from fastapi import FastAPI
from fastapi.responses import JSONResponse
from configs.sqlalchemy_configs import Session, Base, engine
from database.database import Retos, RetosEntregados
from datetime import datetime, timedelta
from utils.utils import  get_difficulty, get_random_challenge,guardar_entrega

import retos as retostxt

Base.metadata.create_all(engine)
app = FastAPI()

@app.get('/')
def bienvenida():
    db = Session()
    res = db.query(Retos).all()
    return res

@app.get('/nuevoreto')
def entrega_reto():
    intervalo_semanal = timedelta(days=7)
    db = Session()
    #obtenemos el último reto
    ultimo_reto = db.query(RetosEntregados).order_by(RetosEntregados.fecha_entrega.desc()).first()
    
    if ultimo_reto is None or datetime.now() - datetime.strptime(ultimo_reto.fecha_entrega,'%Y-%m-%d %H:%M:%S.%f') >= intervalo_semanal:
      dificultad = get_difficulty(datetime.now().month)
      reto = get_random_challenge(dificultad)
      guardar_entrega(reto)
      return JSONResponse(content={'Reto':reto.reto, 'dificultad':reto.dificultad})
    else:
        reto_entregado = db.query(RetosEntregados).order_by(RetosEntregados.id.desc()).first()
        reto = db.query(Retos).filter(Retos.id==reto_entregado.id).first()
        return JSONResponse(content={'Reto':reto.reto, 'dificultad':reto.dificultad})


'''db = Session()
for item in retostxt.cantidadRetos:
    reto = Retos(reto=item['reto'],dificultad=item['dificultad'])
    try:
        db.add(reto)
        db.commit()
    except Exception as e:
        print(e)'''