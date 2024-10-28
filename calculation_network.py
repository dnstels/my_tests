# -*- coding: cp1251 -*-
"""

Template Excel Embedded Python Script

- Functions decorated with @xl_func will be available as functions in Excel
formulas, and those decorated with @xl_macro will be available as macros and
assigned, for instance, to buttons.  More than one decorator can be applied to
a given functions::
    from pyxll import xl_func, xl_macro
    @xl_macro
    @xl_func
    def foo():
        # do stuff here

- Functions decorated with @entry_point will appear in the drop-down list of
functions for this script::
    from enpyxll import entry_point
    @entry_point
    def bar():
        # do stuff here

- Log messages will appear in the Log Viewer when the @log_error decorator is
applied. This must be the last decorator on the method:
    from pyxll import xl_macro
    from enpyxll.util.logs import log_error
    import logging
    logger = logging.getLogger(__name__)

    @xl_macro
    @log_error
    def zub():
        logger.info("Running Zub")
        # do even more stuff here

"""

# Start your code here.
#
# Be sure to save the file once you are finished editing so that changes
# are picked up by Excel. Saving Excel does not automatically save
# changes to this script.
#
from pyxll import xl_macro
from sixgill.utilities import get_model_session
from sixgill.pipesim import Model
from sixgill.definitions import Parameters,Units,SystemVariables,ProfileVariables

import pandas as pd
import math
import numpy as np

from enpyxll.util.logs import log_error
import logging

import json

logger = logging.getLogger(__name__)
field_source = 'Source'
field_target = 'Destination'

@log_error
def connect_model_(filename = None):
    logger.info("Opening model {}".format(filename))
    return get_model_session(filename)

@log_error 
def connect_model(filename = None):
    logger.info("Opening model {}".format(filename))
    return Model.open(filename=filename, units=Units.METRIC)


@log_error
def close_model(model:Model):
    logger.info("Close model")
    model.close()
    
def make_out_dataframe(all_connections, flow_correlations):
    column_names = ['name', 'source', 'target']
    df_out = pd.DataFrame(columns=column_names)
    logger.info(all_connections)
    for flow in flow_correlations:
        t = list(all_connections.loc[all_connections[field_source] == flow][field_target])[0]
        s = list(all_connections.loc[all_connections[field_target] == flow][field_source])[0]
        df_out.loc[len(df_out.index)] = [flow, s, t]
    i = 0
    for f in df_out['source'].isin(df_out['target']):
        val = df_out.iloc[i]['source']
        # if not f:
        #     val = all_connections[all_connections[field_target] == df_out.iloc[i]['source']][field_source].values[0]
        df_out.iloc[i]['source'] = val
        i = i + 1
    return df_out
    
@xl_macro
@log_error 
def get_connection_info(filename):
    model=connect_model(filename)
    #begin some code
    all_connections = model.connections()
    all_connections_df=pd.DataFrame(all_connections)[[field_source, field_target]]
    
    sim_settings = model.sim_settings
    flow_correlation_mapping = sim_settings.get_flow_correlations()

    close_model(model)
    
    fc_data_frame = pd.DataFrame.from_dict(flow_correlation_mapping, orient="index")
    fc_data_frame = fc_data_frame.drop('Default', axis=0)
    fc_data_frame.index.name = "Name"
    all_flows=fc_data_frame.index.values.tolist()
    
    connect_df=make_out_dataframe(all_connections_df,all_flows)
    return (connect_df['name'].tolist(),connect_df['source'].tolist(),connect_df['target'].tolist())

@xl_macro
@log_error 
def get_geometry_profile(filename,flow_name):
    model=connect_model(filename)
    geometry_profile = model.get_geometry(context=flow_name)
    close_model(model)
    return geometry_profile[["HorizontalDistance","Elevation"]].to_json()

@xl_macro
@log_error
def get_info(filename,typename):
    model=connect_model(filename)
    connections_to_sinc = model.get_values(component =typename)
    connections_to_sinc_df=pd.DataFrame.from_dict(connections_to_sinc, orient="index")
    close_model(model)
    return [connections_to_sinc_df[['Name']].index.values.tolist()]

