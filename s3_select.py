import boto3

# S3 bucket to query (Change this to your bucket)

session=boto3.session.Session(profile_name="dev_root")
s3_cli=session.client(service_name="s3", region_name="us-east-2")

S3_BUCKET = 'tera1234'

r = s3_cli.select_object_content(
        Bucket=S3_BUCKET,
        Key='COLLEGE_DATA_2015.csv',
        ExpressionType='SQL',
        Expression="select \"INSTNM\" from s3object s where s.\"STABBR\" in ['OR', 'IA']",
        InputSerialization={'CSV': {"FileHeaderInfo": "Use"}},
        OutputSerialization={'CSV': {}},
)

for event in r['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)