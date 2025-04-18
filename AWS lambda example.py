import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Triggered by S3 upload event.")

    # Get bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key    = event['Records'][0]['s3']['object']['key']

    print(f"Processing file: s3://{bucket}/{key}")

    # Download the file (into memory)
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read()

    print(f"File retrieved successfully! Size: {len(content)} bytes.")

    return {
        'statusCode': 200,
        'body': f"Downloaded {key} from {bucket}"
    }
