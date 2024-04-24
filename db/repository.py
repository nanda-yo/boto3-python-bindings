from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource
from boto3.dynamodb.conditions import Key

from conf.settings import get_settings

config = get_settings()
class ItemsRepository:
    def __init__(self, db: ServiceResource) -> None:
        self.__db = db

    def get_all(self):
        table = self.__db.Table(config.AWS_TABLE_ID)  # referencing the table
        response = table.scan()             # gets ENTIRE table
        return response.get('Items', [])    # return data

    def get_item(self, id: str):
        try:
            table = self.__db.Table(config.AWS_TABLE_ID)              # referencing the table

            expression = Key('pk').eq(id)
            response = table.query(KeyConditionExpression=expression) # get item using pk (partition key), i had that like that for simplicity, but dumb aws doesnt allow lookup for just one key in other methods 3(
            if not response['Items']:
                raise KeyError
            else:
                return response['Items']
        except ClientError as e:
            raise KeyError(e.response['Error']['Message'])

    def create_item(self, item: dict):
        table = self.__db.Table(config.AWS_TABLE_ID)
        response = table.put_item(Item=item)
        token = item.get('pk')
        if response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            return token
        else:
            return response

    def update_item(self, item: dict):
        table = self.__db.Table(config.AWS_TABLE_ID)
        try:
            response = table.update_item(
                Key={'pk': item.get('pk'),'sk': item.get('sk')},
                UpdateExpression="""                
                    set
                        author=:author,
                        description=:description,
                        title=:title
                """,
                ConditionExpression ="pk = :pk AND sk = :sk",
                ExpressionAttributeValues={         # values defined in here will get injected to update expression
                    ':sk' : item.get('sk'),
                    ':pk' : item.get('pk'),
                    ':author': item.get('author'),
                    ':description': item.get('description'),
                    ':title': item.get('title')
                },
                ReturnValues="ALL_NEW"          # return the complete updated item
            )

            return response
        except ClientError as e:
            raise KeyError(e.response['Error']['Message'])
    def delete_item(self, pk: str, sk:str):
        table = self.__db.Table(config.AWS_TABLE_ID)  # referencing the table
        #sk = 'fkr'
        try:
            response = table.delete_item(           # delete item using pk and sk
                Key={'pk': pk,'sk': sk} #probably would be wise to use cond exp there aswell, cause this never returns 404 etc. Also for real life scenario, add ReturnedConsumedCapacity.
            )
            return response
        except ClientError as e:
            raise KeyError(e.response['Error']['Message'])