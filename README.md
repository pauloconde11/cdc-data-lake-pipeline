# 🚀 CDC Data Lake Pipeline

Pipeline de **Change Data Capture (CDC)** desenvolvido para simular uma arquitetura moderna de ingestão de dados. O projeto captura alterações em um banco PostgreSQL utilizando **Debezium** e **Apache Kafka**, realiza micro-batching em Python, converte os eventos para o formato **Apache Parquet** e armazena os arquivos em um bucket **MinIO**, simulando a camada **Bronze** de um Data Lake compatível com Amazon S3.

## 📌 Arquitetura

```text
                PostgreSQL
                     │
                     ▼
             WAL (Logical Decoding)
                     │
                     ▼
               Debezium CDC
                     │
                     ▼
                Apache Kafka
                     │
                     ▼
             Python Consumer
                     │
                     ▼
            Micro-Batching
                     │
                     ▼
             Apache Parquet
                     │
                     ▼
      MinIO (Bronze Data Lake)
```

---

## 🛠️ Tecnologias

* Python
* PostgreSQL
* Debezium
* Apache Kafka
* Apache Parquet (PyArrow)
* Pandas
* MinIO (S3 Compatible Object Storage)
* Docker & Docker Compose

---

## ⚙️ Funcionalidades

* Captura de alterações no PostgreSQL utilizando CDC.
* Publicação automática dos eventos em tópicos Kafka.
* Consumo dos eventos por um consumidor Python.
* Agrupamento de eventos em micro-batches por tamanho.
* Conversão dos eventos para arquivos Apache Parquet.
* Upload automático dos arquivos para um bucket MinIO.
* Organização da camada Bronze para futura evolução do pipeline.

---

## 📁 Estrutura do Projeto

```text
consumer/
├── kafka/
├── storage/
│   ├── parquet_writer.py
│   └── minio_client.py
├── readers/
├── inspectors/
├── main.py
└── config.py
```

---

## 🎯 Objetivo

Este projeto foi desenvolvido com fins de estudo para compreender, na prática, como funciona um pipeline moderno de ingestão de dados utilizado em ambientes de Engenharia de Dados.

O foco desta primeira etapa foi implementar todo o fluxo de ingestão, desde a captura das alterações no banco de dados até o armazenamento dos arquivos Parquet em um Object Storage compatível com Amazon S3.

---

## 🚧 Próximos Passos

* Leitura dos arquivos armazenados no MinIO.
* Implementação da camada Silver.
* Orquestração do pipeline com Apache Airflow.
* Processamento distribuído com Apache Spark.
* Evolução para uma arquitetura completa de Lakehouse.

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.
