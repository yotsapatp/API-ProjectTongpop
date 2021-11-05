from google.auth.credentials import Scoped
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
                username = request.args.get('username')
                action = request.args.get('action')
                nameId = request.args.get('nameId')
                categoryId = request.args.get('categoryId')  
                qty = request.args.get('qty')  
                lineId = request.args.get('lineId')  
            elif request_json and 'username' in request_json:
                username = request_json['username']
                action = request_json['action']
                nameId = request_json['nameId']
                categoryId = request_json['categoryId'] 
                qty = request_json['qty'] 
                lineId = request_json['lineId'] 
            else:
                return {"message": 'error', "username": "Not found !! "}

            user = check_user(username=username)
            if(user != False):
                if(action == 'products'):
                    contents = {
                        "type": "carousel",
                        "contents": mainProduct(user=user, categoryId=categoryId, nameId=nameId)
                    } 
                elif(action == 'productDetail'):
                    response = getProductDetail(user, nameId=nameId)
                    return response
                elif(action == 'productDetailTotal'):
                    response = getProductDetail_total(user, nameId=nameId,qty=qty)
                    return response  
                elif(action == 'productAdd'):
                    response = productAdd(user, lineId=lineId,nameId=nameId,qty=qty)
                    return response  
                elif(action == 'productDelete'):
                    response = productDelete(user, lineId=lineId,nameId=nameId)
                    return response  
                elif(action == 'productCart'):
                    response = productCart(user=user,lineId=lineId)
                    return response   
                elif(action == 'productCheckout'):
                    response = productCheckout(user=user,lineId=lineId)
                    return response   
                else:
                    contents = {
                        "type": "carousel",
                        "contents": mainCategory(user=user, nameId=nameId)
                    }

                jsonFlex = {"response_type": "object"}
                jsonFlex["line_payload"] = [
                    {
                        "type": "flex",
                        "altText": "ข้อมูล",
                        "contents": contents
                    }
                ]
                headers = {
                    'Response-Type': 'object'
                }
                return (jsonFlex, 200, headers)
            else:
                return {"message": 'error', "User": username + "Not found !! "}
        else:
            return {"message": 'error', "detail": "Work!!!"}

    except Exception as e:
        print(e)
        return {"message": 'error', "detail": str(e)}


def mainCategory(user, nameId=None):
    googleSheetId = user['googleSheetId']
    from libflex_pt import flexCategory, flexProduct, flexResult

    sheetName = 'category'

    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url)

    if nameId is not None:
        df = df.loc[df['name'] == str(nameId)]

    json_body = []
    if not df.empty:
        for index, row in df.iterrows():
            print(row['images'], row['name'])
            content = flexCategory(data=row)
            json_body.append(content)
    else:
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


def mainProduct(user, categoryId=None, nameId=None):
    googleSheetId = user['googleSheetId']
    from libflex_pt import flexCategory, flexProduct, flexResult 
    sheetName = 'products'
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url) 

    if nameId is not None:
        df = df.loc[df['name'] == str(nameId)]

    if categoryId is not None:
        df = df.loc[df['category'] == str(categoryId)]
    else:
        df = df.loc[df['category'] == 'ทะเลเผา']

    json_body = []

    if not df.empty:
        for index, row in df.iterrows():
            print(row['name'], row['images'], row['price'])
            content = flexProduct(data=row)
            json_body.append(content)
    else:
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


def getProductDetail_total(user, nameId=None,qty=1):
    googleSheetId = user['googleSheetId'] 
    sheetName = 'products'
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url)
    split_name = nameId.split(': ')

    try:
        products_name = split_name[1]
    except IndexError:
        products_name = split_name[0]

    if nameId is not None:
        df = df.loc[df['name'] == str(products_name)] 
    if not df.empty:
        # df.to_json(orient='split')
        df_json_string = df.to_json(orient='records')
        df_json = json.loads(df_json_string)
        res =  {
            'name' : df_json[0]['name'],
            'price' : df_json[0]['price'],
            'qty' : qty,
            'total' : int(df_json[0]['price'])*int(qty),
        } 
        return res
    else: 
        return False


def productAdd(user, lineId=None,nameId=None,qty=1):
    googleSheetId = user['googleSheetId'] 
    sheetName = 'products'
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url) 
    split_name = nameId.split(': ') 
    try:
        products_name = split_name[1]
    except IndexError:
        products_name = split_name[0]

    if nameId is not None:
        df = df.loc[df['name'] == str(products_name)] 
    if not df.empty:
        # df.to_json(orient='split')
        df_json_string = df.to_json(orient='records')
        df_json = json.loads(df_json_string)
        res =  {
            'lineId' : lineId,
            'name' : df_json[0]['name'],
            'price' : df_json[0]['price'],
            'qty' : qty,
            'total' : int(df_json[0]['price'])*int(qty),
        }  

        ### ทำ API ไปบันทึกที่ google sheets 
        r = requests.post(url_gas + '?action=addUser',json = res)
        if(r.status_code == 200):
             return  {"message": 'success'}
        else:
            return  {"message": 'error'} 
    else: 
        return False


def productDelete(user, lineId=None,nameId=None):
    googleSheetId = user['googleSheetId']
    from libflex_pt import flexCategory, flexProduct

    res =  {
            'lineId' : lineId,
            'name' : nameId
    }  

    ### ทำ API ไปบันทึกที่ google sheets 
    r = requests.post(url_gas + '?action=deleteUser',json = res)
    if(r.status_code == 200):
            return  {"message": 'success'}
    else:
        return  {"message": 'error'}  

def getProductDetail(user, nameId=None):
    googleSheetId = user['googleSheetId']
    from libflex_pt import flexCategory, flexProduct

    sheetName = 'products'
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url)

    df['price'] = df['price'].str.replace(',', '').astype(float)
    split_name = nameId.split(': ')

    try:
        products_name = split_name[1]
    except IndexError:
        products_name = split_name[0]

    if nameId is not None:
        df = df.loc[df['name'] == str(products_name)]

    if not df.empty:
        # df.to_json(orient='split')
        df_json_string = df.to_json(orient='records')
        df_json = json.loads(df_json_string)
        return df_json[0]
    else:
        return False


def mainProductDetail(user, nameId=None):
    df = getProductDetail(user, nameId=nameId)
    if df != False:
        return df
    else:
        return {"message": 'error', "detail": "ไม่พบข้อมูล"}


 
def test():
    nameId = 'เซต A'
    qty = 3
    user = check_user(username='pt')
    # res = mainProduct(user=user, categoryId='ทะเลเผา', nameId=None)
    # res = mainCategory(user, nameId=None)


    lineId = "tong"
    nameId = "กุ้งเผา"
    qty = 3 
    response = productAdd(user, lineId=lineId,nameId=nameId,qty=qty)
    print(response)


    # lineId = "tong"
    # nameId = "กุ้งเผา" 
    # response = productDelete(user, lineId=lineId,nameId=nameId)
    # print(response)


    lineId = "tong" 
    response = productCart(user, lineId)
    # print(response)
    print(json.dumps(response))


    # # contents = {
    #             "type": "carousel",
    #             # "contents": mainProduct(user=user, categoryId='ทะเลเผา', nameId=None)
    #             # "contents": mainCategory(user=user, nameId=None)
    #         }
    # res = getProductDetail_total(user=user,nameId=nameId,qty=qty) 
    # print(json.dumps(contents))


 

if __name__ == "__main__":
    test()
