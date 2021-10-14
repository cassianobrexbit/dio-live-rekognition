import json
import os
import urllib.parse
import boto3

s3 = boto3.client('s3')
rekognition = boto3.client("rekognition")

def lambda_handler(event, context):

    # Obter o arquivo do bucket S3
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    out_bucket = "dio-live-output-demo-test"
    try:
      
        # Processamento da imagem recebida e detecção de padrões
        response = rekognition.detect_labels(Image = {"S3Object": {"Bucket": bucket, "Name": key}}, MinConfidence = 70)
        print(response)
        
        # Geração do arquivo de resposta
        response_path = os.path.splitext(key)[0] + '.json'
        s3.put_object(Body=json.dumps(response["Labels"]), Bucket=out_bucket, Key=response_path)
        
        return 'Concluído!'
    except Exception as e:
        print(e)
        raise e
