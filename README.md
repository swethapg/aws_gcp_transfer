# aws_gcp_transfer

The File Transfer Module is a Python package that allows you to transfer files from a directory and its subdirectories to AWS S3 and Google Cloud Storage. The module supports customizable file types for S3 and GCS transfers.

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies using pip:

```shell
pip install -r requirements.txt
```

3. Install the module using pip:

```shell
    pip install .
```

### Usage

To use the File Transfer Module, follow these steps:

1. Import the transfer_files function from the module:

```shell
    from file_transfer_module.file import transfer_files
```

2. Specify the directory containing the files, the AWS S3 bucket name, and the Google Cloud Storage bucket name:

```shell
    directory = '/path/to/files'
    s3_bucket = 'your-s3-bucket'
    gcs_bucket = 'your-gcs-bucket'
```

3. Call the transfer_files function with the directory and bucket names as arguments:

```shell
    transfer_files(directory, s3_bucket=s3_bucket, gcs_bucket=gcs_bucket)
```

4. The files with matching file types will be transferred to the respective cloud storage services.


#### Configuration

    The file types for S3 and GCS transfers are configurable. To modify the supported file types, open the file.py file and update the s3_file_types and gcs_file_types lists with the desired file extensions.


##### Running the Tests

    The module includes unit tests implemented using pytest. To run the tests and check code coverage, follow these steps:

1. Install the test dependencies:

```shell
    pip install -r requirements.txt
```
2. Run the tests using pytest:

```shell
    pytest file_transfer_module/tests --cov=file_transfer_module
```
    The code coverage report will be displayed, indicating the percentage of code coverage achieved.


