from enum import Enum
from typing import Optional, List
from fastapi import APIRouter, Path, Query
from pydantic import BaseModel, Field

app03 = APIRouter()

@app03.get("/path/parameters")
def path_params01():
    return {"message": "This is a message"}

@app03.get("/path/{parameters}")
def path_parames01(parameters: str):
    return {"message": parameters}

class CityName(str, Enum):
    Beijing = "Beijing"
    Shanghai = "Shanghai"

@app03.get("/enum/{city}")
async def latest(city: CityName):
    if city == CityName.Shanghai:
        return {"city_name": city, "confirmed": 1212, "death": 10}
    if city == CityName.Beijing:
        return {"city_name": city, "confirmed": 890, "death": 3}
    return {"city_name": city, "lastest": "unknow"}

@app03.get("/files/{file_path:path}")
def filepath(file_path: str):
    return f"The file path is {file_path}"

@app03.get("/path_/{num}")
def num(
    num: int = Path(..., ge=1, le=9, title="Your number")):
    return num

@app03.get("/query")
def page_limit(page: int = 1, limit: Optional[int] = None):
    if limit:
        return {"page": page, "limit": limit}
    return {"page": page}

@app03.get("/query/bool/conversion")
def type_conversion(param: bool = False):
    return {param}

@app03.get("/query/validations")
def query_params_validate(
    values1: str = Query(..., alias="alias_name", max_length=9, regex="^a"),
    values2: List[str] = Query(default=["v1", "v2"])
):
    return values1, values2

class CityInfo(BaseModel):
    name: str = Field(..., example="Beijing")
    country: str
    country_code: str = None
    courntry_populution: int = Field(default=800, ge=800, title="Number of populution",
     description="Number of populution about a country")

    class Config:
       schema_extra = {
           "example": {
               "name": "Shanghai",
               "country": "China",
               "country_code": "CN",
               "country_populution": 14000000
           }
       }

@app03.post("/reqest_body/city")
def city_info(city: CityInfo):
    print(city.name, city.country)
    return city.dict()

# test
