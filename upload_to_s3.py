import boto3

s3_client = boto3.client('s3')

bucket_name = "debit-card-bucket"

def upload_to_s3(filename, date_str):
    file_path = f"raw_data/date={date_str}/{filename}"
    s3_client.upload_file(
        f'/tmp/{filename}',
        bucket_name,
        file_path
    )
    print(f"File Uploaded to S3 bucket {bucket_name}/{file_path}")
    return