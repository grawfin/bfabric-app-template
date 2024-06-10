
import requests
import json
import datetime
import bfabric
from dash import html
import dash_bootstrap_components as dbc

VALIDATION_URL = "https://fgcz-bfabric.uzh.ch/bfabric/rest/token/validate?token="
HOST = "fgcz-bfabric.uzh.ch"

def token_to_data(token): 

    if not token:
        return None

    validation_url = VALIDATION_URL + token
    res = requests.get(validation_url, headers={"Host": HOST})
    
    if res.status_code != 200:
        res = requests.get(validation_url)
    
        if res.status_code != 200:
            return None
    try:
        master_data = json.loads(res.text)
    except:
        return None
    
    if True: 

        userinfo = json.loads(res.text)

        expiry_time = userinfo['expiryDateTime']
        current_time = datetime.datetime.now()
        five_minutes_later = current_time + datetime.timedelta(minutes=5)

        # Comparing the parsed expiry time with the five minutes later time

        if not five_minutes_later <= datetime.datetime.strptime(expiry_time, "%Y-%m-%d %H:%M:%S"):
            return "EXPIRED"
        
        token_data = dict(
            user_data = userinfo['user'],
            token_expires = expiry_time,
            entity_id_data = userinfo['entityId'],
            entityClass_data = userinfo['entityClassName'],
            webbase_data = validation_url.split('rest')[0],
            application_params_data = {},
            application_data = str(userinfo['applicationId']) 
        )
        
        token_data['bfabric_wrapper'] = bfabric.Bfabric(login=token_data['user_data'], password=userinfo['userWsPassword'], webbase=token_data['webbase_data'])

        return token_data
    
def entity_data(token_data):

    entity_class_map = {
        "Run": "run",
        "Sample": "sample",
        "Project": "container",
        "Order": "container",
        "Container": "container",
        "Plate": "plate"
    }

    if not token_data:
        return None

    wrapper = token_data.get('bfabric_wrapper', None)
    entity_class = token_data.get('entityClass_data', None)
    endpoint = entity_class_map.get(entity_class, None)
    entity_id = token_data.get('entity_id_data', None)

    if wrapper and entity_class and endpoint and entity_id:
        return wrapper.read_object(endpoint=endpoint, obj={"id":entity_id})[0]
    else:
        return None
