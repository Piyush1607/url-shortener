import time
import boto3

dynamodb = boto3.resource('dynamodb')

Table = dynamodb.Table('url_shortener')


def send_data(short_url, long_url, counter):
    res = Table.put_item(
        Item={
            'counter': counter,
            'url_ttl': int(time.time() + 300),
            'short_url': short_url,
            'long_url': long_url
        },
        ReturnValues='ALL_OLD'
    )

    print(res)


def get_url(short_url):
    res = Table.get_item(
        Key={
            'short_url': short_url
        }
    )

    return res["Item"]["long_url"]
