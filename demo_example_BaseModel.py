from datetime import datetime

from pydantic import BaseModel, PositiveInt ,computed_field,Field

from typing import Optional,Dict,Union
from dataclasses import dataclass

# @dataclass
class User(BaseModel):
    id: int =None
    name: str = Field(description='aqswdefre',alias='foo_alias', serialization_alias='foo_alias',default='John Doe')
    '''Наименование'''
    signup_ts_1: Union[datetime,None] = None  
    # signup_ts: datetime | None  
    signup_ts: Optional[datetime] = None  
    tastes: Optional[Dict[str, PositiveInt]]  = None

    @computed_field
    @property
    def Name(self) -> str:
        return self.name


external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',
    'foo_alias': 'My name',
    'tastes': {
        'wine': 9,
        b'cheese': 7,  
        'cabbage': '1',  
    },
}

user = User(**external_data)  
user1=User()

# print(user.id)
# print(user1.id)
print(user.model_dump())
print('~'*80)
print(user1.model_dump(by_alias=True))
print('~'*80)
for prop,v in User.model_fields.items():
    print(prop,'->',v.description)
# print(user.model_json_schema(by_alias=False)['properties']['name']['description'])

# print(user1.to_dict())



