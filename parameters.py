import pandas as pd 
import json
import numpy as np
import pickle

model = None
data_columns = None
locations = None 

def load_artifacts():

    global model, data_columns, locations

    with open("C:/Users/user/Desktop/bengluruhousing/columns.json", "r") as file:
        data_columns = json.load(file)["data_columns"]
        locations = data_columns[3:]

    with open("C:/Users/user/Desktop/bengluruhousing/model.pkl","rb") as f:
        model = pickle.load(f)
    
def load_locations():
    return locations

location = locations

def get_estimated_price(location, area_sf, bhk, bath):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(data_columns))
    x[0] = area_sf
    x[1] = bath
    x[2] = bhk
    if loc_index >=0:
        x[loc_index] = 1
    
    return round(model.predict([x])[0],2)    

if __name__==("__main__"):

    load_artifacts()
    print(locations)
    # print(load_columns())
    # predict_price = get_estimated_price('6th phase jp nagar', 2000, 8, 4)

    # print(f"The predicted price is: {predict_price}")
