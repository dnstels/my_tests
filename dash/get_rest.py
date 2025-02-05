import calendar
import locale
from urllib.parse import quote
from flask import json
import requests
import pandas as pd

import numpy as np

url = "http://serv51:8005"
# url = "http://localhost:8000"

def get_from(endPoint,request=None,url=url):
    endPoint=f"/api/{endPoint}"
    # endPoint="/err500"
    try:
        response = requests.get(f'{url}{endPoint}',timeout=3)

        if response.status_code == 200:
            err=None
            res=response.text
        else:
            err_content=json.loads(response.content.decode('utf8').replace("'", '"'))
            err=f"Запрос: {endPoint} -> Ошибка: {response.status_code} \
                {json.dumps(err_content,ensure_ascii=False)}"
            res=None
    except requests.ConnectionError as e:
        res=None
        err="Сервер данных недоступен."
    except requests.Timeout as e:
        res=None
        err="Время ожидание ответа сервера данных окончено."
    except Exception as e:
        res=None
        err=f"Произошла ошибка: \n\r{str(e)}"
        print(err)
    finally:
        return (err,res)

def get_fake_graph_data():
    start_u=0
    end_u=80000

    data=[f'''{{"numberOfThePlanEndDate":{week},
         "humanLaborCostsDays":{0 if week==1 else np.random.uniform(start_u, end_u)}}}'''
         for week in range(1,54)]
    
    res=f"[{','.join(data)}]"
    return None,res

def empty_data():
    return pd.DataFrame({
        'group_name':[],
        'labor_costs':[]
    })

def create_request_department_for_LabourCost(departments):
    if departments == None: 
        return ''
    request= ','.join([item for item in departments]) \
        if type(departments) == list else departments
    return quote(request)

def get_LabourCost(departments,period_type=0):
    df=empty_data()
    request= create_request_department_for_LabourCost(departments)
    endPoint_labourCost=f"LabourCost/Period/{period_type}" if request==''\
        else f"LabourCost/Period/{period_type}/DepartmentCodes/{request}"
    err,res=get_from(endPoint_labourCost)
    # print(endPoint_labourCost)
    # err,df=get_fake()
    if res != None:
        df=pd.read_json(res)
        if len(df)>0:
            df.rename(columns={'humanLaborCostsDays': 'labor_costs'}, 
                            inplace=True)
            df.sort_values(by='numberOfThePlanEndDate')
            df['group_name']=df['numberOfThePlanEndDate'].astype(str)\
                if period_type==0 \
                    else nums_to_month(df['numberOfThePlanEndDate'])
        else:
            df=empty_data()
    # print(err,df)
    return (err,df)

def get_departments():
    df=pd.DataFrame({"id":[],"guid": [],"name": [],"departmentCode": [],
        "code": [] })
    err,result=get_from('Departments')
    if result!=None:
        df=pd.read_json(result)
    return err,df

def nums_to_month(nums):
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    return [f"[{num}] {calendar.month_abbr[num]}"for num in nums]

def get_ScheduledTime(departments):
    request= create_request_department_for_LabourCost(departments)
    res=None
    err=''
    if request=='':
        err,df_dep=get_departments()
        departments=df_dep['departmentCode'].to_list()
        request= create_request_department_for_LabourCost(departments)
    # res_err=err
    if err=='' or err==None:
        err,res=get_from(f"Departments/DepartmentCodes/{request}/ScheduledTime")
    # res_err+=f"\n- {err}"
    return err,res if res!=None else 0

