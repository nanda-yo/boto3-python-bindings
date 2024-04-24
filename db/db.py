import boto3
from boto3.resources.base import ServiceResource

from conf.settings import get_settings

config = get_settings()

def initialize_db() -> ServiceResource:
    ddb = boto3.resource('dynamodb',
                         region_name=config.AWS_REGION,
                         aws_access_key_id=config.AWS_ACCESS_KEY_ID.get_secret_value(),
                         aws_session_token=config.AWS_SESSION_TOKEN.get_secret_value(),
                         aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY.get_secret_value()
                         )

    return ddb