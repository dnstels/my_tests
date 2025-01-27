from urllib.parse import quote
import requests
import pandas as pd

import numpy as np

url = "http://serv51:8005/api/"

def get_from(endPoint,request=None,url=url):
    try:
        response = requests.get(f'{url}{endPoint}',timeout=3)

        if response.status_code == 200:
            err=None
            res=response.text
        else:
            err=f"Ошибка: {response.status_code}"
            res=None
    except:
        res=None
        err='Сервер данных недоступен'
    finally:
        return (err,res)

def get_fake():
    start_u=0
    end_u=80000
    df = pd.DataFrame({
        'weekNumberOfThePlanEndDate':
            [str(week_num)for week_num in range(1,54)],
        'humanLaborCostsDays':
            [np.random.uniform(start_u, end_u)for n in range(1,54)]
    })
    data=[f'''{{"weekNumberOfThePlanEndDate":{week},
         "humanLaborCostsDays":{0 if week==1 else np.random.uniform(start_u, end_u)}}}'''
         for week in range(1,54)]
    
    res=f"[{','.join(data)}]"
    # return (None,df)
    return None,res

def empty_data():
    return pd.DataFrame({
        'week_num':[],
        'labor_costs':[]
    })

def get_LabourCost(departments):
    df=empty_data()
    request= departments if departments == None else quote(','.join([item for item in departments]))
    endPoint_labourCost="LabourCost" if departments==None else f"LabourCost/DepartmentCodes/{request}"
    err,res=get_from(endPoint_labourCost)
    # err,df=get_fake()
    if res != None:
        df=pd.read_json(res)
        df.rename(columns={'weekNumberOfThePlanEndDate': 'week_num', 
                        'humanLaborCostsDays': 'labor_costs'}, 
                        inplace=True)
        df['week_num']=df['week_num'].astype(str)

    return (err,df)