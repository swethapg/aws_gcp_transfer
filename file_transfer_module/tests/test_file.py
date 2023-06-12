import os
from unittest.mock import patch
from file_transfer_module.transfer import transfer_files, upload_to_s3, upload_to_gcs

@patch('file_transfer_module.transfer.boto3')
def test_upload_to_s3(mock_boto3):
    mock_s3_client = mock_boto3.client.return_value
    file_path = '/path/to/file.jpg'
    bucket = 'test-s3-bucket'

    upload_to_s3(file_path, bucket)

    mock_s3_client.upload_file.assert_called_once_with(
        file_path, bucket, os.path.basename(file_path)
    )

@patch('file_transfer_module.transfer.storage')
def test_upload_to_gcs(mock_storage):
    mock_storage_client = mock_storage.Client.return_value
    mock_bucket = mock_storage_client.bucket.return_value
    mock_blob = mock_bucket.blob.return_value
    file_path = '/path/to/file.pdf'
    bucket = 'test-gcs-bucket'

    upload_to_gcs(file_path, bucket)

    mock_storage.Client.assert_called_once()
    mock_storage_client.bucket.assert_called_once_with(bucket)
    mock_bucket.blob.assert_called_once_with(os.path.basename(file_path))
    mock_blob.upload_from_filename.assert_called_once_with(file_path)

@patch('file_transfer_module.transfer.upload_to_s3')
@patch('file_transfer_module.transfer.upload_to_gcs')
def test_transfer_files(mock_upload_to_gcs, mock_upload_to_s3):
    directory = '/path/to/files'
    s3_bucket = 'test-s3-bucket'
    gcs_bucket = 'test-gcs-bucket'

    transfer_files(directory, s3_bucket=s3_bucket, gcs_bucket=gcs_bucket)

    assert mock_upload_to_gcs.call_count == 3  # Assuming there are 3 files with GCS extensions
    assert mock_upload_to_s3.call_count == 7  # Assuming there are 7 files with S3 extensions

