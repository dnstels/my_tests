import json


class JsonClassEncoder(json.JSONEncoder):
    def default(self, obj):
        # if isinstance(obj, Address):
        # return obj.__dict__
        # out={}
        # for i_attr in [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("_")]:
        #     out[i_attr]=obj.__getattribute__(i_attr)
        return {i_attr:obj.__getattribute__(i_attr) for i_attr in [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("_")]}


def get_first_or_none(obj):
    return next(iter(obj if hasattr(obj, '__iter__') else []), None)

def get_atter(obj,attr_name:str):
    return obj.__getattribute__(attr_name) if hasattr(obj,attr_name) else None

def norm_dict(t:type,d:dict):
    return {i:d.get(i,None) for i in t.__annotations__ }
