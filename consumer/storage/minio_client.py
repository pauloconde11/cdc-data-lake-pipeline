from minio import Minio
from config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_SECURE

#montando o cliente

def create_minio_client():
    return Minio(
        endpoint=MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=MINIO_SECURE,
    )

def minio_upload(client, bucket_name, local_file_path, object_name):
    client.fput_object(
        bucket_name,
        object_name,
        local_file_path
    )
    print(f"Upload realizado com sucesso para o MinIO: {object_name}")