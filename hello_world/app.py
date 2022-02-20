from random import random
import boto3
from io import BytesIO
from PIL import Image


def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    file_name = file_key.split('.')[0]
    s3 = boto3.resource('s3')
    input_bucket = s3.Bucket(bucket_name)
    output_bucket = s3.Bucket('output-images-denis')
    file = BytesIO()
    input_bucket.download_fileobj(file_key, file)

    im = Image.open(file)
    rgb_im = im.convert('RGB')
    byte_io = BytesIO()
    rgb_im.save(byte_io, format="JPEG")
    with BytesIO() as output:
        rgb_im.save(output, format="jpeg")
        contents = output.getvalue()
        b = BytesIO(contents)
        print(len(contents))
        output_bucket.upload_fileobj(b, f'{file_name}{random()*1000}.jpeg')
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
        },
        'body': 'success'
    }
