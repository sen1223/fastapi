from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None

@app.get("/")
def hello_world():
    return {'hello': 'world'}


@app.put('/city/{city}')
def resutl(city: str, city_info: CityInfo):
    return {'city': city, 'country': city_info.country, 'province': city_info.province,
    'is_affectived': city_info.is_affected}

# uvicorn hello_world:app --reload