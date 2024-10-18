from dataclasses import dataclass
import importlib
import json
import sys
from typing import List
try:
    if '.' not in sys.path :
        sys.path.append('.')
    import tools
except ImportError:
    spec = importlib.util.spec_from_file_location("models","core/tools.py")
    tools = importlib.util.module_from_spec(spec)
    sys.modules["tools"] = tools
    spec.loader.exec_module(tools)


@dataclass
class Profile:
    HorizontalDistance: float
    '''Горизонтальное расстояние'''
    Elevation: float
    '''Высота'''

    MeasuredDistance:float

@dataclass
class Flowline:
    Name:str
    HorizontalDistance:float
    '''Длина'''
    Elevation: float 
    '''Возвышение(высота)'''
    InnerDiameter: float 
    '''Диаметр(внешний)'''
    WallThickness: float 
    '''Толщина стенки'''
    Temperature: float 
    '''Температура'''
    Roughness:float 
    '''Шероховатость'''
    UCoeffuserAir:float 
    '''Температурный коэффициент'''

    @property
    def Diameter(self):
        return self.InnerDiameter+(self.WallThickness*2)
    @Diameter.setter
    def Diameter(self,value:float):
        self.InnerDiameter=value-(self.WallThickness*2)

    def to_json(self):
        d=self.__dict__
        prop_inc='Diameter'
        if hasattr(self, prop_inc):
            d[prop_inc]=self.__getattribute__(prop_inc)
        prop_exc='InnerDiameter'
        if hasattr(self, prop_exc) and (prop_exc in d):
            del d[prop_exc]
        out={self.Name:d}
        return json.dumps(out,cls=tools.JsonClassEncoder,indent=4)

@dataclass
class Names:
    Flowline:List[str]
    '''Трубопроводы'''
    Source:List[str]
    '''Источники'''
    Sink:List[str]
    '''Стоки'''
    Junction:List[str]
    '''Узлы'''
    Choke:List[str]
    '''Штуцеры'''

    @staticmethod
    def get_types():
        return tuple(Names.__annotations__)
    @staticmethod
    def get_valid_node_types():
        return ('Source','Sink','Junction')
    def get_valid_nodes(self):
        return self.Source+self.Sink+self.Junction

@dataclass
class Source:
    Pressure:float
    '''Давление'''
    Temperature:float
    '''Температура'''
    GasFlowRate:float
    '''Расход газа'''

@dataclass
class Sink:
    Pressure:float
    '''Давление'''
    GasFlowRate:float
    '''Расход газа'''

@dataclass(frozen=True)
class Branch():
    Source:str
    Destination:str
    def validate(self):
        return self.Source != None and self.Destination != None
    @staticmethod
    def get_orients():
        return Branch.__annotations__
    @staticmethod
    def get_revers_orient(orient:str):        
        return tools.get_first_or_none([s for s in Branch.get_orients() if s != orient])


@dataclass
class ProjectDataModel:
    Names:Names
    Network:List[Branch]
    Flowline_data:{Flowline}
    Conditions_data:{}
    Constraints_data:{}
    Siulation_data:{}
    pipesim_file:str
    project_name:str
