import json
import logging
from functools import wraps
from typing import OrderedDict

from numpy import nan
from sixgill.pipesim import Model
from sixgill.definitions import Units,Parameters,ModelComponents,ProfileVariables,SystemVariables,SimulationState
import pandas as pd
import sys
import time
sys.path.append('.')
from  core.models import ProjectDataModel,Names,Flowline
from  core import tools

from io import StringIO

import six

def logging_setting():
    # manta.server.manager.logger.addHandler(logging.NullHandler())
    # log_stream = StringIO()
    # # logging.basicConfig(stream=log_stream)
    # logging.basicConfig(filename='app.log', filemode='w',level=logging.INFO)
    fileHandler = logging.FileHandler('app.log')
    class LogStream(object):
        def __init__(self):
            self.logs = ''

        def write(self, str):
            self.logs += str

        def flush(self):
            pass

        def __str__(self):
            return self.logs

    log_stream = LogStream()
    # logging.basicConfig(stream=log_stream,level=logging.ERROR)

    # log=logging.getLogger('manta.server.manager')
    # log=logging.getLogger()
    # FORMAT = "%(process)s %(thread)s: %(message)s"
    FORMAT = "%(levelname)s: %(name)s: %(message)s"
    formatter=logging.Formatter(fmt=FORMAT)
    fileHandler.setFormatter(formatter)
    # log.addHandler(fileHandler)
    # log.propagate = False
    # log.info('1234567890')
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for l in loggers:
        l.propagate=False
        l.addHandler(fileHandler)
    # loggers = [name for name in logging.root.manager.loggerDict]
    # print(loggers)

params_base=[
        Parameters.Flowline.GEOMETRYPROFILE,

        # Parameters.Flowline.GEOTHERMALPROFILE,

        Parameters.Flowline.HORIZONTALDISTANCE,
        Parameters.Flowline.ELEVATIONDIFFERENCE,
        Parameters.Flowline.INNERDIAMETER,
        Parameters.Flowline.WALLTHICKNESS,
        Parameters.Flowline.ROUGHNESS,
        Parameters.Flowline.AMBIENTAIRTEMPERATURE,
        Parameters.Flowline.HeatTransfer.UCOEFFUSERAIR,
        Parameters.Flowline.HeatTransfer.UCOEFFUSER,
        ]
params_ext=[
        Parameters.Flowline.GEOMETRYPROFILE,
        Parameters.Flowline.GEOTHERMALPROFILE,
]

PROFILE_PARAMS=['MeasuredDistance',  'HorizontalDistance',  'Elevation']
IN_DATA_PARAMS=['Pressure','Temperature','GasFlowRate']
CONDITIONS_PARAMS=['Temperature', 'Pressure', 'FlowRateType', 'GasFlowRate']

Parameters.Sink

def get_names(model:Model):
    out_dict={}
    for prop in Names.get_types():
        out_dict[prop]=[item['Name'] for item in model.find_components(component=prop)]
    return out_dict

def get_data_flowlines(model:Model):
    flow_lines=model.get_values(component=ModelComponents.FLOWLINE,parameters=params_base)
    # profiles={flow_name:get_geometry(model,flow_name) for flow_name in list(flow_lines)}
    # return (flow_lines,profiles)
    flow_lines_dict={}
    profile_dict={}
    for k,v in flow_lines.items():
        flow_lines_dict[k]=v#tools.norm_dict(Flowline,v)
        profile_pipesim= v[Parameters.Flowline.GEOMETRYPROFILE]
        if profile_pipesim != None:
            profile=profile_pipesim.data_frame[PROFILE_PARAMS].to_dict(orient ='records')
            profile_dict[k]=profile
    return (flow_lines_dict,profile_dict)

# def get_geometry(model:Model,flow_name):
#     return list(model.get_geometry(context=flow_name)[["HorizontalDistance","Elevation"]].to_dict())

def get_network(model:Model):
    return model.connections()

def get_indata(model:Model):
    out=model.get_values(component=ModelComponents.SOURCE,
                         parameters=IN_DATA_PARAMS)
    out.update(model.get_values(component=ModelComponents.SINK,
                         parameters=IN_DATA_PARAMS))
    return out

