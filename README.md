# dio-live-rekognition
Repositório para a live do dia 14/10/2021

## Serviços utilizados
 - Amazon S3
 - Amazon IAM
 - AWS Lambda
 - Amazon Rekognition

## Configurações iniciais

### No Amazon IAM
 - IAM Console - Roles - Create role - Lambda - Permissions [LambdaExecute, AmazonRekognitionFullAccess, AmazonS3FullAccess] - Role name [LambdaRekognitionDemoRole]

### No Amazon S3
 - Criar dois buckets:
 - S3 Console
  - Create bucket - name [dio-live-rekognition-input-data]
  - Create bucket - name [dio-live-rekognition-output-data]

### No Amazon Lambda
 - Create function - Use a blueprint [s3-get-object-python]
 - Use an existing role - Trigger [dio-live-rekognition-input-data]
 - Code - inserir o código de exemplo da pasta ```/src``` do respositório (Atualizar o nome do bucket S3 de destino)
 - Deploy

#### Configurações adicionais
 - Selecionar a função criada - Configuration - General configuration - Timeout [1 minuto]
