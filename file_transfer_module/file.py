import os
import boto3
from google.cloud import storage

def transfer_files(directory, s3_bucket=None, gcs_bucket=None):
    """
    Transfers files from the specified directory and its subdirectories
    to AWS S3 and Google Cloud Storage.

    Args:
        directory (str): The directory path containing the files.
        s3_bucket (str, optional): The AWS S3 bucket name. Defaults to None.
        gcs_bucket (str, optional): The Google Cloud Storage bucket name. Defaults to None.
    """
    # List all files in the specified directory and its subdirectories
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_list.append(file_path)

    # Transfer files to AWS S3 and Google Cloud Storage
    for file_path in file_list:
        file_extension = os.path.splitext(file_path)[1][1:].lower()
        if file_extension in s3_file_types and s3_bucket:
            upload_to_s3(file_path, s3_bucket)
        elif file_extension in gcs_file_types and gcs_bucket:
            upload_to_gcs(file_path, gcs_bucket)

def upload_to_s3(file_path, bucket):
    """
    Uploads a file to AWS S3.

    Args:
        file_path (str): The path of the file to upload.
        bucket (str): The AWS S3 bucket name.
    """
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket, os.path.basename(file_path))

def upload_to_gcs(file_path, bucket):
    """
    Uploads a file to Google Cloud Storage.

    Args:
        file_path (str): The path of the file to upload.
        bucket (str): The Google Cloud Storage bucket name.
    """
    storage_client = storage.Client()
    bucket_obj = storage_client.bucket(bucket)
    blob = bucket_obj.blob(os.path.basename(file_path))
    blob.upload_from_filename(file_path)

# Configurable file types for S3 and GCS transfer
s3_file_types = ['jpg', 'png', 'svg', 'webp', 'mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm']
gcs_file_types = ['doc', 'docx', 'csv', 'pdf']
