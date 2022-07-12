from pydantic import BaseModel, ValidationError
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    id: int
    name: str = "Tom"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {
    "id": 123,
    "name": "John",
    "signup_ts": "2022-07-09 12:22",
    "friends": [1,2,"3"]
}

user = User(**external_data)
# print(user.id, user.name, user.signup_ts, user.fields)

# try:
#     User(id="Num", name=12, friends=[1, 2, 3, 4])
# except ValidationError as e:
#     print(e.json())

print(user.dict())
print(user.json())
print(user.copy())
print(User.parse_obj(obj=external_data))
# print(User.parse_raw())