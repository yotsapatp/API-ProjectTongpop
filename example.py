import requests
import json
import pandas as pd
import datetime as datetime
from datetime import date, timedelta

url_gas = "https://script.google.com/macros/s/AKfycbzwb1QwcuN_9xFx70VVNGl1ff657jwBFCv1G45cWxeuDQ7kkvx_c4y_KGwSvR4JcT3lhw/exec"

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

def main(request=None):
    try:
        if(request != None):
            request_json = request.get_json()
            if request.args and 'username' in request.args: 
                username   = username=request.args.get('username')
                action     = request.args.get('action')
                nameId     = request.args.get('nameId')
                categoryId = request.args.get('categoryId')
                imageurl   = request.args.get('imageurl') 
            elif request_json and 'username' in request_json:
                username   = request_json['username']
                action     = request_json['action']
                nameId     = request_json['nameId']
                categoryId = request_json['categoryId']
                imageurl   = request_json['imageurl'] 
            else:
                return {"message": 'error', "username": "Not found !! "} 

            user = check_user(username=username)
            if(user != False):
                productCart(user=user,lineId=nameId)
            else:   
                return {"message": 'error', "User": "Not found !! "}

                
        else:
            return {"message": 'error', "detail": "Work!!!"}

    except Exception as e:
        print(e)
        return {"message": 'error', "detail": str(e)}


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
