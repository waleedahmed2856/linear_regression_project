from fastapi import FastAPI
from pydantic import BaseModel
from parameters import load_artifacts, get_estimated_price, load_locations

app = FastAPI()

load_artifacts()
class HomeData(BaseModel):
    location: str
    area_sf: float
    bhk: int
    bath: int
@app.get("/get_location_names")
def get_location_names():
    return {"locations": load_locations()}

@app.post("/predict_home_price")
def predict_home_price(data: HomeData):
    estimated_price = get_estimated_price(
        data.location,
        data.area_sf,
        data.bhk,
        data.bath
    )
    return {"estimated_price": estimated_price}