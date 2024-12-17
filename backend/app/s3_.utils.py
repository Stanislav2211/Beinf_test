import boto3
from botocore.exceptions import NoCredentialsError

BUCKET_NAME = "your-bucket-name"

def upload_to_s3(filename: str, content: str) -> str:
    """
    Завантаження файлу у S3.
    """
    s3 = boto3.client("s3")
    try:
        s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=content)
        return f"s3://{BUCKET_NAME}/{filename}"
    except NoCredentialsError:
        raise Exception("AWS credentials not found.")
