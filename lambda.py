import boto3, uuid

def lambda_handler(event, context):
  tab = boto3.resource("dynamodb").Table("sensordata")
  event['key'] = str(uuid.uuid1())
  table.put_item(Item=event)
