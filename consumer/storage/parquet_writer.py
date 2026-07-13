import pandas as pd
from datetime import datetime

def write_parquet_file(buffer, output_path):
    df = pd.DataFrame(buffer)
    df.to_parquet(output_path, engine='pyarrow', index=False)

def parquet_file_name_builder(buffer, timestamp):
    timestamp = timestamp.strftime("%Y%m%d_%H%M%S_%f")
    return f"bronze/clientes_teste_{timestamp}.parquet"