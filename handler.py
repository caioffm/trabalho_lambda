import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    SENDER = "ridan696@gmail.com"
    RECIPIENT = "ridan696@gmail.com"
    AWS_REGION = "sa-east-1"
    SUBJECT = "Teste Amazon SES"
    
    BODY_TEXT = ("Amazon SES Test\r\n"
                 "Este e-mail foi enviado com Amazon SES usando "
                 "AWS SDK para Python (Boto3)."
                )
                
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Amazon SES Test</h1>
      <p>Este e-mail foi enviado com
        <a href='https://aws.amazon.com/ses/'>Amazon SES</a> usando
        <a href='https://boto3.amazonaws.com/v1/documentation/api/latest/index.html'>AWS SDK para Python (Boto3)</a>.</p>
    </body>
    </html>
                """            
    CHARSET = "UTF-8"
    
    client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        return e.response['Error']['Message']
    else:
        return "Email sent! Message ID: " + response['MessageId']
