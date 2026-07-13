                PostgreSQL
                     │
                     ▼
            WAL (Write Ahead Log)
                     │
                     ▼
                Debezium CDC
                     │
                     ▼
                   Kafka
                     │
                     ▼
             Kafka Consumer
                     │
                     ▼
            Buffer (Micro Batch)
                     │
                     ▼
          Conversão para Parquet
                     │
                     ▼
             Upload para MinIO