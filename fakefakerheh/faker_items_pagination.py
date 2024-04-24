from pydantic import Field
from decimal import Decimal
from pydantic import BaseModel
from typing import List, Optional
from faker import Faker
from uuid import uuid4

thefaker = Faker()



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


class ItemsFactoryWithPagination():
    @classmethod
    def generate_pk(cls):
        return str(uuid4())

    @classmethod
    def generate_sk(cls):
        # Implement your own logic to generate realistic names
        return str("fkr")

    @classmethod
    def generate_title(cls):
        # Implement your own logic to generate hobbies
        return Faker().paragraph(nb_sentences=2)

    @classmethod
    def generate_author(cls):
        # Implement your own logic to generate realistic ages
        return Faker().name()

    @classmethod
    def generate_description(cls):
        # Implement your own logic to generate realistic birthdays
        return Faker().text(max_nb_chars = 300)
    @classmethod
    def generate_params(cls):
        var1=Faker().isbn10()
        var2=Faker().isbn10()
        var3=Faker().pydecimal(left_digits=4,right_digits=3)
        var3=2.5

        return ItemParams(var1=var1,var2=var2,var3=var3)


    @classmethod
    def build(cls,prevToken,nextToken):
        pk = cls.generate_pk()
        sk = cls.generate_sk()
        title = cls.generate_title()
        author = cls.generate_author()
        description = cls.generate_description()
        #params = cls.generate_params()
        var1=Faker().isbn10()
        var2=str(Faker().isbn10())
        var3=Faker().pydecimal(left_digits=4,right_digits=3)
        params = [
     {
       "var1": var1,
       "var2": var2,
       "var3": var3
     }
   ]
        return ItemsModel(pk=pk,sk=sk,title=title,author=author,description=description,params=params)
