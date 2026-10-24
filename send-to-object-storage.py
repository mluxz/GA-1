import os
import boto3
import logging
import time
from datetime import datetime
import pytz 
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

access_key = os.getenv('231786a8-2f4c-424e-afe0-7f2e6472dd17')
secret_key = os.getenv('9d27c2c98eb1d80a1d7e774a9d3bf3da64ef806fb6b9940b20ceb094fd14e38c')

def upload_files_from_directory(directory):
    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url = "https://s3.ir-thr-at1.arvanstorage.ir",
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key
        )

        bucket_name = '12857'

        bucket = s3_resource.Bucket(bucket_name)
        bucket.create(ACL='public-read')

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):  # Check if it's a file
                object_name = filename  # Use the filename as the object name

                with open(file_path, "rb") as file:
                    s3_resource.Bucket(bucket_name).put_object(
                        ACL='private',
                        Body=file,
                        Key=object_name
                    )

                logging.info(f"File '{filename}' uploaded successfully")
    except Exception as e:
        logging.error(e)

# Specify the directory containing files to upload
directory_path = './stage'  # Change this to your directory
upload_files_from_directory(directory_path)