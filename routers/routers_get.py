#routers
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.get_services import RetoGetServices
from configs.sqlalchemy_configs import Session

router_get = APIRouter()

@router_get.get('/')
def bienvenida():
    return JSONResponse(status_code=200, content={'mensaje':'Bienvenido a la API de retos de Programación I'})

@router_get.get('/nuevoreto')
def entrega_reto():
    db = Session()
    res = RetoGetServices(db).get_new_reto()
    return res