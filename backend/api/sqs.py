import boto3, json, os
from dotenv import load_dotenv

load_dotenv()

QUEUE_URL = os.environ['SQS_URL']

SQS = boto3.client('sqs', aws_access_key_id=os.environ['AWS_ACCESS'],
                   aws_secret_access_key=os.environ['AWS_SECRET'], region_name=os.environ['AWS_REGION'])


def send_messages(l, r):
    for i in range(l, r):
        SQS.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=str(i),
            MessageGroupId='Counter'
        )





def poll_counter():
    received_message = SQS.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=1
    )
    SQS.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=received_message['Messages'][0]['ReceiptHandle'])
    counter_val = int(received_message['Messages'][0]['Body'])
    print(json.dumps(received_message, indent = 4))
    return counter_val




