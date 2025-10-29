# app/utils.py
import os
import socket
import boto3
from botocore.exceptions import ClientError

# Configuración S3 desde variables de entorno
S3_BUCKET = os.environ.get('S3_BUCKET', 'pokeneas-images-2025')
S3_REGION = os.environ.get('S3_REGION', 'us-east-1')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


def get_container_id():
    """
    Obtiene el ID del contenedor Docker.
    Usa socket.gethostname() que devuelve el container ID en Docker.
    """
    return socket.gethostname()


def get_s3_client():
    """Crea y devuelve un cliente de S3 configurado"""
    try:
        s3_client = boto3.client(
            's3',
            region_name=S3_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        return s3_client
    except Exception as e:
        print(f"Error creando cliente S3: {e}")
        return None


def get_s3_image_url(image_name):
    """
    Genera la URL pública de una imagen en S3.
    
    Args:
        image_name: nombre del archivo en S3
    
    Returns:
        URL completa de la imagen
    """
    return f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{image_name}"


def upload_image_to_s3(file, filename):
    """
    Sube una imagen a S3 (opcional, por si quieres agregar funcionalidad)
    
    Args:
        file: archivo a subir
        filename: nombre con el que se guardará
    
    Returns:
        True si se subió correctamente, False si hubo error
    """
    s3_client = get_s3_client()
    
    if not s3_client:
        return False
    
    try:
        s3_client.upload_fileobj(
            file,
            S3_BUCKET,
            filename,
            ExtraArgs={
                'ACL': 'public-read',
                'ContentType': 'image/png'
            }
        )
        return True
    except ClientError as e:
        print(f"Error subiendo imagen a S3: {e}")
        return False


def validate_environment():
    """
    Valida que las variables de entorno necesarias estén configuradas.
    Útil para debugging.
    """
    required_vars = ['S3_BUCKET', 'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY']
    missing_vars = []
    
    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"⚠️ Variables de entorno faltantes: {', '.join(missing_vars)}")
        return False
    
    print("✓ Todas las variables de entorno están configuradas")
    return True