@xl_macro
@log_error
def get_flowline_values(filename,flowline):
    model=connect_model(filename)
    logger.info("get_flowline_values {}".format(flowline))
    res=[]
    # res.append(model.get_value(flowline, Parameters.Flowline.LENGTH))
    res.append(model.get_value(flowline, Parameters.Flowline.HORIZONTALDISTANCE))
    res.append(model.get_value(flowline, Parameters.Flowline.ELEVATIONDIFFERENCE))
    res.append(model.get_value(flowline, Parameters.Flowline.INNERDIAMETER))
    res.append(model.get_value(flowline, Parameters.Flowline.WALLTHICKNESS))
    res.append(model.get_value(flowline, Parameters.Flowline.ROUGHNESS))
    res.append(model.get_value(flowline, Parameters.Flowline.AMBIENTAIRTEMPERATURE))
    res.append(model.get_value(flowline, Parameters.Flowline.HeatTransfer.UCOEFFUSERAIR))
    close_model(model)
    return [res]

@xl_macro
@log_error
def get_conditions(filename,item):    
    import math
    model=connect_model(filename)
    logger.info("get_conditions {}".format(item))
    res=[]
    loc_list=["Pressure","Temperature","GasFlowRate"]

    studynetsim1 = model.tasks.networksimulation.get_conditions()
    for key,val in studynetsim1.items():
        if key == item:
            for k,v in val.items():
                if k in loc_list:
                    res.append(k + ':' + ('' if math.isnan(v) else str(v)))
                    # print("\t",k,':','' if math.isnan(v) else v,'\t')
    close_model(model)
    return [res]

@xl_macro
@log_error
def save_branch_to_file_(filename,separator,data_str,prof_general_json):
    logger.info(prof_general_json)
    
@xl_macro
@log_error
def save_branch_to_file(filename,separator,data_str,prof_general_json,prof_thermal_json):
    data=data_str.split(separator)
    flowline=data[0]
    model=connect_model(filename)
    if data[1]!='Nan': model.set_value(context=flowline,parameter=Parameters.Flowline.HORIZONTALDISTANCE, value=float(data[1].replace(",", ".")))
    if data[2]!='Nan': model.set_value(context=flowline,parameter=Parameters.Flowline.ELEVATIONDIFFERENCE, value=float(data[2].replace(",", ".")))
    if data[3]!='Nan': model.set_value(context=flowline,parameter=Parameters.Flowline.INNERDIAMETER, value=float(data[3].replace(",", ".")))
    if data[4]!='Nan': model.set_value(context=flowline,parameter=Parameters.Flowline.WALLTHICKNESS, value=float(data[4].replace(",", ".")))
    if data[5]!='Nan': model.set_value(context=flowline,parameter=Parameters.Flowline.ROUGHNESS, value=float(data[5].replace(",", ".")))
    if data[6]!='Nan': model.set_value(context=flowline,parameter=Parameters.Flowline.AMBIENTAIRTEMPERATURE, value=float(data[6].replace(",", ".")))
    # if data[6]!='Nan': model.set_value(context=flowline,parameter=Parameters.Flowline.AMBIENTWATERTEMPERATURE, value=float(data[6].replace(",", ".")))
    if data[7]!='Nan': model.set_value(context=flowline,parameter=Parameters.Flowline.HeatTransfer.UCOEFFUSERAIR, value=float(data[7].replace(",", ".")))
    
    # logger.info(prof_general_json)
    prof_thermal=pd.read_json(prof_thermal_json)
    prof_general_t=pd.read_json(prof_general_json)
    prof_general=prof_general_t.sort_index(axis=0, ascending=True, inplace=False)
    prof_thermal=prof_thermal.sort_index(axis=0, ascending=True, inplace=False)
    prof_general=prof_general.astype(np.float64)
    prof_thermal=prof_thermal.astype(np.float64)
    # print(prof_general.dtypes)
    #prof_general['MeasuredDistance']=''
    prof_general['Latitude']=''
    prof_general['Longitude']=''
    prof_general['IsVertex']=''
    MeasuredDistance=[]
    for index, row in prof_general.iterrows():
        # logger.info(row['HorizontalDistance'])
        # logger.info(row['Elevation'])
        MeasuredDistance.append(math.sqrt(float(row['HorizontalDistance'])**2+float(row['Elevation'])**2))
    prof_general['MeasuredDistance']=MeasuredDistance
        # logger.info(row['MeasuredDistance'])
    logger.info(prof_general)
    model.set_geometry(flowline,prof_general)
    model.set_geothermal_profile(flowline,prof_thermal)
    model.save()
    close_model(model)

