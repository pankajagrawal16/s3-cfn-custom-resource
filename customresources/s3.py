from botocore.exceptions import ClientError
from crhelper import CfnResource
import logging
import boto3

logger = logging.getLogger(__name__)
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL')
s3_client = boto3.client('s3')

try:
    pass
except Exception as e:
    helper.init_failure(e)


@helper.create
@helper.update
def put_object(event, _):
    logger.info("Stack creation few folders will be created under S3 bucket")

    bucket = event['ResourceProperties']['S3Bucket']
    folders = event['ResourceProperties']['SubFolders']

    for folder in folders:
        try:
            response = s3_client.put_object(Bucket=bucket, Body='', Key=folder + '/')
            logger.info(f'Created Successfully {response}')
        except ClientError as ex:
            raise ValueError(f'Failed creating folder {folder} inside bucket {bucket} for reason {ex.response}')
    helper.Data.update({})
    return event.get("PhysicalResourceId", {})


@helper.delete
def delete(event, context):
    logger.info("Stack delete therefore no real changes required on resources")


def handler(event, context):
    helper(event, context)
