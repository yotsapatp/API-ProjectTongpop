 
from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from fastapi.param_functions import Body
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.openapi.utils import get_openapi 

from passlib.context import CryptContext
from pydantic import BaseModel, Field

import numpy as np
import pandas as pd
import requests
import json
from google.cloud import storage
from google.oauth2 import service_account
import pandas_gbq
# from pandas_gbq import schema
import datetime as datetime
from datetime import date, timedelta
import random

SECRET_KEY = "21bb28cfdac986bd041470db0ef8cbe32ecf18cfcea96163c6fc37f5ec6e4f89"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

url_gas = "https://script.google.com/macros/s/AKfycbzwb1QwcuN_9xFx70VVNGl1ff657jwBFCv1G45cWxeuDQ7kkvx_c4y_KGwSvR4JcT3lhw/exec"

app = FastAPI() 
  
class productCart_request(BaseModel):
    user: str
    lineId: str 



def check_user(username=None):
    db = {
        "pt": {
            "googleSheetId": "1ZCL0TGz-6eqzGb9Ix29N1ZpRKLgqVxClKW9i-kfJA3g", 
        } 
    }
    if username in db:
        user_dict = db[username]
        return user_dict
    else:
        return False

@app.post("/checkout")
async def productCheckout(data : productCart_request ): 
    user = check_user(username=data.user)
    if(user != False):
        try: 
            response =  productCheckout(user,data.lineId)
            return response
        except ValueError as e:
            return {
                'error_code':  str(e),
            }
    else:
        return {"message": 'error', "User": data.user + "Not found !! "}

@app.post("/productCart")
async def productCart(data : productCart_request ): 
    user = check_user(username=data.user)
    if(user != False):
        try: 
            response =  productCart(user,data.lineId)
            return response
        except ValueError as e:
            return {
                'error_code':  str(e),
            }
    else:
        return {"message": 'error', "User": data.user + "Not found !! "}


def productCheckout(user, lineId):
    today = date.today()
    today = today.strftime("%Y-%m-%d")
    googleSheetId = user['googleSheetId'] 
    sheetName = 'orders'
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url)  

    if lineId is not None:
        df = df.loc[df['lineId'] == str(lineId)]  

    from libflex_pt import flexCart, flexCart_product 
        
    if not df.empty:
        detail = []
        data = {}
        total = 0
        items = 0
        json_body = []
        for index, row in df.iterrows():
            content_product = flexCart_product(data=row)
            detail.append(content_product)
            total += row['price']
            items += int(row['qty'])
        data['total'] = total
        data['items'] = items
        data['date'] = today
        data['lineId'] = lineId
        content = flexCart(data=data, detail=detail)
        json_body.append(content)
    else:
        json_body = []
        content = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": "ไม่พบการค้นหา",
                        "wrap": True,
                        "weight": "bold",
                        "gravity": "center",
                        "size": "xl"
                    }
                ]
            }
        }
        json_body.append(content)
    return json_body


        

def productCart(user, lineId):
    today = date.today()
    today = today.strftime("%Y-%m-%d")
    googleSheetId = user['googleSheetId'] 
    sheetName = 'orders'
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url)  

    if lineId is not None:
        df = df.loc[df['lineId'] == str(lineId)]  

    from libflex_pt import flexCart, flexCart_product_whitdel 

    res =  {
        'lineId' : lineId
    }   
    r = requests.post(url_gas + '?action=lineId',json = res)
    if(r.status_code != 200): 
        return  {"message": 'error'}  

    if not df.empty:
        detail = []
        data = {}
        total = 0
        items = 0
        json_body = []
        for index, row in df.iterrows():
            content_product = flexCart_product_whitdel(data=row)
            detail.append(content_product)
            total += row['total']
            items += int(row['qty'])
        data['total'] = total
        data['items'] = items
        data['date'] = today
        data['lineId'] = lineId
        content = flexCart(data=data, detail=detail)
        json_body.append(content)
    else:
        json_body = []
        content = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": "ไม่พบการค้นหา",
                        "wrap": True,
                        "weight": "bold",
                        "gravity": "center",
                        "size": "xl"
                    }
                ]
            }
        }
        json_body.append(content)
    return json_body
