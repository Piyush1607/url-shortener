import json
from rest_framework.response import Response
from .sqs import poll_counter
from .dynamo import send_data, get_url
from rest_framework.decorators import api_view
from .utils import base62_encode
from django.shortcuts import redirect

BASE_URL = "http://127.0.0.1:8000/"


@api_view(['POST'])
def shortUrl(req):
    body = json.loads(req.body)
    counter = int(100000 + poll_counter())
    short_url = f'{BASE_URL}{base62_encode(counter)}'
    send_data(short_url=short_url, long_url=body['url'], counter=str(counter))
    return Response({
        "short_url": short_url
    })


@api_view(['GET'])
def redirect_short(req, short_url_id):
    try:
        return redirect(get_url(BASE_URL + short_url_id))
    except:
        return Response(status=404, data={
            "message": "url expired"
        })
