import json 
from datetime import date, timedelta
from mock_data_generator import generate_data
from upload_to_s3 import upload_to_s3
from create_rds_schema import connect_and_create_db


def lambda_handler(event, context):

    start_date = date(2024, 5, 29)
    end_date = date.today()

    for current_date in range((end_date - start_date).days + 1):
        
        # Generate Date
        current_date = start_date + timedelta(days = current_date)
        date_str = str(current_date)
        generate_data(current_date, date_str)

        # Upload generated CSV file to S3
        upload_to_s3(f"transactions_{date_str}.csv", date_str)

        # Connect to RDS, create customers database and customer_transactions table
    connect_and_create_db()

    return {
        'StatusCode':200,
        'body':json.dumps("Customer Data Generated, uploaded to S3, created RDS DB and Table")
    }