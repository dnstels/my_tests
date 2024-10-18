from abc import ABC, abstractmethod
from dataclasses import dataclass
@dataclass
class AbsClass(ABC):
    a:int
    b:int

    def _get_headers(self):
        return (i_attr for i_attr in [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")])
    
    def get_headers_():
        return (i_attr for i_attr in [attr for attr in dir(__class__) if not callable(getattr(__class__, attr)) and not attr.startswith("_")])
    @abstractmethod
    def get_headers(self):
        return self.__annotations__
    
    @classmethod
    def get_annotations(cls):
        d = {}
        for c in cls.mro():
            try:
                d.update(**c.__annotations__)
            except AttributeError:
                # object, at least, has no __annotations__ attribute.
                pass
        return d

@dataclass
class SubClass(AbsClass):
    c:int

    def get_headers(cls):
        return __class__.__annotations__.update(super().get_headers())
    

v1=SubClass(1,2,3)
# print(tuple(v1.get_headers()))

print(SubClass.get_annotations().keys())

# for i in SubClass.get_headers():
#     print(i)