def get_simulation(model:Model):
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
        system_variables=system_variables,options={"GenerateOutputFile":False,"Restart":False,"Parallelism":4})
    
    # results=model.tasks.networksimulation.run(options={"GenerateOutputFile":False,"Restart":False,"Parallelism":4})
    
    i=0
    start_time = time.time()
    start_localtime=time.strftime('%d.%m.%Y %H:%M:%S',time.localtime(start_time))
    print(f'Start simulation {start_localtime}')
    status = model.tasks.networksimulation.get_state(simulation_id)
    while status == SimulationState.RUNNING: #'Running':
        i=i+1
        status = model.tasks.networksimulation.get_state(simulation_id)
        if (time.time() - start_time) > 60: 
            print('TimeOut ERROR !!!')
            status = SimulationState.FAILED #'Flied'

        # print(f'{i} State simulation {model.tasks.networksimulation.get_state(simulation_id)}')
    
    print(f'-- State simulation {model.tasks.networksimulation.get_state(simulation_id)}')
    print("--- %s seconds ---" % (time.time() - start_time))

    results = model.tasks.networksimulation.get_results(simulation_id)
    return results# .system


def get_conditions(model:Model):
    return pd.DataFrame.from_dict(model.tasks.networksimulation.get_conditions()).T[CONDITIONS_PARAMS].T.to_dict()
def get_constraints(model:Model):
    return model.tasks.networksimulation.get_constraints()

def open():
    filename='D:\\repos\\Pipesim_\\test-test-test.pips'
    return Model.open(filename=filename, units=Units.METRIC)


if __name__=='__main__':
    filename='D:\\repos\\Pipesim_\\test-test-test.pips'
    # flowline=Flowline
    # for member in [attr for attr in dir(flowline) 
    #                    if not callable(getattr(flowline, attr)) 
    #                    and (not attr.startswith("_"))]:
    #     print(member)
    
    # model=Model.open(filename=filename, units=Units.METRIC)
    model=open()
    # print(model.get_values(component=ModelComponents.FLOWLINE,parameters=params_base))
    names=get_names(model)
    (flow_lines,profiles)=get_data_flowlines(model)
    # flow_lines=get_data_flowlines(model)
    network=get_network(model)
    in_data=get_indata(model)
    conditions=get_conditions(model)
    constraints=get_constraints(model)
    # simulation=get_simulation(model)
    # print(model.session)
    model.close()
    # print(model.session)
    # # model.close()
    # print('-'*25,'names','-'*25)
    # # # print(pd.DataFrame.from_dict(in_data))
    # print(names)
    print('-'*25,'flow_lines_dict','-'*25)
    # print(pd.DataFrame.from_dict(in_data))
    # print(json.dumps(flow_lines,cls=tools.JsonClassEncoder))
    print(flow_lines)
    # print(pd.DataFrame(profiles['kg202-205.Flowline_1']))
    print(profiles)
    # print('-'*25,'network','-'*25)
    # # print(pd.DataFrame.from_dict(in_data))
    # print(network)
    # print('-'*25,'in_data','-'*25)
    # # print(pd.DataFrame.from_dict(in_data))
    # print(in_data)
    # print('-'*25,'conditions','-'*25)
    # # print(pd.DataFrame.from_dict(conditions))
    # print(conditions)
    print('-'*25,'constraints','-'*25)
    # # print(pd.DataFrame.from_dict(constraints))
    print(constraints)
    # print('-'*25,'simulation','-'*25)
    # print(pd.DataFrame(simulation.messages))
    # print(pd.DataFrame.from_dict(simulation.summary, orient="index").T)
    # print(pd.DataFrame.from_dict(simulation.system, orient="index").to_dict()) ## !!! work variant 
    # print(simulation.system)
    
    # print('-'*50)
    # for k,v in names.items():
    #     print(k,v)
    # print('-'*50)
    # for k,v in flow_lines_dict.items():
    #     print(k,v.to_json())
    
    # print(log_stream)
    # print(log_stream.getvalue())
    
    pass
