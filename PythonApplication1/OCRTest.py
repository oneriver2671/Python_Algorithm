

import requests
import uuid
import time
import json

api_url = 'https://i1rgck9mtk.apigw.ntruss.com/custom/v1/35263/a87e3be54dd4ba3219896c3753a9fc4a285940ad7550aa81a4932101be900354/general'
secret_key = 'dENYclhVT3B1RndNUFBXSFBzdk9PQkhVRFFtSHRteEE='
image_file = '/images/날마다_숨쉬는_순간마다.jpg'

request_json = {
    'images': [
        {
            'format': 'jpg',
            'name': 'demo'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}

payload = {'message': json.dumps(request_json).encode('UTF-8')}
files = [
  ('file', open(image_file,'rb'))
]
headers = {
  'X-OCR-SECRET': 'dENYclhVT3B1RndNUFBXSFBzdk9PQkhVRFFtSHRteEE='
}

response = requests.request("POST", api_url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))

