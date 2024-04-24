from pydantic import Field
from decimal import Decimal
from pydantic import BaseModel
from typing import List, Optional

from db.repository import ItemsRepository

class ItemParams(BaseModel):
    var1: str = Field(..., example='String Var')  #just some random stuff, i have no idea what i, if ever,  gonna do with that
    var2: str = Field(..., example='String Var 2')
    var3: Decimal = Field(..., example=2.5)

class ItemsModel(BaseModel):
    pk: Optional[str] = Field(..., example='Primary Key, typeof int')
    sk: Optional[str] = Field(..., example='Sorting Key, typeof str')
    title: str = Field(..., example='Example Title')
    author: str = Field(..., example='Example Author')
    description: Optional[str] = Field(..., example='Example Description')
    params: List[ItemParams]


class ItemsDomain():
    def __init__(self, repository: ItemsRepository) -> None:
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def get_item(self, id: str):
        return self.__repository.get_item(id)

    def create_item(self, item: ItemsModel):
        #item.pk = str(uuid4())
        return self.__repository.create_item(item.dict())

    def update_item(self, item: ItemsModel):
        return self.__repository.update_item(item.dict())

    def delete_item(self, id: str,range_key: str):
        return self.__repository.delete_item(id, range_key)