def str_to_value(str_in):
    import re
    str_var=str_in
    str_var = re.sub(r'[^\d.,]', '', str_var.replace(",", "."))
    to_types = {
        'NaN': math.nan,
        '': math.nan,
        'True': True,
        'False': False
    }
    try:
        return float(str_var)
    except ValueError:
        return to_types.get(str_in,str_in)

def str_to_data(in_str):
    l1=in_str.split('@')
    dict_t=dict()
    dict_t1=dict()
    for i in range(0,len(l1),2):
        l2=l1[i+1].split(';')
        for item in l2:
            l=item.split(':')
            dict_t1[l[0]]=str_to_value(l[1])
        dict_t[l1[i]]=dict_t1
    return dict_t

@xl_macro
@log_error
def save_conditions_(filename,data_str):
    model=connect_model(filename)
    model.tasks.networksimulation.set_conditions(
            boundaries=str_to_data(data_str))
    model.save()
    close_model(model)
    
@xl_macro
@log_error
def save_conditions(filename,json_str):
    data=json.loads(json_str)
    model=connect_model(filename)
    for item in data:
        model.set_value(item['Name'],Parameters.Boundary.PRESSURE, float(item['Pressure']) if item['Pressure'] is not None else np.nan)
        model.set_value(item['Name'],Parameters.ModelComponent.ISACTIVE, bool(item['IsActive']))
        if item.get('Temperature')  is not None :
            model.set_value(item['Name'],Parameters.Boundary.TEMPERATURE, float(item['Temperature']))
        if item.get('GasFlowRate')  is not None :
            model.set_value(item['Name'],Parameters.Boundary.GASFLOWRATE, float(item['GasFlowRate']))
            
    # model.tasks.networksimulation.set_conditions(
    #         boundaries=str_to_data(data_str))
    model.save()
    close_model(model)

@xl_macro
@log_error
def clone_model(in_filename,out_filename):
    model=connect_model(in_filename)
    model.save(out_filename)
    close_model(model)

@xl_macro
@log_error
def simulation(in_filename):
    model=connect_model(in_filename)
    id_s=run_network_simulation(model)
    result=get_simulation_results(model,id_s)
    model.close()
    return result.to_json()

def run_network_simulation(model):
    ''' Run a network simulation '''
    system_variables = [
        SystemVariables.SYSTEM_OUTLET_TEMPERATURE, # (T вых)(Tout)
        SystemVariables.SYSTEM_TEMPERATURE_DIFFERENCE, # ((T вх)=(T вых)+(*))(Tin)
        
        SystemVariables.TEMPERATURE, # (T вх)(Tout) (Node)
        SystemVariables.PRESSURE, # (P вх)(Pin) (Node)
        
        SystemVariables.SYSTEM_OUTLET_PRESSURE, # (P исх)(Pout)
        SystemVariables.SYSTEM_INLET_PRESSURE, # (P вх)(Pin)
        SystemVariables.OUTLET_MASS_FLOWRATE_FLUID, # (Массовый расход газа)(MassRate) (*60 *60)
        SystemVariables.OUTLET_VOLUME_FLOWRATE_GAS_STOCKTANK, # (Расход газа)(GasRate)

        SystemVariables.MAXIMUM_VELOCITY_GAS, # (Макс скорость газа)(GasVelocity)(??)
    ]

    profile_variables = [        
        ProfileVariables.TEMPERATURE,
        ProfileVariables.PRESSURE,
        ProfileVariables.ELEVATION,
        ProfileVariables.TOTAL_DISTANCE
    ]
    
    simulation_id = model.tasks.networksimulation.start(
                                 profile_variables=profile_variables,
                                 system_variables=system_variables)
    logger.info("Running network simulation.")
    model.tasks.networksimulation.run(options={"GenerateOutputFile":False,"Restart":False,"Parallelism":4})
    return simulation_id

def get_simulation_results(model,id_s):
    ''' Get the simulation results once the simulation has finished '''
    results = model.tasks.networksimulation.get_results(id_s)

    # System variable results
    system_df = pd.DataFrame.from_dict(results.system, orient="index")
    system_df.index.name = "Variable"
    return system_df
    
# print(get_connection_info("D:\\repos\\Pipesim\\test-pipesim2020.1.pips"))
