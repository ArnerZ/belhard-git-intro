from pydantic import BaseModel
from typing import Any,List 
tt = {
    'age':41,
    'name': 'Stas',
    'children': [
        {
            'age': 10,
            'name': 'Masha'
        }
    ],
    'married': True,
    'city': None
}

class TT(BaseModel):
    age: int
    name: str
    children: List
    married: bool
    city: Any


print(TT)
s = TT(**tt)
print(s.json())