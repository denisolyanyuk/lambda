import boto3
from io import BytesIO
s3 = boto3.resource('s3')
BUCKET = "input-files-bucket-denis"

s3.Bucket(BUCKET).upload_file("/home/denis/Desktop/1.png", "1.png")
