# Função Lambda para Envio de E-mails

## Descrição
Esta função Lambda foi criada para enviar e-mails usando o Amazon Simple Email Service (Amazon SES). A função é escrita em Python e é implantada na AWS.

## Estrutura do Repositório

Trabalho_lambda/
├── handler.py
├── README.md
└── requirements.txt


## Arquivo `handler.py`
O arquivo `handler.py` contém o código da função Lambda.

```python
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

Arquivo requirements.txt
O arquivo requirements.txt lista as dependências necessárias para a função Lambda.

boto3

Configuração do Handler
No console AWS Lambda, a configuração do handler deve ser handler.lambda_handler.

Permissões IAM
A função Lambda precisa de permissões para enviar e-mails usando o Amazon SES. Certifique-se de que o papel IAM associado à função Lambda tem a política AmazonSESFullAccess ou uma política personalizada com permissões para o Amazon SES.

Exemplo de Política Personalizada

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ses:SendEmail",
            "Resource": "arn:aws:ses:sa-east-1:211125763260:identity/ridan696@gmail.com"
        }
    ]
}


Verificação do Endereço de E-mail
Antes de enviar e-mails usando o Amazon SES, você precisa verificar o endereço de e-mail do remetente. Siga estes passos:

No console AWS, vá para o serviço Amazon SES.
Clique em "Email Addresses" no painel de navegação esquerdo.
Clique em "Verify a New Email Address".
Insira o endereço de e-mail ridan696@gmail.com e clique em "Verify This Email Address".
Abra o e-mail de verificação e clique no link para confirmar a verificação.
Testando a Função Lambda
No console AWS Lambda, selecione a função sendEmailLambda.
Clique em "Test".
Crie um novo evento de teste com o seguinte JSON:

{
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

Execute o teste e verifique os logs para confirmar que o e-mail foi enviado com sucesso.
Monitoramento e Logs
Para monitorar a função e ver os logs, siga estes passos:

No console AWS Lambda, vá para a aba "Monitoramento".
Clique em "Ver logs no CloudWatch".
Verifique os logs gerados durante a execução da função para identificar qualquer problema.
Troubleshooting
Erro de Permissão (AccessDeniedException): Verifique se o papel IAM associado à função Lambda tem a política correta para o Amazon SES.
Erro de Verificação de E-mail (Email address is not verified): Certifique-se de que o endereço de e-mail do remetente foi verificado no Amazon SES.
Erro de Configuração do Handler: Verifique se o handler está configurado corretamente como handler.lambda_handler.
Conclusão
Esta documentação cobre os passos necessários para criar, configurar e testar a função Lambda para enviar e-mails usando o Amazon SES.
 Se houver qualquer problema ou se precisar de mais assistência, sinta-se à vontade para pedir ajuda.