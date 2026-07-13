from kafka_consumer import create_kafka_consumer
from storage.parquet_writer import write_parquet_file
from storage.parquet_writer import parquet_file_name_builder
from storage.minio_client import create_minio_client
from storage.minio_client import minio_upload
from datetime import datetime
import json

MAX_BUFFER_SIZE_BYTES = 2 * 1024  # 2 KB
BRONZE_BUCKET = "cdc-clientes"
BRONZE_PREFIX = "bronze/clientes"

def get_event_size_bytes(event):
    event_json = json.dumps(event, ensure_ascii=False)
    return len(event_json.encode("utf-8"))

def main():
    consumer = create_kafka_consumer()
    client = create_minio_client()
    buffer = []
    buffer_size_bytes = 0  
    
    
    for message in consumer:

        if message.value is None:
            print("Mensagem nula recebida, ignorando...")
            continue
        
        event = message.value
        event_size_bytes = get_event_size_bytes(event)

        buffer.append(event)
        buffer_size_bytes += event_size_bytes

        if buffer_size_bytes >= MAX_BUFFER_SIZE_BYTES:
            timestamp = datetime.now()
            output_path = parquet_file_name_builder("clientes", timestamp)
            object_name = f"{BRONZE_PREFIX}/{timestamp.strftime('%Y-%m-%d')}/{output_path.split('/')[-1]}"

            write_parquet_file(buffer, output_path)
            minio_upload(client, BRONZE_BUCKET, output_path, object_name)

            buffer.clear()
            buffer_size_bytes = 0

        print(f"evento recebido. Total no buffer: {len(buffer)}")
        print(f"Tamanho do buffer em bytes: {buffer_size_bytes} bytes")



if __name__ == "__main__":
    main()