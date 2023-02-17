from fastapi import FastAPI
from configs.sqlalchemy_configs import Base, engine
from routers.routers_get import router_get


Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(router_get)